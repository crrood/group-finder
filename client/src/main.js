import { createApp } from 'vue'
import App from './App.vue'
import router from './router.js'
import './styles.css'
import { createAuth0 } from '@auth0/auth0-vue'

const app = createApp(App)

// Vuejs router
app.use(router)

// Auth0 user authentication
app.use(
  createAuth0({
    domain: "dev-w5wu3a3y.us.auth0.com",
    client_id: "MFMZf4OTOtI5BybWD7AsJeNtIXoK5U7L",
    redirect_uri: window.location.origin
  })
);

// mount app to index.html
app.mount('#app')
