import { createApp } from 'vue'
import App from './App.vue'
import router from './router.js'
import './styles.css'
import { createAuth0 } from '@auth0/auth0-vue'
import axios from 'axios'

const app = createApp(App)

// Vuejs router
app.use(router)

// Auth0 user authentication
app.use(
  createAuth0({
    domain: import.meta.env['VITE_AUTH0_DOMAIN'],
    client_id: import.meta.env['VITE_AUTH0_CLIENT_ID']
  })
);

// global variables
const axiosInstance = axios.create({
  baseURL: 'http://localhost'
})
app.provide('axios', axiosInstance)

// mount app to index.html
app.mount('#app')
