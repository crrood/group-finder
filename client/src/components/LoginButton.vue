<template>
  <div>
    <div v-if="!state.isAuthenticated">
      <button class="btn-primary" @click="login">
        Log in
      </button>
    </div>
    <div v-else class="flex gap-4">
      <button class="btn-primary" @click="logout">
        Log out
      </button>
    </div>
  </div>
</template>

<script setup>
import { useAuth0 } from '@auth0/auth0-vue';
import { reactive, watch } from 'vue';

const auth0 = useAuth0();

const state = reactive({
  user: auth0.user,
  isAuthenticated: auth0.isAuthenticated,
  isLoading: auth0.isLoading
});

watch(() => state.isLoading, isLoading => {
  if (!isLoading && state.isAuthenticated) {
    console.log(state.user.sub);
    console.log(state.user.email);
  }
});

function login() {
  auth0.loginWithRedirect({ redirect_uri: 'http://localhost:3000/' });
}

function logout() {
  auth0.logout({ returnTo: 'http://localhost:3000/' });
}

</script>