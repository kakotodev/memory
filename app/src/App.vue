<script setup>
import { RouterLink, RouterView } from 'vue-router'

// pages
import AccueilView from './views/AccueilView.vue';


// templates 
import Header from '@/components/Header.vue';
import Footer from '@/components/Footer.vue';

</script>

<template>
  <Header />
  <AccueilView />
  <Footer />
</template>

