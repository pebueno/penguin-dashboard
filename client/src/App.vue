<template>
  <div id="app">
    <h1>Penguin Visualizations by Size</h1>
    <Dashboard />
  </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import Dashboard from './components/Dashboard.vue';

export default defineComponent({
  components: {
    Dashboard,
  },
});
</script>

<style>
</style>
