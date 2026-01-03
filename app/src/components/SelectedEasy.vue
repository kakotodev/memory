<script setup>
    import { ref, onMounted } from 'vue';

    const card = ref([])
    const flippedCards = ref([])

    const setupGame = () => {
        const cartes = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H'];
        const deck = [cartes, cartes];

        cartes.value = deck.sort(() => Math.random() - 0.5).map((lettre, index) => ({
            id: index, 
            value: lettre,
            isFlipped: false,
            isMatched: false
            }))
        }

        const flipCard = (card) => {
            if (card.isFlipped || flippedCards.value.length === 2) {
            return 
        }
            card.isFlipped = true 
            flippedCards.value.push(card)
        }
        if (flippedCards.value.length === 2) {
            checkMatch()
        }

        const checkMatch = () => {
            const [card1, card2] = flippedCards

            if (card1.value === card2.value) {
                card1.isMatched = true
                card2.isMatched = true
                flippedCards.value = []
            } else {
                setTimeout(() => {
                    card1.isFlipped = false
                    card2.isFlipped = false
                    flippedCards.value = []
                }, 1000)
            }
        }

        onMounted(setupGame)

</script>

<template>
    <h2>Mode : {{  choix  }}</h2>
    <div class="grid grid-cols-4 gap-4 bg-gray-200 p-6 rounded-xl shadow-inner">
        <div class="absolute inset-0 bg-indigo-600 rounded-lg flex items-center justify-center shadow-md backface-hidden">
          <span class="text-white text-3xl font-bold">?</span>
        </div>
        <div class="absolute inset-0 bg-white rounded-lg flex items-center justify-center shadow-md rotate-y-180 backface-hidden border-2 border-indigo-500">
          <span class="text-4xl">{{ card.value }}</span>
        </div>
    </div>

</template>

<style scoped>

</style>