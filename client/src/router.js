import { authGuard } from '@auth0/auth0-vue'
import { createRouter, createWebHistory } from 'vue-router'
import LandingPage from './components/LandingPage.vue'
import PlayerProfile from './components/PlayerProfile.vue'
import UserProfile from './components/UserProfile.vue'

const routes = [
  {
    path: '/',
    name: 'LandingPage',
    component: LandingPage
  },
  {
    path: '/playerProfile',
    name: 'PlayerProfile',
    component: PlayerProfile
  },
  {
    path: '/userProfile',
    name: 'UserProfile',
    component: UserProfile,
    beforeEnter: authGuard
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
