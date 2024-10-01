<template>
    <div>
        <div id="plotly-chart" ref="scatterPlot"></div>
    </div>
</template>

<script lang="ts">
import { defineComponent, ref, watch, onMounted } from 'vue';
import Plotly from 'plotly.js-dist';

export default defineComponent({
    props: {
        penguinData: {
            type: Array,
            required: true,
        },
    },
    setup(props) {
        const scatterPlot = ref<HTMLElement | null>(null);
        const updatePlot = () => {
            if (!Array.isArray(props.penguinData) || props.penguinData.length === 0) {
                console.error('No penguin data available to plot.');
                return;
            }

            const data = [{
                x: props.penguinData.map(p => p.flipper_length_mm),
                y: props.penguinData.map(p => p.body_mass_g),
                mode: 'markers',
                type: 'scatter',
                marker: { size: 10, color: 'blue' },
            }];

            const layout = {
                title: 'Penguin Flipper Length vs Body Mass',
                xaxis: { title: 'Flipper Length (mm)' },
                yaxis: { title: 'Body Mass (g)' },
            };

            if (scatterPlot.value) {
                Plotly.newPlot(scatterPlot.value, data, layout);
            }
        };



        watch(() => props.penguinData, updatePlot);

        onMounted(updatePlot);

        return { scatterPlot };
    },
});
</script>

<style scoped>
#plotly-chart {
    width: 100%;
    height: 500px;
}
</style>
