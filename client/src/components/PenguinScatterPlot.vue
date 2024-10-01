<template>
    <div>
        <div id="plotly-chart" ref="plotlyChart"></div>
    </div>
</template>

<script lang="ts">
import { defineComponent, ref, watch } from 'vue';
import Plotly from 'plotly.js-dist';

export default defineComponent({
    props: {
        penguinData: {
            type: Array,
            required: true,
        },
    },
    setup(props) {
        const plotlyChart = ref<HTMLElement | null>(null);

        const updatePlot = () => {
            if (!Array.isArray(props.penguinData) || props.penguinData.length === 0) {
                console.error('penguinData is not a valid array:', props.penguinData);
                return;
            }

            const traces: any[] = [];

            // Create traces for each penguin species and island
            const speciesAndIslands = [...new Set(props.penguinData.map(p => `${p.species} (${p.island})`))];

            speciesAndIslands.forEach(speciesAndIsland => {
                const [species, island] = speciesAndIsland.split(' (');
                const islandData = props.penguinData.filter(p => p.species === species && p.island === island.slice(0, -1));

                traces.push({
                    x: islandData.map(p => p.flipper_length_mm),
                    y: islandData.map(p => p.body_mass_g),
                    mode: 'markers',
                    type: 'scatter',
                    name: `${species} (${island.slice(0, -1)})`,
                    marker: {
                        size: 10,
                        opacity: 0.8,
                        color: species === 'Adelie' ? 'black' : species === 'Chinstrap' ? 'purple' : 'orange',
                    },
                    text: islandData.map(p => `${p.species}<br>Island: ${p.island}`),
                    hoverinfo: 'text',
                });
            });

            const layout = {
                title: {
                    text: 'Penguin Size, Palmer Station LTER',
                    font: { size: 14 },
                },
                xaxis: {
                    title: 'Flipper Length (mm)',
                    titlefont: { size: 18 },
                    tickfont: { size: 14 },
                    automargin: true,
                },
                yaxis: {
                    title: 'Body Mass (g)',
                    titlefont: { size: 18 },
                    tickfont: { size: 14 },
                    automargin: true,
                },
                showlegend: true,
                margin: {
                    l: 50,
                    r: 50,
                    t: 50,
                    b: 100,
                },
                height: 600,
                width: 800,
            };

            Plotly.newPlot(plotlyChart.value, traces, layout);
        };

        watch(() => props.penguinData, updatePlot);

        return {
            plotlyChart,
        };
    },
});
</script>

<style scoped>
#plotly-chart {
    width: 100%;
    height: 500px;
    border-radius: 8px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
    background-color: #fff;
    padding-bottom: 100px;
    margin: 20px 0;
}
</style>