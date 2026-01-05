<script setup>
import { defineEmits } from 'vue';

defineEmits(['select-mode'])

function AlertButton() {
    console.log("Un mode de jeux a été selectioné")
}

</script>

<template>
    <div>
        <div class="place-items-center">
            <h1>Sélectionner un mode de jeux</h1>
        </div>
        <div class="place-items-center">
            <button @click="$emit('select-mode','Classique'); AlertButton()">Classique</button>
            <button @click="$emit('select-mode', 'Survie'); AlertButton()">Survie</button>
        </div>  
    </div>
</template>

<style scoped>
    button {
        display: flex;
        
        font-size: 30px;
    }
</style>