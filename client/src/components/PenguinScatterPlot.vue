<template>
    <div>
        <h3>Scatter Plot</h3>
        <div id="scatter-plot" ref="scatterPlot"></div>
    </div>
</template>

<script lang="ts">
import { defineComponent, ref, onMounted } from 'vue';
import Plotly from 'plotly.js-dist';
import { mockPenguinData } from '../mockData';

export default defineComponent({
    setup() {
        const scatterPlot = ref<HTMLElement | null>(null);

        onMounted(() => {
            const data = [{
                x: mockPenguinData.map(p => p.flipper_length_mm),
                y: mockPenguinData.map(p => p.body_mass_g),
                mode: 'markers',
                type: 'scatter',
                marker: { size: 10, color: 'blue' },
            }];

            const layout = {
                title: 'Penguin Flipper Length vs Body Mass',
                xaxis: { title: 'Flipper Length (mm)' },
                yaxis: { title: 'Body Mass (g)' },
            };

            Plotly.newPlot(scatterPlot.value, data, layout);
        });

        return { scatterPlot };
    },
});
</script>

<style scoped>
#scatter-plot {
    width: 100%;
    height: 400px;
}
</style>
