<script setup>
import { RouterLink } from 'vue-router';
</script>

<template>
    <router-link 
        to="/" 
        class="px-4 py-2 rounded-lg text-gray-600 dark:text-gray-300 hover:bg-blue-50 hover:text-blue-600 dark:hover:bg-gray-800 transition-all font-medium"
        active-class="bg-blue-50 text-blue-600 dark:bg-gray-800 dark:text-blue-400 font-bold"
    >
        Accueil
    </router-link>
    <router-link 
        to="/leaderboard" 
        class="px-4 py-2 rounded-lg text-gray-600 dark:text-gray-300 hover:bg-blue-50 hover:text-blue-600 dark:hover:bg-gray-800 transition-all font-medium"
        active-class="bg-blue-50 text-blue-600 dark:bg-gray-800 dark:text-blue-400 font-bold"
    >
        Classement
    </router-link>
</template>
