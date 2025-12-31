<script setup>

</script>

<template>
    <main>
        <div>
            <div class="place-items-center">
                <h1>Classement</h1>
                <h3>Voici les classement</h3>
                <div class="place-items-center py-8">
                    <nav>
                        <router-link to="/play">Jouer au jeux</router-link>
                        <router-link to="/rules">Regles du jeux</router-link>
                    </nav>
                </div>
            </div>
            <div id="SectionLb" class="flex">
                <div class="lb"></div>
                <div class="lb"></div>
                <div class="lb"></div>
            </div>
        </div>
    </main>
</template>

<style scoped>

    #SectionLb {
        margin-bottom: 100px;
    }

    .lb {

        border: solid;

        margin-right: 5px;
        margin-left: 5px;

        height: 800px;
        width: 300px;
    }
</style>