<script lang="ts">
import { defineComponent, ref } from 'vue';

export default defineComponent({
  emits: ['updateFilters'],
  setup(_, { emit }) {
    const selectedSpecies = ref('');
    const selectedIsland = ref('');

    const applyFilters = () => {
      emit('updateFilters', {
        species: selectedSpecies.value,
        island: selectedIsland.value,
      });
    };

    return {
      selectedSpecies,
      selectedIsland,
      applyFilters,
    };
  },
});
</script>

<template>
    <div>
        <h3>Filter Controls</h3>
        <div>
            <label for="species">Select Species:</label>
            <select v-model="selectedSpecies" @change="applyFilters">
                <option value="">All</option>
                <option value="Adelie">Adelie</option>
                <option value="Chinstrap">Chinstrap</option>
                <option value="Gentoo">Gentoo</option>
            </select>
        </div>

        <div>
            <label for="island">Select Island:</label>
            <select v-model="selectedIsland" @change="applyFilters">
                <option value="">All</option>
                <option value="Biscoe">Biscoe</option>
                <option value="Dream">Dream</option>
                <option value="Torgersen">Torgersen</option>
            </select>
        </div>
    </div>
</template>

<style scoped>
</style>
