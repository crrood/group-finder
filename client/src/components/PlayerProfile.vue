<template>
  <div class="flex">
    <div class="flex basis-4/12 justify-center h-96 bg-gray-300">
      <img class="rounded-full max-w-full" :src='state.profilePicture'>
    </div>
    <div class="flex basis-8/12 justify-evenly bg-gray-100">
      <p class="font-beyond-wonderland text-7xl">{{ state.name }}</p>
    </div>
  </div>
  <div class="flex justify-center">
    <button class="btn-primary" @click='getProfile'>Thump it!</button>
  </div>
</template>

<script setup>
import { inject, reactive } from 'vue';

// reactive state
const state = reactive({
  id: 1,
  name: 'Placeholder name',
  profilePicture: 'https://placekitten.com/250/384'
});

// methods
const axios = inject('axios');
function getProfile() {
  const path = '/playerProfiles/' + state.id;
  axios.get(path)
    .then(res => {
      console.log(res.data);
      state.name = res.data.name;
      state.profilePicture = res.data.thumbnail;
    })
    .catch(error => {
      console.error(error);
    })
}

// lifecycle hooks

</script>