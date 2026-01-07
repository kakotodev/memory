<script setup>
import { ref } from 'vue';

import SelectedMode from '@/components/SelectedMode.vue';
import SelectedClassique from '@/components/SelectedClassique.vue';
import SelectedEasy from '@/components/SelectedEasy.vue';
import SelectedMedium from '@/components/SelectedMedium.vue';
import SelectedHard from '@/components/SelectedHard.vue';
import SelectedClassement from '@/components/SelectedClassement.vue';

const choix = ref(null)

const updateMode = (modeSelectionner) => {
    choix.value = modeSelectionner
    console.log(choix.value)
}

</script>

<template>
    <main>
        <div id="SectionGame">
            <SelectedMode v-if="choix === null" @select-mode="updateMode($event)"/>
            <SelectedClassique v-else-if="choix === 'Classique'" @select-mode="updateMode($event)" />
            <SelectedEasy v-else-if="choix === 'easy'" @select-mode="updateMode($event)" />
            <SelectedMedium v-else-if="choix === 'medium'" @select-mode="updateMode($event)" />
            <SelectedHard v-else-if="choix === 'hard'" @select-mode="updateMode($event)" />
            <SelectedClassement v-else-if="choix === 'Classement'" @select-mode="updateMode($event)" />
        </div>
    </main>
</template>

<style scoped>

    #SectionGame {
        border: solid;
        width: 1800px;
        height: 900px;
    }
</style>
