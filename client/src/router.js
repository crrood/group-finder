import { createRouter, createWebHistory } from 'vue-router'
import LandingPage from './components/LandingPage.vue'
import PlayerProfile from './components/PlayerProfile.vue'

const routes = [
  {
    path: '/',
    name: 'landingPage',
    component: LandingPage
  },
  {
    path: '/playerProfile',
    name: 'PlayerProfile',
    component: PlayerProfile
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
