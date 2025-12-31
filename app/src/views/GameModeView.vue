<script setup>
import { ref } from 'vue';

import SelectedMode from '@/components/SelectedMode.vue';

const SelectedMode = ref(null)

const updateMode = (modeSelectionner) => {
    SelectedMode.value = modeSelectionner
}

</script>

<template>
    <main>
        <div id="SectionGame" class="pb-66">
            <SelectedMode v-if="SelectedMode === null" />
        </div>
    </main>
</template>

<style scoped>

    #SectionGame {
        border: solid;
        width: 1800px;
        height: 800px;
    }
</style>
