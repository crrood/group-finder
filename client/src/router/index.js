import { createRouter, createWebHistory } from 'vue-router'
import LandingPage from '@/components/LandingPage.vue'
import PlayerProfilePreview from '@/components/PlayerProfilePreview.vue'
import PlayerProfile from '@/components/PlayerProfile.vue'

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
  },
  {
    path: '/playerProfile',
    name: 'PlayerProfile',
    component: PlayerProfile
  }
]

const router = createRouter({
  history: createWebHistory(process.env.BASE_URL),
  routes
})

export default router
