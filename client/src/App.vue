<template>
  <div id="app">
    <h1>Penguin Dashboard</h1>
    <FilterControls @updateFilters="updateFilters" />
    <PenguinList :penguinData="filteredPenguinData" />
    <PenguinScatterPlot :penguinData="filteredPenguinData" />
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, computed } from 'vue';
import PenguinList from './components/PenguinList.vue';
import PenguinScatterPlot from './components/PenguinScatterPlot.vue';
import FilterControls from './components/FilterControls.vue';
import { mockPenguinData } from './mockData';

export default defineComponent({
  components: {
    PenguinList,
    PenguinScatterPlot,
    FilterControls,
  },
  setup() {
    const penguinData = ref(mockPenguinData);
    const selectedSpecies = ref('');
    const selectedIsland = ref('');

    const updateFilters = (filters) => {
      selectedSpecies.value = filters.species;
      selectedIsland.value = filters.island;
    };

    const filteredPenguinData = computed(() => {
      return penguinData.value.filter(penguin => {
        const speciesMatch = selectedSpecies.value ? penguin.species === selectedSpecies.value : true;
        const islandMatch = selectedIsland.value ? penguin.island === selectedIsland.value : true;
        return speciesMatch && islandMatch;
      });
    });

    return {
      penguinData,
      updateFilters,
      filteredPenguinData,
    };
  },
});
</script>

<style scoped>
</style>
