<script setup>
import Navbar from './components/common/Navbar.vue'
</script>

<template>
  <div class="bg-background min-h-screen">
    <Navbar />
    <main>
      <router-view />
    </main>
  </div>
</template>