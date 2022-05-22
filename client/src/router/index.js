import { createRouter, createWebHistory } from 'vue-router'
import LandingPage from '@/components/LandingPage.vue'
import PlayerProfilePreview from '@/components/PlayerProfilePreview.vue'

const routes = [
  {
    path: '/',
    name: 'landingPage',
    component: LandingPage
  },
  {
    path: '/playerProfilePreview',
    name: 'PlayerProfilePreview',
    component: PlayerProfilePreview
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
