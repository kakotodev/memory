<script setup>
import { defineEmits } from 'vue';

defineEmits(['select-mode'])

function AlertButton() {
    console.log("Un mode de jeux a été selectioné")
}

</script>

<template>
    <div class="flex flex-col items-center justify-center py-12 px-4">
        <h1 class="text-3xl md:text-5xl font-bold mb-12 text-gray-900 dark:text-white text-center">
            Sélectionner un mode de jeu
        </h1>
        <div class="flex flex-wrap gap-8 justify-center">
            <button 
                @click="$emit('select-mode','Classique'); AlertButton()"
                class="group relative overflow-hidden px-10 py-8 bg-white dark:bg-gray-800 rounded-3xl shadow-xl hover:shadow-2xl transition-all duration-300 transform hover:-translate-y-1 w-72 border border-gray-100 dark:border-gray-700"
            >
                <div class="absolute inset-0 bg-gradient-to-br from-blue-50 to-indigo-50 dark:from-gray-800 dark:to-gray-700 opacity-0 group-hover:opacity-100 transition-opacity"></div>
                <div class="relative z-10 flex flex-col items-center gap-4">
                    <span class="text-4xl">🎮</span>
                    <span class="text-xl font-bold text-gray-900 dark:text-white group-hover:text-blue-600 dark:group-hover:text-blue-400 transition-colors">Partie Classique</span>
                </div>
            </button>

            <button 
                @click="$emit('select-mode', 'Classement'); AlertButton()"
                class="group relative overflow-hidden px-10 py-8 bg-gradient-to-br from-blue-600 to-indigo-600 rounded-3xl shadow-xl hover:shadow-2xl transition-all duration-300 transform hover:-translate-y-1 w-72"
            >
                <div class="absolute inset-0 bg-white/10 opacity-0 group-hover:opacity-100 transition-opacity"></div>
                <div class="relative z-10 flex flex-col items-center gap-4">
                    <span class="text-4xl">🏆</span>
                    <span class="text-xl font-bold text-white">Mode Classement</span>
                </div>
            </button>
        </div>  
    </div>
</template>

<style scoped>
</style>
