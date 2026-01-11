<script setup>
import { ref } from 'vue';
import headerNav from './headerNav.vue';

const MenuBurger = ref(false);

const ActiverMenuBurger = () => {
    MenuBurger.value = !MenuBurger.value
}
</script>

<template>
    <header class="bg-white dark:bg-gray-900 shadow-sm sticky top-0 z-50">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex justify-between h-16 items-center">
                <!-- Logo -->
                <div class="flex-shrink-0">
                    <router-link to="/">
                         <h1 class="text-2xl font-black tracking-tight bg-gradient-to-r from-blue-600 to-indigo-600 bg-clip-text text-transparent">
                            MEMORY
                        </h1>
                    </router-link>
                </div>

                <!-- Desktop Nav -->
                <div class="hidden lg:flex items-center gap-8">
                    <nav class="flex gap-6">
                        <headerNav />
                    </nav>
                </div>

                <!-- Mobile Menu Button -->
                <div class="flex items-center lg:hidden">
                    <button @click="ActiverMenuBurger" class="p-2 rounded-md text-gray-600 hover:text-blue-600 hover:bg-gray-100 dark:text-gray-300 dark:hover:bg-gray-800 transition-colors">
                        <span class="sr-only">Open menu</span>
                        <svg v-if="!MenuBurger" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16" />
                        </svg>
                        <svg v-else class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
                        </svg>
                    </button>
                </div>
            </div>
        </div>

        <!-- Mobile Menu -->
        <div v-show="MenuBurger" class="lg:hidden absolute w-full bg-white dark:bg-gray-900 border-b border-gray-100 dark:border-gray-800 shadow-lg">
            <nav class="flex flex-col p-4 space-y-2">
                 <headerNav />
            </nav>
        </div>
    </header>
</template>

<style scoped>
</style>
