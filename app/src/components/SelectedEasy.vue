<script setup>
    import { ref, onMounted, onUnmounted } from 'vue';
    
    const emit = defineEmits(['select-mode', 'game-win'])

    const card = ref([])
    const flippedCards = ref([])
    
    // Stats
    const timer = ref(0)
    const attempts = ref(0)
    let intervalId = null

    const setupGame = () => {
        // Reset stats
        timer.value = 0
        attempts.value = 0
        clearInterval(intervalId)
        startTimer()

        const symbols = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'];
        // Create pairs and flatten
        const deck = [...symbols, ...symbols];

        // Shuffle and map to card objects
        card.value = deck
            .sort(() => Math.random() - 0.5)
            .map((val, index) => ({
                id: index, 
                value: val,
                isFlipped: false,
                isMatched: false
            }));
    }

    const startTimer = () => {
        intervalId = setInterval(() => {
            timer.value++
        }, 1000)
    }

    const stopTimer = () => {
        clearInterval(intervalId)
    }

    const formatTime = (seconds) => {
        const mins = Math.floor(seconds / 60)
        const secs = seconds % 60
        return `${mins}:${secs.toString().padStart(2, '0')}`
    }

    const flipCard = (selectedCard) => {
        // Prevent clicking if already flipped, matched, or if 2 cards are already flipped
        if (selectedCard.isFlipped || selectedCard.isMatched || flippedCards.value.length === 2) {
            return 
        }

        selectedCard.isFlipped = true 
        flippedCards.value.push(selectedCard)

        if (flippedCards.value.length === 2) {
            attempts.value++ // Increment attempts
            checkMatch()
        }
    }

    const checkMatch = () => {
        const [card1, card2] = flippedCards.value

        if (card1.value === card2.value) {
            card1.isMatched = true
            card2.isMatched = true
            flippedCards.value = []

            // Check for Win Condition
            if (card.value.every(c => c.isMatched)) {
                stopTimer()
                const score = { time: timer.value, attempts: attempts.value }
                console.log("Game Won!", score)
                emit('game-win', score)
            }

        } else {
            setTimeout(() => {
                card1.isFlipped = false
                card2.isFlipped = false
                flippedCards.value = []
            }, 1000)
        }
    }

    onMounted(setupGame)
    onUnmounted(() => clearInterval(intervalId))

</script>

<template>
    <div class="flex flex-col items-center justify-center min-h-[50vh] p-4">
        <h2 class="text-3xl font-bold mb-4 text-white">Mode : Facile</h2>
        
        <!-- Stats Bar -->
        <div class="flex gap-8 mb-6 bg-white px-8 py-3 rounded-full text-gray-900 shadow-lg border border-gray-200">
            <div class="flex flex-col items-center">
                <span class="text-xs uppercase tracking-wider text-gray-500">Temps</span>
                <span class="text-2xl font-mono font-bold">{{ formatTime(timer) }}</span>
            </div>
            <div class="w-px bg-gray-200"></div>
            <div class="flex flex-col items-center">
                <span class="text-xs uppercase tracking-wider text-gray-500">Essais</span>
                <span class="text-2xl font-mono font-bold">{{ attempts }}</span>
            </div>
        </div>

        <div class="grid grid-cols-4 gap-4 p-4">
            <div 
                v-for="c in card" 
                :key="c.id" 
                class="card-container cursor-pointer w-24 h-32"
                @click="flipCard(c)"
            >
                <div class="card-inner w-full h-full relative transition-transform duration-500" :class="{ 'is-flipped': c.isFlipped || c.isMatched }">
                    <div class="card-front absolute inset-0 bg-indigo-600 rounded-xl flex items-center justify-center shadow-lg backface-hidden border-2 border-indigo-400">
                        <span class="text-white text-4xl font-bold">?</span>
                    </div>

                    <div class="card-back absolute inset-0 bg-white rounded-xl flex items-center justify-center shadow-lg backface-hidden rotate-y-180 border-2 border-indigo-600">
                        <span class="text-4xl font-bold text-indigo-800">{{ c.value }}</span>
                    </div>
                </div>
            </div>
        </div>
        
        <button 
            @click="$emit('select-mode', null)" 
            class="mt-8 px-6 py-2 bg-white text-indigo-600 font-bold rounded-full hover:bg-indigo-50 transition-colors shadow-lg"
        >
            Retour au menu
        </button>
    </div>
</template>

<style scoped>
.card-container {
    perspective: 1000px;
}

.card-inner {
    transform-style: preserve-3d;
}

.card-inner.is-flipped {
    transform: rotateY(180deg);
}

.backface-hidden {
    backface-visibility: hidden;
}

.rotate-y-180 {
    transform: rotateY(180deg);
}
</style>