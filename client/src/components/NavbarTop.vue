<template>
  <nav class="flex gap-4 p-2 bg-primary font-rise-of-kingdom text-white" role="navigation"
    aria-label="main navigation">
    <div class="">
      <router-link class="" to="/">
        <img class="w-24 h-24" src="https://placekitten.com/96/96">
      </router-link>
    </div>

    <div class="flex justify-start place-items-center gap-8 text-2xl">
      <router-link class="" to="/playerProfileList">
        PlayerProfileList
      </router-link>
    </div>

    <div class="flex grow pr-4 justify-end place-items-center text-lg">
      <LoginButton />
    </div>
  </nav>
</template>

<script setup>

import LoginButton from './LoginButton.vue'

</script>