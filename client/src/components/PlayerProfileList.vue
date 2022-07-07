<template>
  <div class="bg-parchment">
    <PlayerProfileListEntry 
      v-for="playerCharacter in state.playerCharacters" 
      :key="playerCharacter._id.$oid"
      :playerCharacter="playerCharacter" />
  </div>
</template>

<script setup>
import { reactive, inject } from 'vue';
import PlayerProfileListEntry from './PlayerProfileListEntry.vue';

const state = reactive({
  playerCharacters: [],
  page_number: 0
})

const axios = inject('axios');
function getPlayerCharacterList(page_number) {
  const path = '/playerCharacters?page=' + page_number
  axios.get(path)
    .then(res => {
      state.playerCharacters = res.data;
    })
    .catch(error => {
      console.error(error);
    })
}

getPlayerCharacterList(state.page_number);

</script>