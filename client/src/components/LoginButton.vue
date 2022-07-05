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
import { reactive, watch, inject } from 'vue';

const auth0 = useAuth0();
const axios = inject('axios');

const state = reactive({
  user: auth0.user,
  isAuthenticated: auth0.isAuthenticated,
  isLoading: auth0.isLoading
});

watch(() => state.isLoading, isLoading => {
  if (!isLoading && state.isAuthenticated) {
    const path = '/users/' + state.user.sub;
    const user = {
      auth0Id: state.user.sub,
      email: state.user.email
    }

    axios.put(path, user)
      .then(res => {
        console.log(res);
      })
      .catch(error => {
        console.log(error);
      })
  }
});

function login() {
  auth0.loginWithRedirect({ redirect_uri: 'http://localhost:3000/' });
}

function logout() {
  auth0.logout({ returnTo: 'http://localhost:3000/' });
}

</script>