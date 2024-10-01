<template>
    <div>
        <h3>Penguin List <i>(mocky data)</i></h3> 
        <ul>
            <li v-for="penguin in penguinData" :key="penguin.flipper_length_mm">
                SPECIE: {{ penguin.species }} - Island: {{ penguin.island }}: Flipper length: {{ penguin.flipper_length_mm }} mm, Body mass: {{ penguin.body_mass_g }} g
            </li>
        </ul>
    </div>
</template>

<script lang="ts">
import { defineComponent } from 'vue';
import { mockPenguinData } from '../mockData';

export default defineComponent({
    data() {
        return {
            penguinData: mockPenguinData,
        };
    },
});
</script>

<style scoped>
i {
    font-size: 12px;
    font-weight: 400;
}
</style>
