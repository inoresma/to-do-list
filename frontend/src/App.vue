<script setup>
import HelloWorld from './components/HelloWorld.vue'
</script>

<template>
  <div class="min-h-screen bg-blue-900 py-6 flex flex-col justify-center sm:py-12">
    <div class="relative py-3 sm:max-w-xl sm:mx-auto">
      <div class="relative px-4 py-10 bg-white shadow-lg sm:rounded-3xl sm:p-20">
        <div class="max-w-md mx-auto">
          <div class="divide-y divide-gray-200">
            <div class="py-8 text-base leading-6 space-y-4 text-gray-700 sm:text-lg sm:leading-7">
              <div class="flex items-center space-x-4">
                <a href="https://vitejs.dev" target="_blank">
                  <img src="/vite.svg" class="h-12 w-12 hover:scale-110 transition-transform" alt="Vite logo" />
                </a>
                <a href="https://vuejs.org/" target="_blank">
                  <img src="./assets/vue.svg" class="h-12 w-12 hover:scale-110 transition-transform" alt="Vue logo" />
                </a>
              </div>
              <HelloWorld msg="Vite + Vue + Tailwind" class="mt-8" />
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<style>
/* You can remove the previous styles since we'll use Tailwind classes */
</style>
