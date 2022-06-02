<template>
  <div>
    <p>Here's a user profile, alright</p>
    <button class="btn-primary" @click="showAuth">Get token</button><hr>
    <code>{{ state.token }}</code>
  </div>
</template>

<script setup>
import { reactive } from 'vue';
import { useAuth0 } from '@auth0/auth0-vue';

// reactive state
const state = reactive({
  user: useAuth0()
});

async function showAuth() {
  state.user.getAccessTokenSilently()
    .then(token => {
      state.token = token;
    })
    .catch(e => {
      state.token = e;
    });
}

</script>