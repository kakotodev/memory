<script setup>

import { ref } from 'vue';

const MenuBurger = ref(false);

const ActiverMenuBurger = () => {
    MenuBurger.value = !MenuBurger.value
}


</script>

<template>
    <header class="flex justify-center">
        <div class="flex justify-between w-9/10">
            <div>
                <h1>MEMORY</h1>
            </div>
            <div class="flex items-center">
                <nav>
                    <div>
                        <button @click="ActiverMenuBurger" class="block lg:hidden"><span>☰</span></button>
                    </div>
                    <div class="hidden lg:block">
                        <a href="">Accueil</a>
                        <a href="">Leaderboard</a>
                    </div>
                </nav>
            </div>
        </div>
        <div v-if="MenuBurger" class="flex items-center top-14 absolute lg:hidden">
            <nav class="flex flex-col">
                <a href="">Accueil</a>
                <a href="">Leaderboard</a>
            </nav>
        </div>
    </header>
</template>

<style scoped>

    @media (min-width: 1024px){
        a {
            margin: 25px;
        }
    }
</style>