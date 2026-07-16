<template>
  <Header />

  <main>
    <RouterView />
  </main>
</template>

<script setup>
import Header from './components/Header.vue'
import { RouterView } from 'vue-router'
</script>

<style>
main {
  padding: 30px;
}
</style>