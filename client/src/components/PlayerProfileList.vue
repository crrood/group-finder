<template>
  <PlayerProfileListEntry
    v-for="character in state.characters"
    :key="character._id.$oid"
    :character="character"
  />
</template>

<script setup>
import { reactive, inject } from 'vue';
import PlayerProfileListEntry from './PlayerProfileListEntry.vue';

const state = reactive({
  characters: []
})

const axios = inject('axios');
function getCharacterList(page_number) {
  const path = '/playerCharacters?page=' + page_number
  axios.get(path)
    .then(res => {
      state.characters = res.data;
    })
    .catch(error => {
      console.error(error);
    })
}

getCharacterList(0);

</script>