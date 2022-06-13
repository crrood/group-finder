<template>
  <div class="flex">
    <div class="flex basis-4/12 justify-center h-96 bg-gray-300">
      <img class="rounded-full max-w-full" :src='state.character.photo.fullsize'>
    </div>
    <div class="flex basis-8/12 justify-evenly bg-gray-100">
      <p class="font-beyond-wonderland text-7xl">{{ state.character.name }}</p>
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