<template>
    <div id="filter-div">
        <h3 class="filter-title">Filter Controls</h3>
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
    </div>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue';

export default defineComponent({
    emits: ['updateFilters'],
    setup(_, { emit }) {
        const selectedSpecies = ref('');
        const selectedIsland = ref('');

        const applyFilters = () => {
            emit('updateFilters', { species: selectedSpecies.value, island: selectedIsland.value });
        };

        return {
            selectedSpecies,
            selectedIsland,
            applyFilters,
        };
    },
});
</script>

<style scoped>
.filter-title {
    font-size: 1.5rem;
    margin-bottom: 10px;
    font-weight: 500;
    color: #333;
}

.filter-group {
    margin-bottom: 15px;
}

.filter-group label {
    font-size: 0.9rem;
    color: #555;
    margin-bottom: 5px;
    display: block;
}

.filter-select {
    width: 100%;
    padding: 8px;
    border: 1px solid #ccc;
    border-radius: 4px;
    font-size: 1rem;
}

.filter-select:focus {
    outline: none;
    border-color: #3f51b5;
    box-shadow: 0 0 5px rgba(63, 81, 181, 0.3);
}
</style>
