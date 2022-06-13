<template>
  <div class="grid grid-cols-12">
    <div class="col-span-4 flex justify-center h-96 bg-gray-300">
      <img class="rounded-full max-w-full" :src='state.character.photo.fullsize'>
    </div>
    <div class="col-span-8 grid grid-cols-12 bg-gray-100">
      <p class="col-span-12 font-beyond-wonderland text-center text-7xl">{{ state.character.name }}</p>
      <div class="col-span-12 grid grid-cols-12 ml-3">
        <span class="col-span-3">Race: {{ state.character.race }}</span>
        <span class="col-span-3">Gender: {{ state.character.gender }}</span>
        <span class="col-span-3">Height: {{ state.character.height }}</span>
        <span class="col-span-3">Weight: {{ state.character.weight }}</span>
      </div>
    </div>
  </div>
  <div class="flex justify-center">
    <button class="btn-primary" @click='getCharacter'>Thump it!</button>
  </div>
</template>

<script setup>
import { inject, reactive } from 'vue';

// reactive state
const state = reactive({
  id: 1,
  // placeholder data while page is loading
  character: {
    name: 'Placeholder name',
    photo: {
      fullsize: 'https://placekitten.com/250/384'
    }
  }
});

// methods
const axios = inject('axios');
function getCharacter() {
  const path = '/playerCharacters/' + state.id;
  axios.get(path)
    .then(res => {
      console.log(res.data);
      state.character = res.data;
    })
    .catch(error => {
      console.error(error);
    })
}

// lifecycle hooks

</script>