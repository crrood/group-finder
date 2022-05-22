<template>
  <nav>
    <router-link to="/">Home</router-link> |
    <router-link to="/playerProfilePreview">PlayerProfilePreview</router-link>
  </nav>
  <router-view/>
</template>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

nav {
  padding: 30px;
  background-color: #2c3e50;
}

nav a {
  font-weight: bold;
  color: #FFFFFF;
}

nav a.router-link-exact-active {
  color: #42b983;
}

router-view {
  border-color: #2c3e50;
}
</style>
