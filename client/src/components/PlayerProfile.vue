<template>
  <div class="grid grid-cols-12">
    <!-- Character Photo -->
    <div class="col-span-4 flex justify-center h-96 bg-gray-300">
      <img class="rounded-full max-w-full" :src='state.character.photo.fullsize'>
    </div>
    <div class="col-span-8 grid grid-cols-12 grid-rows-6 bg-gray-100">
      <p class="col-span-12 row-span-2 font-beyond-wonderland text-center text-7xl bg-gray-400">{{
        state.character.name}}</p>
      <!-- Physical Details -->
      <div class="col-span-12 row-span-4 flex flex-wrap gap-x-12 justify-evenly p-5">
        <label v-for="detail in Object.keys(state.character.details)" :key="detail">
          <span class="">{{ capitalize(detail) }}: </span>
          <input type="text" class="border-0 border-b-2 border-gray-200 focus:border-black focus:ring-0"
            size=15 v-model="state.character.details[detail]">
        </label>
      </div>
      <!-- Stats -->
    </div>
    <div class="col-span-12 flex justify-evenly gap-x-12 bg-blue-100">
      <span v-for="(value, name) in state.character.stats" class="border-2 border-black text-center bg-blue-200">
        <input type="text" class="border-0 border-b-2 border-gray-200 text-center focus:border-black focus:ring-0"
          max-length=2 size=2 v-model="state.character.stats[name]">
          <hr>
        {{ name }}
      </span>
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
    details: {
      "race": "",
      "class": "",
      "background": "",
      "level": 1,
      "gender": "",
      "height": "",
      "weight": ""
    },
    "stats": {
      "strength": 0,
      "dexterity": 0,
      "constitution": 0,
      "intelligence": 0,
      "wisdom": 0,
      "charisma": 0
    },
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

function capitalize(str) {
  return str[0].toUpperCase() + str.substring(1);
}

// lifecycle hooks

</script>