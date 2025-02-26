<template>
  <div class="min-h-screen bg-background flex items-center justify-center px-4">
    <div class="max-w-md w-full bg-white rounded-xl shadow-lg p-8">
      <div class="mb-6">
        <router-link 
          to="/"
          class="text-secondary hover:text-primary flex items-center space-x-1"
        >
          <ArrowLeftIcon class="h-5 w-5" />
          <span>Volver al inicio</span>
        </router-link>
      </div>

      <div class="text-center">
        <h1 class="text-2xl font-bold text-primary">ToDoList</h1>
        <h2 class="mt-4 text-xl font-semibold text-text">Iniciar Sesión</h2>
      </div>

      <div class="mt-8">
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

        <p class="mt-8 text-center text-sm text-secondary">
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
import { ArrowLeftIcon } from '@heroicons/vue/24/outline'

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
      throw new Error(data.detail || 'Credenciales incorrectas. El usuario o contraseña no son válidos.')
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
  