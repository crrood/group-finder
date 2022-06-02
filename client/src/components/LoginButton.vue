<template>
  <div>
    <button v-if="!state.isAuthenticated" @click="login">
      Log in
    </button>
    <button v-else @click="logout">
      Log out
    </button>
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