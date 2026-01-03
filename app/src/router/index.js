import { createRouter, createWebHistory } from 'vue-router'
import AccueilView from '@/views/AccueilView.vue'
import ReglesView from '@/views/ReglesView.vue'
import ClassementView from '@/views/ClassementView.vue'
import GameModeView from '@/views/GameModeView.vue'

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
    {
      path: '/leaderboard',
      name: 'classement',
      component: ClassementView
    },
    {
      path: '/play',
      name: 'play',
      component: GameModeView
    },
    {
      path: '/selection-niveau',
      name: 'selection-niveau',
      component: () => import('../views/SelectionNiveauView.vue')
    }
  ],
})

export default router
