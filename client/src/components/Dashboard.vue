<template>
    <div class="dashboard">
        <h2>Penguin Visualizations by Size</h2>
        <div class="dashboard-content">
            <div class="chart-container">
                <h3>Scatter Plot</h3>
                <PenguinScatterPlot :penguinData="penguinData" />
                <hr class="divider" />
                <h3>Histogram</h3>
                <PenguinHistogram :penguinData="penguinData" />
            </div>

            <div class="sidebar">
                <FilterControls @updateFilters="updateFilters" />
                <div class="slider-container">
                    <div class="slider-group">
                        <label for="flipper-length">Flipper Length (mm):</label>
                        <input type="range" id="flipper-length" v-model="flipperLength" min="170" max="230"
                            @input="applyFilters" class="slider" />
                        <span>{{ flipperLength }}</span>
                    </div>

                    <div class="slider-group">
                        <label for="body-mass">Body Mass (g):</label>
                        <input type="range" id="body-mass" v-model="bodyMass" min="2500" max="6500"
                            @input="applyFilters" class="slider" />
                        <span>{{ bodyMass }}</span>
                    </div>
                </div>
            </div>
        </div>
    </div>
</template>

<script lang="ts">
import { defineComponent, ref, onMounted } from 'vue';
import axios from 'axios';
import PenguinScatterPlot from './PenguinScatterPlot.vue';
import PenguinHistogram from './PenguinHistogram.vue';
import FilterControls from './FilterControls.vue';

export default defineComponent({
    components: {
        PenguinScatterPlot,
        PenguinHistogram,
        FilterControls,
    },
    setup() {
        const penguinData = ref([]);
        const flipperLength = ref(200);
        const bodyMass = ref(4000);

        const fetchPenguinData = async (filters = {}) => {
            try {
                const response = await axios.post('http://127.0.0.1:5000/api/data', filters);
                penguinData.value = response.data;
                console.log('Fetched Penguin Data:', penguinData.value);
            } catch (error) {
                console.error('Error fetching penguin data:', error);
            }
        };

        const updateFilters = (filters) => {
            fetchPenguinData(filters);
        };

        const applyFilters = () => {
            const filters = {
                flipper_length_mm: flipperLength.value,
                body_mass_g: bodyMass.value,
            };
            fetchPenguinData(filters);
        };

        onMounted(() => fetchPenguinData());

        return {
            penguinData,
            updateFilters,
            flipperLength,
            bodyMass,
            applyFilters,
        };
    },
});
</script>

<style scoped>
.dashboard {
    max-width: 1200px;
    margin: 0 auto;
    padding: 20px;
}

.dashboard-content {
    display: flex;
    gap: 20px;
}

.chart-container {
    flex: 1;
    margin-top: 20px;
}

.sidebar {
    width: 250px;
    padding: 20px;
    background-color: #f9f9f9;
    border-radius: 8px;
    box-shadow: 0 2px 10px rgba(0, 0, 0, 0.1);
}

.slider-container {
    margin-top: 20px;
}

.slider-group {
    margin-bottom: 20px;
}

.slider {
    width: 100%;
    -webkit-appearance: none;
    height: 6px;
    border-radius: 5px;
    background: #ccc;
    outline: none;
    transition: background 0.3s;
}

.slider::-webkit-slider-thumb {
    -webkit-appearance: none;
    appearance: none;
    width: 20px;
    height: 20px;
    border-radius: 50%;
    background: #3f51b5;
    cursor: pointer;
}

.slider::-moz-range-thumb {
    width: 20px;
    height: 20px;
    border-radius: 50%;
    background: #3f51b5;
    cursor: pointer;
}

.slider-container span {
    display: block;
    margin-top: 5px;
    text-align: center;
    font-size: 14px;
}
</style>
