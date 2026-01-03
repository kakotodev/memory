<script setup>
import { RouterLink } from 'vue-router';
</script>

<template>
    <main>
        <div class="pb-66">
            <div class="place-items-center">
                <h1>Sélectionner un </h1>
                <h1 style="padding-left: 3rem;">niveau</h1>
            </div>
            
            <div class="place-items-center py-8">
                <nav class="flex flex-col space-y-6 place-items-center">
                    <router-link to="/game/4x4" class="btn">
                        4 x 4
                    </router-link>
                    
                    <router-link to="/game/5x5" class="btn">
                        5 x 5
                    </router-link>
                    
                    <router-link to="/game/6x6" class="btn" >
                        6 x 6
                    </router-link>

                     <router-link to="/play" class="btn" >
                        Retour
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
