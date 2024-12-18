<script setup>
import PerfilUsuario from './components/usuarios/PerfilUsuario.vue'
</script>

<template>
  <div class=" bg-gray-100">
    <nav class="bg-white shadow-sm">
      <div class=" mx-auto px-4 py-3">
        <h1 class="text-xl font-semibold text-gray-800">Todo List App</h1>
      </div>
    </nav>
    
    <main class="">
      <PerfilUsuario />
    </main>
  </div>
</template>

<style>
/* You can remove the previous styles since we'll use Tailwind classes */
</style>
