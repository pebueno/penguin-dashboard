<template>
    <div class="slider-control">
        <label for="flipper-length">Flipper Length (mm):</label>
        <input type="range" id="flipper-length" min="170" max="230" step="1" v-model="flipperLength"
            @input="applyFilters" class="slider" />
        <span>{{ flipperLength }}</span>

        <label for="body-mass">Body Mass (g):</label>
        <input type="range" id="body-mass" min="2500" max="6500" step="10" v-model="bodyMass" @input="applyFilters"
            class="slider" />
        <span>{{ bodyMass }}</span>
    </div>
</template>

<script lang="ts">
import { defineComponent, ref } from 'vue';

export default defineComponent({
    emits: ['updateFilters'],
    setup(_, { emit }) {
        const flipperLength = ref(200); // Default value
        const bodyMass = ref(4000); // Default value

        const applyFilters = () => {
            emit('updateFilters', {
                flipper_length_mm: flipperLength.value,
                body_mass_g: bodyMass.value,
            });
        };

        return {
            flipperLength,
            bodyMass,
            applyFilters,
        };
    },
});
</script>

<style scoped>
.slider-control {
    display: flex;
    flex-direction: column;
    gap: 10px;
    padding: 20px;
    border-radius: 8px;
    background-color: #f9f9f9;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

.slider {
    width: 100%;
}

label {
    font-size: 0.9rem;
    color: #555;
}
</style>
