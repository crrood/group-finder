<template>
  <div>
    <p>{{ state.response }}</p>
  </div>
</template>

<script setup>
import axios from 'axios';
import { onMounted, reactive } from 'vue';

// reactive state
const state = reactive({
  response: "Loading..."
});

// methods
onMounted(() => {
  const path = 'http://localhost:5000/';
  axios.get(path)
    .then(res => {
      state.response = res.data;
    })
    .catch(error => {
      console.error(error);
    })
})

// lifecycle hooks

</script>