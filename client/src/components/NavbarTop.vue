<template>
  <nav class="grid grid-cols-12 gap-4 p-2 bg-slate-500 font-rise-of-kingdom text-white" role="navigation" aria-label="main navigation">
    <div class="col-span-1">
      <router-link class="" to="/">
        <img class="w-24 h-24" src="https://placekitten.com/96/96">
      </router-link>
    </div>

    <div class="flex col-span-5 justify-start place-items-center gap-8 text-2xl">
      <router-link class="" to="/playerProfile">
        PlayerProfile
      </router-link>
    </div>

    <div class="flex col-span-5 justify-end place-items-center gap-4 mr-12 text-lg">
      <button class="btn-primary">
        Sign up
      </button>
      <button>
        Log in
      </button>
    </div>
  </nav>
</template>

<script setup>

</script>