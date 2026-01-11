<script setup>  
import { RouterLink } from 'vue-router';
</script>

<template>
    <main class="flex-grow flex flex-col items-center justify-center min-h-[85vh] relative overflow-hidden bg-gray-50 dark:bg-gray-950">
        <!-- Background decorative elements -->
        <div class="absolute top-0 left-0 w-full h-full overflow-hidden z-0 opacity-30 pointer-events-none">
            <div class="absolute -top-40 -right-40 w-96 h-96 bg-blue-400 rounded-full blur-3xl opacity-20 animate-pulse"></div>
            <div class="absolute top-40 -left-20 w-72 h-72 bg-indigo-400 rounded-full blur-3xl opacity-20"></div>
        </div>

        <div class="z-10 text-center px-4 max-w-4xl mx-auto">
            <h1 class="text-6xl md:text-8xl font-black mb-8 tracking-tight">
                <span class="bg-clip-text text-transparent bg-gradient-to-r from-blue-600 via-indigo-600 to-purple-600 dark:from-blue-400 dark:via-indigo-400 dark:to-purple-400 animate-gradient">
                    MEMORY
                </span>
            </h1>
            
            <h3 class="text-xl md:text-2xl text-gray-600 dark:text-gray-300 mb-16 font-light max-w-2xl mx-auto leading-relaxed">
                Exercez votre mémoire avec notre jeu de cartes classique. 
                <br class="hidden md:block" />
                Êtes-vous prêt à relever le défi ?
            </h3>
            
            <nav class="flex flex-col sm:flex-row gap-6 justify-center items-center">
                <router-link 
                    to="/play" 
                    class="group relative px-8 py-4 bg-blue-600 text-white rounded-full text-lg font-bold shadow-lg hover:shadow-blue-500/50 transition-all hover:-translate-y-1 w-64 sm:w-auto"
                >
                    <span class="relative z-10 flex items-center justify-center gap-2">
                        Jouer maintenant 
                        <span class="group-hover:translate-x-1 transition-transform">→</span>
                    </span>
                    <div class="absolute inset-0 rounded-full bg-white/20 opacity-0 group-hover:opacity-100 transition-opacity"></div>
                </router-link>

                <router-link 
                    to="/rules" 
                    class="group px-8 py-4 bg-white dark:bg-gray-800 text-gray-700 dark:text-white border border-gray-200 dark:border-gray-700 rounded-full text-lg font-bold shadow-sm hover:shadow-lg hover:border-blue-500/50 transition-all hover:-translate-y-1 w-64 sm:w-auto"
                >
                    Règles du jeu
                </router-link>
            </nav>
        </div>
    </main>
</template>

<style scoped>
@keyframes gradient {
    0% { background-position: 0% 50%; }
    50% { background-position: 100% 50%; }
    100% { background-position: 0% 50%; }
}
.animate-gradient {
    background-size: 200% auto;
    animation: gradient 4s linear infinite;
}
</style>