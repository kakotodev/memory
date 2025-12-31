<script setup>
import { defineEmits } from 'vue';

defineEmits(['select-mode'])

</script>

<template>
    <div class="place-items-center">
        <h1>Sélectionner un mode de jeux</h1>
    </div>
    <div class="place-items-center">
        <button @click="$emit('select-mode','Classique')">Classique</button>
        <button @click="$emit('select-mode', 'Survie')">Survie</button>
    </div>
</template>

<style scoped>
    button {
        display: flex;
        
        font-size: 30px;
    }
</style>