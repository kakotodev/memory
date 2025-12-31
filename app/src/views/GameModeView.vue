<script setup>
import { RouterLink } from 'vue-router';
</script>

<template>
    <main>
        <div class="pb-66">
            <div class="place-items-center">
                <h1>Sélectionner un </h1>
                <h1 style="padding-left: 3rem;">mode de jeux</h1>
            </div>
            
            <div class="place-items-center py-8">
                <nav class="flex flex-col space-y-6 place-items-center">
                    <router-link to="/" class="btn">
                        Classique
                    </router-link>
                    
                    <router-link to="/" class="btn">
                        Survie
                    </router-link>
                    
                    <router-link to="/" class="btn" >
                        Quitter
                    </router-link>
                </nav>
            </div>
        </div>
    </main>
</template>

<style scoped>
    .btn {
        padding: 1rem;
        background-color: white;
        color: black;
        border: 1px solid black;
        width: 16rem;
        text-align: center;
    }
</style>
