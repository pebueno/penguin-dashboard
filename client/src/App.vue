<template>
  <div id="app">
      <h1>Penguin Dashboard</h1>
      <PenguinList />
      <PenguinScatterPlot />
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import PenguinList from './components/PenguinList.vue';
import PenguinScatterPlot from './components/PenguinScatterPlot.vue';

export default defineComponent({
  components: {
      PenguinList,
      PenguinScatterPlot,
  },
});
</script>

<style>
/* Global styles can go here */
#app {
  max-width: 800px;
  margin: 0 auto;
}
</style>
