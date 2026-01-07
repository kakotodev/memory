<script setup>
import { defineEmits } from 'vue';

defineEmits(['select-mode'])

function AlertButton() {
    console.log("Un mode de jeux a été selectioné")
}

</script>

<template>
    <div class="place-items-center">
        <div class="place-items-center">
            <h1>Sélectionner un mode de jeux</h1>
        </div>
        <div>
            <button @click="$emit('select-mode','easy'); AlertButton()">Facile</button>
            <button @click="$emit('select-mode','medium'); AlertButton()">Moyen</button>
            <button @click="$emit('select-mode','hard'); AlertButton()">Difficile</button>
        </div>
    </div>
</template>

<style scoped>
    button {
        display: flex;
        
        font-size: 30px;
    }
</style>