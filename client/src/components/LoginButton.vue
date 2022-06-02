<template>
  <div>
    <div v-if="!state.isAuthenticated">
      <button class="btn-primary" @click="login">
        Log in
      </button>
    </div>
    <div v-else class="flex gap-4">
      <button class="btn-warning" @click="logout">
        Log out
      </button>
      <router-link to="UserProfile">
        <button class="btn-primary">
          User Profile
        </button>
      </router-link>
    </div>
  </div>
</template>

<script setup>
import { useAuth0 } from '@auth0/auth0-vue';
import { reactive } from 'vue';

const auth0 = useAuth0();

const state = reactive({
  user: auth0.user,
  isAuthenticated: auth0.isAuthenticated,
  isLoading: auth0.isLoading
});

function login() {
  auth0.loginWithRedirect();
}

function logout() {
  auth0.logout({ returnTo: window.location.origin });
}

</script>