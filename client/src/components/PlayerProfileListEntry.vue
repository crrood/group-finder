<template>
  <div @click="router.push({ 
      name: 'PlayerProfile',// + playerCharacter._id.$oid, 
      params: { playerCharacter: JSON.stringify(playerCharacter) } })">
    GO
  </div>
  <img class="rounded-full max-w-full" :src='playerCharacter.photo.thumbnail'>
  <div>Name: {{ playerCharacter.name }}</div>
</template>

<script setup>
import router from '../router';

defineProps(['playerCharacter']);
</script>