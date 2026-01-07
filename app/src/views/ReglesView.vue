<script setup>  

</script>

<template>
    <main>
        <div class="pb-128">
            <h1>Les règles du jeux</h1>
            <div class="sectionRegle">
                <h3>Regle</h3>
                <div>Le but du jeu est de retrouver toutes les paires de cartes identiques. Retournez deux cartes à la fois pour essayer de trouver une correspondance.</div>
            </div>
            <div class="sectionRegle">
                <h3>Objectif</h3>
                <div>Réussir le plus vite possible</div>
            </div>
        </div>
    </main>
</template>

<style scoped>
    .sectionRegle {
        margin-bottom: 50px;
        margin-top: 50px;

        @media (max-width: 1024px){
            margin-bottom: 20px;
            margin-top: 20px;            
        }

    }

    h1 {
        margin-bottom: 50px;

        @media (max-width: 1024px){
            margin-bottom: 20px;
            display: flex;
            justify-content: center;   
        }
    }
</style>