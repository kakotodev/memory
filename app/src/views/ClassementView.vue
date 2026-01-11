<script setup>

</script>

<template>
    <main class="min-h-screen py-16 px-4 bg-gray-50 dark:bg-gray-900">
        <div class="max-w-7xl mx-auto">
            <div class="text-center mb-16">
                <h1 class="text-4xl md:text-5xl font-bold mb-4 text-gray-900 dark:text-white">Classement</h1>
                <h3 class="text-xl text-gray-600 dark:text-gray-400">Découvrez les meilleurs joueurs</h3>
            </div>

            <div class="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-8">
                <!-- Leaderboard Columns -->
                <div class="bg-white dark:bg-gray-800 rounded-3xl shadow-lg border border-gray-100 dark:border-gray-700 min-h-[500px] p-8 flex flex-col relative overflow-hidden group hover:shadow-xl transition-shadow">
                    <div class="absolute top-0 left-0 w-full h-2 bg-gradient-to-r from-yellow-400 to-orange-500"></div>
                    <h2 class="text-2xl font-bold mb-6 text-gray-800 dark:text-white flex items-center gap-2">
                        <span>🥇</span> Facile
                    </h2>
                    <div class="flex-grow flex items-center justify-center text-gray-400 italic">
                        Aucun score enregistré
                    </div>
                </div>
                
                <div class="bg-white dark:bg-gray-800 rounded-3xl shadow-lg border border-gray-100 dark:border-gray-700 min-h-[500px] p-8 flex flex-col relative overflow-hidden group hover:shadow-xl transition-shadow">
                    <div class="absolute top-0 left-0 w-full h-2 bg-gradient-to-r from-blue-400 to-indigo-500"></div>
                    <h2 class="text-2xl font-bold mb-6 text-gray-800 dark:text-white flex items-center gap-2">
                        <span>🥈</span> Moyen
                    </h2>
                    <div class="flex-grow flex items-center justify-center text-gray-400 italic">
                        Aucun score enregistré
                    </div>
                </div>

                <div class="bg-white dark:bg-gray-800 rounded-3xl shadow-lg border border-gray-100 dark:border-gray-700 min-h-[500px] p-8 flex flex-col relative overflow-hidden group hover:shadow-xl transition-shadow">
                     <div class="absolute top-0 left-0 w-full h-2 bg-gradient-to-r from-red-400 to-pink-500"></div>
                    <h2 class="text-2xl font-bold mb-6 text-gray-800 dark:text-white flex items-center gap-2">
                        <span>🥉</span> Difficile
                    </h2>
                    <div class="flex-grow flex items-center justify-center text-gray-400 italic">
                        Aucun score enregistré
                    </div>
                </div>
            </div>
            
             <div class="mt-16 text-center">
                 <router-link 
                    to="/" 
                    class="inline-flex items-center text-blue-600 dark:text-blue-400 font-semibold hover:underline"
                >
                    <span class="mr-2">←</span> Retour à l'accueil
                </router-link>
            </div>
        </div>
    </main>
</template>

<style scoped>
</style>