<template>
  <div>
      <div id="histogram" ref="histogramDiv"></div>
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, watch } from 'vue';
import Plotly from 'plotly.js-dist';

export default defineComponent({
  props: {
      penguinData: {
          type: Array,
          required: true
      },
      flipperLength: {
          type: Number,
          required: true,
      },
      bodyMass: {
          type: Number,
          required: true,
      },
  },
  setup(props) {
      const histogramDiv = ref<HTMLElement | null>(null);

      const updateHistogram = () => {
          if (!Array.isArray(props.penguinData) || props.penguinData.length === 0) {
              console.error('penguinData is not a valid array:', props.penguinData);
              return;
          }

          const bodyMassData = props.penguinData.map(p => p.body_mass_g);

          const trace = {
              x: bodyMassData,
              type: 'histogram',
              marker: {
                  color: 'rgba(255, 99, 132, 0.6)',
                  line: {
                      color: 'rgba(255, 99, 132, 1)',
                      width: 1,
                  },
              },
              xbins: {
                  start: 2500,
                  end: 6500,
                  size: 100,
              }
          };

          const layout = {
              title: {
                  text: 'Body Mass Distribution',
                  font: { size: 14 },
              },
              xaxis: {
                  title: 'Body Mass (g)',
                  titlefont: { size: 14 },
                  tickfont: { size: 12 },
              },
              yaxis: {
                  title: 'Count',
                  titlefont: { size: 14 },
                  tickfont: { size: 12 },
              },
              margin: {
                  t: 20,
                  b: 40,
                  l: 50,
                  r: 20,
              },
          };

          // Clear any existing plot before creating a new one
          Plotly.purge(histogramDiv.value);
          Plotly.newPlot(histogramDiv.value, [trace], layout);
      };

      watch(() => props.penguinData, updateHistogram);

      return {
          histogramDiv
      };
  },
});
</script>

<style scoped>
#histogram {
  width: 100%;
  height: 400px;
  border-radius: 8px;
  box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
  background-color: #fff;
  padding: 20px 0; 
  margin-top: 20px;
}
</style>