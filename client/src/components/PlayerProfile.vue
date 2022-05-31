<template>
  <div class="tile is-ancestor">
    <div class="tile is-parent">
      <div class="tile is-child is-3 is-warning notification">
        <img :src='state.thumbnail'>
      </div>
      <div class="tile is-child is-info notification">
        <p class="title">{{ state.name }}</p>
      </div>
    </div>
  </div>
  <button @click='getProfile'>Thump it!</button>
</template>

<script setup>
import axios from 'axios';
import { reactive } from 'vue';

// reactive state
const state = reactive({
  id: 1,
  name: 'Placeholder name',
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