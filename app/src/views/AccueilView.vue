<script setup>  

import { RouterLink } from 'vue-router';

</script>

<template>
    <main>
        <div class="pb-24">
            <div class="place-items-center">
                <h1>JOUER A MEMORY</h1>
                <h3>êtes-vous prête a relevez le défi ?</h3>
            </div>
            <div class="place-items-center py-8">
                <nav>
                    <router-link to="/play">Jouer au jeu</router-link>
                    <router-link to="/rules">Regles du jeu</router-link>
                </nav>
            </div>
        </div>
    </main>
</template>

<style scoped>
    
</style>