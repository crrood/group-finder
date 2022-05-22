<template>
  <div>
    <img :src='state.thumbnail'>
    <p>{{ state.name }}</p>
    <p>{{ state.id }}</p>
    <button @click='getProfile'>Thump it!</button>
  </div>
</template>

<script setup>
import axios from 'axios';
import { reactive } from 'vue';

// reactive state
const state = reactive({
  id: 1,
  name: 'Thumper Strongbottom',
  thumbnail: 'https://www.iana.org/_img/2022/iana-logo-header.svg'
});

// methods
function getProfile() {
  const path = 'http://localhost:5000/playerProfiles/' + state.id;
  axios.get(path)
    .then(res => {
      console.log(res.data);
      state.name = res.data.name;
      state.thumbnail = res.data.thumbnail;
    })
    .catch(error => {
      console.error(error);
    })
}

// lifecycle hooks

</script>