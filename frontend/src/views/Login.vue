<template>
    <div class="min-h-screen bg-background">
      <div class="flex min-h-screen flex-1 flex-col justify-center px-6 py-12 lg:px-8">
        <div class="sm:mx-auto sm:w-full sm:max-w-sm">
          <h1 class="text-center text-2xl font-bold text-primary">ToDoList</h1>
          <h2 class="mt-6 text-center text-xl font-semibold text-text">Iniciar Sesión</h2>
        </div>
  
        <div class="mt-10 sm:mx-auto sm:w-full sm:max-w-sm">
          <form class="space-y-6" @submit.prevent="handleSubmit">
            <div>
              <label for="username" class="block text-sm font-medium text-text">Usuario</label>
              <div class="mt-2">
                <input 
                  v-model="formData.username"
                  type="text" 
                  name="username" 
                  id="username" 
                  required
                  class="block w-full rounded-md border-0 py-1.5 px-3 text-text shadow-sm ring-1 ring-inset ring-secondary/30 placeholder:text-secondary focus:ring-2 focus:ring-inset focus:ring-primary"
                />
              </div>
            </div>
  
            <div>
              <label for="password" class="block text-sm font-medium text-text">Contraseña</label>
              <div class="mt-2">
                <input 
                  v-model="formData.password"
                  type="password" 
                  name="password" 
                  id="password" 
                  required
                  class="block w-full rounded-md border-0 py-1.5 px-3 text-text shadow-sm ring-1 ring-inset ring-secondary/30 placeholder:text-secondary focus:ring-2 focus:ring-inset focus:ring-primary"
                />
              </div>
            </div>
  
            <div v-if="error" class="text-red-500 text-sm text-center">
              {{ error }}
            </div>
  
            <div>
              <button 
                type="submit"
                :disabled="loading"
                class="flex w-full justify-center rounded-md bg-primary px-3 py-1.5 text-sm font-semibold text-white shadow-sm hover:bg-accent focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-primary disabled:opacity-50 disabled:cursor-not-allowed"
              >
                <span v-if="loading">Iniciando sesión...</span>
                <span v-else>Iniciar Sesión</span>
              </button>
            </div>
          </form>
  
          <p class="mt-10 text-center text-sm text-secondary">
            ¿No tienes una cuenta?
            <router-link to="/registro" class="font-semibold text-primary hover:text-accent">
              Regístrate aquí
            </router-link>
          </p>
        </div>
      </div>
    </div>
  </template>
  
<script setup>
import { ref } from 'vue'
import { useRouter } from 'vue-router'
import { useAuth } from '@/composables/useAuth'

const router = useRouter()
const { obtenerUsuario } = useAuth()

const formData = ref({
  username: '',
  password: ''
})

const loading = ref(false)
const error = ref(null)

const handleSubmit = async () => {
  try {
    loading.value = true
    error.value = null
    
    const csrfToken = document.cookie.split('; ')
      .find(row => row.startsWith('csrftoken='))
      ?.split('=')[1];

    const response = await fetch('/api/login/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrfToken || '',
      },
      body: JSON.stringify(formData.value),
      credentials: 'include'
    })

    if (!response.ok) {
      const data = await response.json()
      throw new Error(data.detail || 'Error al iniciar sesión')
    }

    await obtenerUsuario()
    router.push('/')
  } catch (e) {
    error.value = e.message
  } finally {
    loading.value = false
  }
}
</script>
  