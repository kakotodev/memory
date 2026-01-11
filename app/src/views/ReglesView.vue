<script setup>  

</script>

<template>
    <main class="min-h-screen py-16 px-4 bg-gray-50 dark:bg-gray-900">
        <div class="max-w-4xl mx-auto">
            <h1 class="text-4xl md:text-5xl font-bold text-center mb-16 text-gray-900 dark:text-white">
                Règles du jeu
            </h1>
            
            <div class="space-y-8">
                <!-- But du jeu Card -->
                <div class="bg-white dark:bg-gray-800 rounded-2xl p-8 shadow-sm hover:shadow-md transition-shadow border border-gray-100 dark:border-gray-700">
                    <div class="flex items-start gap-4">
                        <span class="text-4xl">🎯</span>
                        <div>
                            <h3 class="text-2xl font-bold mb-4 text-blue-600 dark:text-blue-400">But du jeu</h3>
                            <p class="text-gray-600 dark:text-gray-300 leading-relaxed text-lg">
                                L'objectif du Memory est simple : retrouver toutes les paires de cartes identiques en un minimum de temps et avec le moins d'essais possible. Exercez votre mémoire visuelle pour réaliser le meilleur score !
                            </p>
                        </div>
                    </div>
                </div>

                <!-- Comment jouer Card -->
                <div class="bg-white dark:bg-gray-800 rounded-2xl p-8 shadow-sm hover:shadow-md transition-shadow border border-gray-100 dark:border-gray-700">
                    <div class="flex items-start gap-4">
                         <span class="text-4xl">🎮</span>
                        <div>
                            <h3 class="text-2xl font-bold mb-4 text-blue-600 dark:text-blue-400">Comment jouer ?</h3>
                            <ul class="space-y-4 text-gray-600 dark:text-gray-300 text-lg">
                                <li class="flex items-start gap-3">
                                    <span class="flex-shrink-0 w-6 h-6 rounded-full bg-blue-100 dark:bg-blue-900 text-blue-600 dark:text-blue-400 flex items-center justify-center text-sm font-bold mt-1">1</span>
                                    <span>Toutes les cartes sont disposées face cachée sur le plateau.</span>
                                </li>
                                <li class="flex items-start gap-3">
                                    <span class="flex-shrink-0 w-6 h-6 rounded-full bg-blue-100 dark:bg-blue-900 text-blue-600 dark:text-blue-400 flex items-center justify-center text-sm font-bold mt-1">2</span>
                                    <span>Cliquez sur une première carte pour la retourner, puis sur une seconde.</span>
                                </li>
                                <li class="flex items-start gap-3">
                                    <span class="flex-shrink-0 w-6 h-6 rounded-full bg-green-100 dark:bg-green-900 text-green-600 dark:text-green-400 flex items-center justify-center text-sm font-bold mt-1">3</span>
                                    <span>Si les images sont <strong>identiques</strong>, c'est une paire ! Les cartes restent visibles.</span>
                                </li>
                                <li class="flex items-start gap-3">
                                    <span class="flex-shrink-0 w-6 h-6 rounded-full bg-red-100 dark:bg-red-900 text-red-600 dark:text-red-400 flex items-center justify-center text-sm font-bold mt-1">4</span>
                                    <span>Si elles sont <strong>différentes</strong>, mémorisez leur position avant qu'elles ne se retournent.</span>
                                </li>
                                <li class="flex items-start gap-3">
                                    <span class="flex-shrink-0 w-6 h-6 rounded-full bg-purple-100 dark:bg-purple-900 text-purple-600 dark:text-purple-400 flex items-center justify-center text-sm font-bold mt-1">5</span>
                                    <span>Continuez jusqu'à avoir trouvé toutes les paires du plateau.</span>
                                </li>
                            </ul>
                        </div>
                    </div>
                </div>
            </div>
            
            <div class="mt-12 text-center">
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