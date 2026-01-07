<script setup>
    import { ref, onMounted } from 'vue';

    const ScoresEasy = ref([]);
    const ScoresMedium = ref([]);
    const ScoresHard = ref([]);

    const loadScoreEasy = async (diff) => {
        try {
            const response = await fetch(`http://127.0.0.1:8000/api/scores/easy`);
            if (response.ok) {
            ScoresEasy.value = await response.json();
            }
        } catch (error) {
            console.error("Erreur lors de la récupération des scores", error);
        }
    };

    const loadScoreMedium = async (diff) => {
        try {
            const response = await fetch(`http://127.0.0.1:8000/api/scores/medium`);
            if (response.ok) {
            ScoresMedium.value = await response.json();
            }
        } catch (error) {
            console.error("Erreur lors de la récupération des scores", error);
        }
    };

    const loadScoreHard = async (diff) => {
        try {
            const response = await fetch(`http://127.0.0.1:8000/api/scores/hard`);
            if (response.ok) {
            ScoresHard.value = await response.json();
            }
        } catch (error) {
            console.error("Erreur lors de la récupération des scores", error);
        }
    };

    onMounted(() => {
        loadScoreEasy('easy');
        loadScoreMedium('medium');
        loadScoreHard('hard');
    });
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
            <h1>Classement globales</h1>
            <div id="SectionLb" class="flex">
                <div class="lb">
                    <h2>Classement Easy</h2>
                    <ul>
                        <li v-for="score in ScoresEasy" :key="score.id">
                            {{ score.name }} - Temps: {{ score.time }}s - Tentatives: {{ score.attempts }}
                        </li>
                    </ul>
                </div>
                <div class="lb">
                    <h2>Classement Medium</h2>
                    <ul>
                        <li v-for="score in ScoresMedium" :key="score.id">
                            {{ score.name }} - Temps: {{ score.time }}s - Tentatives: {{ score.attempts }}
                        </li>
                    </ul>
                </div>
                <div class="lb">
                    <h2>Classement Hard</h2>
                    <ul>
                        <li v-for="score in ScoresHard" :key="score.id">
                            {{ score.name }} - Temps: {{ score.time }}s - Tentatives: {{ score.attempts }}
                        </li>
                    </ul>
                </div>
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