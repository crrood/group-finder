import { authGuard } from '@auth0/auth0-vue'
import { createRouter, createWebHistory } from 'vue-router'
import LandingPage from './components/LandingPage.vue'
import PlayerProfile from './components/PlayerProfile.vue'
import PlayerProfileList from './components/PlayerProfileList.vue'

const routes = [
  {
    path: '/',
    name: 'LandingPage',
    component: LandingPage
  },
  {
    path: '/playerProfile',
    name: 'PlayerProfile',
    component: PlayerProfile,
    // props: route => ({
    //   playerCharacter: route.params.playerCharacter
    // })
  },
  {
    path: '/playerProfileList',
    name: 'PlayerProfileList',
    component: PlayerProfileList
  }
]

const router = createRouter({
  history: createWebHistory(),
  routes
})

export default router
