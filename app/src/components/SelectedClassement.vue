<script setup>
    import { ref, onMounted } from 'vue';

    const leaderboard = ref([]);

    const loadScores = () => {
    const data = localStorage.getItem('allScores');
    if (data) {
        leaderboard.value = JSON.parse(data);
        }
    };

    const deleteScoreByIndex = (index) => {
        leaderboard.value.splice(index, 1);
        localStorage.setItem('allScores', JSON.stringify(leaderboard.value));
    };

    const deleteScoreAll = () => {
        leaderboard.value = [];
        localStorage.setItem('allScores', JSON.stringify(leaderboard.value));
    };

    const changeName = () => {
        localStorage.setItem('allScores', JSON.stringify(leaderboard.value));
    }
    onMounted(loadScores);
</script>

<template>
    <div class="mt-4">
        <h2 class="text-xl font-bold">Tableau des scores</h2>
        <button @click="deleteScoreAll()">Reset</button>
        <ul>
            <li v-for="(s, index) in leaderboard" :key="index" class="border-b py-1">
            {{ index + 1 }}. {{ s.name }} - {{ s.attempts }} - essais ({{ s.time }}s)
            <button @click="deleteScoreByIndex(index)">X</button>
            <input type="text" v-model="s.name" @keyup.enter="changeName" placeholder="Modifier" />
            <button @click="changeName">Valider</button>
            </li>
        </ul>
    </div>
</template>