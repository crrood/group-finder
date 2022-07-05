<template>
  <img class="rounded-full max-w-full" :src='character.photo.thumbnail'>
  <div>Name: {{ character.name }}</div>
</template>

<script setup>
defineProps(['character']);
</script>