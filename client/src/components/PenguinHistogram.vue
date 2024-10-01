<template>
    <div>
      <h3>Body Mass Distribution</h3>
      <div id="histogram" ref="histogramDiv"></div>
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
      const histogramDiv = ref<HTMLElement | null>(null);
  
      const updateHistogram = () => {
        if (!Array.isArray(props.penguinData) || props.penguinData.length === 0) {
          console.error('No penguin data available for histogram.');
          return;
        }
  
        const bodyMassData = props.penguinData.map(p => p.body_mass_g);
  
        const data = [{
          x: bodyMassData,
          type: 'histogram',
          marker: { color: 'rgba(255, 99, 132, 0.6)' },
          xbins: {
            start: 2500,
            end: 6500,
            size: 100,
          },
        }];
  
        const layout = {
          title: 'Body Mass Distribution',
          xaxis: { title: 'Body Mass (g)' },
          yaxis: { title: 'Count' },
        };
  
        if (histogramDiv.value) {
          Plotly.newPlot(histogramDiv.value, data, layout);
        }
      };
  
      watch(() => props.penguinData, updateHistogram); 
  
      // Call updateHistogram on mount to display the initial histogram
      onMounted(updateHistogram); 
  
      return {
        histogramDiv,
      };
    },
  });
  </script>
  
  <style scoped>
  #histogram {
    width: 100%;
    height: 400px;
  }
  </style>
  