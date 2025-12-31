import { createRouter, createWebHistory } from 'vue-router'
import AccueilView from '@/views/AccueilView.vue'
<<<<<<< Updated upstream
=======
import ReglesView from '@/views/ReglesView.vue'
import ClassementView from '@/views/ClassementView.vue'
import GameModeView from '@/views/GameModeView.vue'
>>>>>>> Stashed changes

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'accueil',
      component: AccueilView,
    },
<<<<<<< Updated upstream
=======
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
    }
>>>>>>> Stashed changes
  ],
})

export default router
