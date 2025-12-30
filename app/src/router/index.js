import { createRouter, createWebHistory } from 'vue-router'
import AccueilView from '@/views/AccueilView.vue'
import ReglesView from '@/views/ReglesView.vue'

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'accueil',
      component: AccueilView,
    },
    {
      path: '/rules',
      name: 'regles',
      component: ReglesView,
    },
  ],
})

export default router
