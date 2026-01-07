<script setup>
    import { ref, onMounted } from 'vue';

    const leaderboard = ref([]);

    const isAscending = ref(true);
    const isAscendingAttempts = ref(true);

    const loadScores = () => {
    const data = localStorage.getItem('allScores');
    if (data) {
        leaderboard.value = JSON.parse(data);
        }
    };

    const toggleSortByTime = () => {
        console.log('Trier par temps', isAscending.value ? 'ASC' : 'DESC');
        
        const sorted = [...leaderboard.value].sort((a, b) => {
            return isAscending.value 
                ? parseFloat(a.time) - parseFloat(b.time) 
                : parseFloat(b.time) - parseFloat(a.time);
        });

        leaderboard.value = sorted;
        isAscending.value = !isAscending.value; 
    };

    const toggleSortByAttempts = () => {
        console.log('Trier par attempts', isAscendingAttempts.value ? 'ASC' : 'DESC');
        
        const sorted = [...leaderboard.value].sort((a, b) => {
            return isAscendingAttempts.value 
                ? a.attempts - b.attempts 
                : b.attempts - a.attempts;
        });

        leaderboard.value = sorted;
        isAscendingAttempts.value = !isAscendingAttempts.value;
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

    console.log('Leaderboard:', leaderboard.value);

    onMounted(loadScores);
</script>

<template>
    <div class="mt-4">
        <h2 class="text-xl font-bold">Tableau des scores locales</h2>
        <button @click="deleteScoreAll()">Reset</button>
        <button @click="toggleSortByTime()">Trie par temps</button>
        <button @click="toggleSortByAttempts()">Trier par attempts</button>
        <ul>
            <li v-for="(s, index) in leaderboard" :key="index" class="border-b py-1">
            {{ index + 1 }}. {{ s.name }} - {{ s.attempts }} attempts - essais ({{ s.time }}s) - difficulté : {{ s.diff }}
            <button @click="deleteScoreByIndex(index)">X</button>
            <input type="text" v-model="s.name" @keyup.enter="changeName" placeholder="Modifier" />
            <button @click="changeName">Valider</button>
            </li>
        </ul>
    </div>
</template>