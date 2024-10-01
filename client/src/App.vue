<template>
  <div id="app">
    <h1>Penguin Dashboard</h1>
    <FilterControls @updateFilters="updateFilters" />
    <PenguinList :penguinData="filteredPenguinData" />
    <PenguinScatterPlot :penguinData="filteredPenguinData" />
    <PenguinHistogram :penguinData="filteredPenguinData" />
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, computed } from 'vue';
import PenguinList from './components/PenguinList.vue';
import PenguinScatterPlot from './components/PenguinScatterPlot.vue';
import PenguinHistogram from './components/PenguinHistogram.vue';
import FilterControls from './components/FilterControls.vue';
import { mockPenguinData } from './mockData';

export default defineComponent({
  components: {
    PenguinList,
    PenguinScatterPlot,
    PenguinHistogram,
    FilterControls,
  },
  setup() {
    const penguinData = ref(mockPenguinData);
    const selectedSpecies = ref('');
    const selectedIsland = ref('');
    const flipperLength = ref(170);
    const bodyMass = ref(2500);

    const updateFilters = (filters) => {
      selectedSpecies.value = filters.species;
      selectedIsland.value = filters.island;
      flipperLength.value = filters.flipper_length_mm;
      bodyMass.value = filters.body_mass_g;
    };

    const filteredPenguinData = computed(() => {
      return penguinData.value.filter(penguin => {
        const speciesMatch = selectedSpecies.value ? penguin.species === selectedSpecies.value : true;
        const islandMatch = selectedIsland.value ? penguin.island === selectedIsland.value : true;
        const flipperLengthMatch = penguin.flipper_length_mm >= flipperLength.value;
        const bodyMassMatch = penguin.body_mass_g >= bodyMass.value;

        return speciesMatch && islandMatch && flipperLengthMatch && bodyMassMatch;
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
