<template>
  <PlayerProfileListEntry 
    v-for="playerCharacter in state.playerCharacter" 
    :key="playerCharacter._id.$oid"
    :playerCharacter="playerCharacter" />
</template>

<script setup>
import { reactive, inject } from 'vue';
import PlayerProfileListEntry from './PlayerProfileListEntry.vue';

const state = reactive({
  playerCharacter: []
})

const axios = inject('axios');
function getPlayerCharacterList(page_number) {
  const path = '/playerCharacters?page=' + page_number
  axios.get(path)
    .then(res => {
      state.playerCharacter = res.data;
    })
    .catch(error => {
      console.error(error);
    })
}

getPlayerCharacterList(0);

</script>