<template>
    <div class="filter-controls">
        <h3>Filter Controls</h3>
        <div class="filter-group">
            <label for="species">Select Species:</label>
            <select v-model="selectedSpecies" @change="applyFilters" class="filter-select">
                <option value="">All</option>
                <option value="Adelie">Adelie</option>
                <option value="Chinstrap">Chinstrap</option>
                <option value="Gentoo">Gentoo</option>
            </select>
        </div>

        <div class="filter-group">
            <label for="island">Select Island:</label>
            <select v-model="selectedIsland" @change="applyFilters" class="filter-select">
                <option value="">All</option>
                <option value="Biscoe">Biscoe</option>
                <option value="Dream">Dream</option>
                <option value="Torgersen">Torgersen</option>
            </select>
        </div>

        <div class="filter-group">
            <label for="flipper-length">Flipper Length (mm): {{ flipperLength }}</label>
            <input type="range" id="flipper-length" v-model="flipperLength" min="170" max="230" @input="applyFilters" />
        </div>

        <div class="filter-group">
            <label for="body-mass">Body Mass (g): {{ bodyMass }}</label>
            <input type="range" id="body-mass" v-model="bodyMass" min="2500" max="6500" @input="applyFilters" />
        </div>
    </div>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue';

export default defineComponent({
    emits: ['updateFilters'],
    setup(_, { emit }) {
        const selectedSpecies = ref('');
        const selectedIsland = ref('');
        const flipperLength = ref(200); // Default value
        const bodyMass = ref(4000); // Default value

        const applyFilters = () => {
            emit('updateFilters', { 
                species: selectedSpecies.value, 
                island: selectedIsland.value,
                flipper_length_mm: flipperLength.value,
                body_mass_g: bodyMass.value
            });
        };

        return {
            selectedSpecies,
            selectedIsland,
            flipperLength,
            bodyMass,
            applyFilters,
        };
    },
});
</script>

<style scoped>
.filter-controls {
    margin-bottom: 20px;
    padding: 10px;
    background-color: #f9f9f9;
    border-radius: 8px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

.filter-group {
    margin-bottom: 15px;
}

.filter-group label {
    font-size: 0.9rem;
    color: #555;
}

.filter-select {
    width: 100%;
    padding: 8px;
    border: 1px solid #ccc;
    border-radius: 4px;
}
</style>
