<script setup>
import { RouterView } from 'vue-router'

// pages
import AccueilView from './views/AccueilView.vue';
import ReglesView from './views/ReglesView.vue';
import ClassementView from './views/ClassementView.vue';


// templates 
import Header from '@/components/Header.vue';
import Footer from '@/components/Footer.vue';

</script>

<template>
  <Header />
  <RouterView />
  <Footer />
</template>

