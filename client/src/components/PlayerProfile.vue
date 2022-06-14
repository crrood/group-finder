<template>
  <div class="grid grid-cols-12 bg-parchment">
    <!-- Character Photo -->
    <div class="col-span-4 flex justify-center h-96">
      <img class="rounded-full max-w-full" :src='state.character.photo.fullsize'>
    </div>
    <div class="col-span-8 grid grid-cols-12 grid-rows-6">
      <p class="col-span-12 row-span-2 font-beyond-wonderland text-center text-7xl">{{
        state.character.name}}</p>
      <!-- Physical Details -->
      <div class="col-span-12 row-span-4 flex flex-wrap gap-x-12 justify-evenly p-5">
        <span v-for="(value, name) in state.character.details" :key="name">
          <label>{{ capitalize(name) }}: </label>
          <input type="text"
            class="" size=15
            v-model="state.character.details[name]">
        </span>
      </div>
    </div>
    <!-- Stats -->
    <div class="col-span-12 flex justify-evenly gap-x-12 bg-blue-100">
      <span v-for="(value, name) in state.character.stats" class="border border-black text-center bg-blue-200">
        <input type="number" class="border-0 border-b-2 border-gray-200 text-center focus:border-black focus:ring-0"
          max-length=2 size=2 v-model="state.character.stats[name]">
        <hr>
        <label>{{ capitalize(name) }}</label>
      </span>
    </div>
    <!-- Personality and beliefs -->
    <div class="col-span-12 grid grid-cols-12 gap-4 p-3 bg-blue-200">
      <span v-for="(value, name) in state.character.personality" class="col-span-4 bg-blue-300">
        <label class="">{{ capitalize(name) }}: </label>
        <textarea class="resize-none border-0 border-b-2 border-gray-200 text-center focus:border-black focus:ring-0"
          v-model="state.character.personality[name]"></textarea>
      </span>
    </div>
  </div>

  <!-- Save / load -->
  <div class="flex justify-center py-2 gap-x-4">
    <button class="btn-primary" @click='getCharacter'>Thump in!</button>
    <button class="btn-primary" @click='saveCharacter'>Thump out!</button>
  </div>
</template>

<script setup>
import { inject, reactive } from 'vue';

// reactive state
const state = reactive({
  id: "62a8cd5ab05e4f23a07d2760", // manually set after /resetDB
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
      state.character = JSON.parse(res.data);
    })
    .catch(error => {
      console.error(error);
    })
}

function saveCharacter() {
  const path = '/playerCharacters/' + state.id;
  axios.put(path, state.character)
    .then(res => {
      console.log(res.data);
    })
    .catch(error => {
      console.error(error);
    })
}

function capitalize(str) {
  return str[0].toUpperCase() + str.substring(1);
}

// lifecycle hooks

</script>