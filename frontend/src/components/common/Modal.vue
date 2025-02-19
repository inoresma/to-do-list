<template>
  <div class="fixed inset-0 z-50 overflow-y-auto" @click.self="$emit('close')">
    <div class="flex min-h-full items-end justify-center p-4 text-center sm:items-center sm:p-0">
      <div class="relative transform overflow-hidden rounded-lg bg-white px-4 pb-4 pt-5 text-left shadow-xl transition-all sm:my-8 sm:w-full sm:max-w-lg sm:p-6">
        <div class="absolute right-0 top-0 pr-4 pt-4">
          <button 
            type="button" 
            class="rounded-md bg-white text-gray-400 hover:text-gray-500 focus:outline-none focus:ring-2 focus:ring-primary focus:ring-offset-2"
            @click="$emit('close')"
          >
            <span class="sr-only">Cerrar</span>
            <XMarkIcon class="h-6 w-6" />
          </button>
        </div>
        <div class="sm:flex sm:items-start">
          <div class="mt-3 text-center sm:mt-0 sm:text-left w-full">
            <h3 class="text-lg font-medium leading-6 text-gray-900">
              <slot name="title"></slot>
            </h3>
            <div class="mt-4">
              <slot name="content"></slot>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { XMarkIcon } from '@heroicons/vue/24/outline'
</script> 