<template>
  <router-view />
</template>

<script setup>
// Vue Router owns the application screens.
</script>

<style>
* {
  margin: 0;
  padding: 0;
  box-sizing: border-box;
}

html {
  background: #f7f4ee;
}

body {
  min-width: 320px;
}

#app {
  font-family: Inter, system-ui, -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  color: #17201a;
  background: #f7f4ee;
}

::-webkit-scrollbar {
  width: 10px;
  height: 10px;
}

::-webkit-scrollbar-track {
  background: #eee8dd;
}

::-webkit-scrollbar-thumb {
  background: #9d927f;
  border-radius: 999px;
  border: 2px solid #eee8dd;
}

button,
input,
textarea {
  font-family: inherit;
}
</style>
