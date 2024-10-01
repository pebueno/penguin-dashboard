<template>
  <div id="app">
    <h1>Penguin Dashboard</h1>
    <FilterControls @updateFilters="updateFilters" />
    <PenguinScatterPlot :penguinData="filteredPenguinData" />
    <PenguinHistogram :penguinData="filteredPenguinData" />
  </div>
</template>

<script lang="ts">
import { defineComponent, ref, computed, onMounted } from 'vue';
import PenguinScatterPlot from './components/PenguinScatterPlot.vue';
import PenguinHistogram from './components/PenguinHistogram.vue';
import FilterControls from './components/FilterControls.vue';

interface Penguin {
  species: string;
  island: string;
  flipper_length_mm: number;
  body_mass_g: number;
}

export default defineComponent({
  components: {
    PenguinScatterPlot,
    PenguinHistogram,
    FilterControls,
  },
  setup() {
    const penguinData = ref<Penguin[]>([]); // Initialize as an empty array
    const selectedSpecies = ref<string>('');
    const selectedIsland = ref<string>('');
    const flipperLength = ref<number>(170);
    const bodyMass = ref<number>(2500);

    const updateFilters = (filters: any) => {
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

    const fetchPenguinData = async () => {
      try {
        const response = await fetch('http://127.0.0.1:5000/api/data');
        const data = await response.json();
        penguinData.value = data;
      } catch (error) {
        console.error('Error fetching penguin data:', error);
      }
    };

    onMounted(() => fetchPenguinData());

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
