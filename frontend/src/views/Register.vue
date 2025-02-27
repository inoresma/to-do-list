<template>
  <div class="min-h-screen bg-background flex items-center justify-center px-4">
    <div class="max-w-md w-full bg-white rounded-xl shadow-lg p-8">
      <!-- Botón volver atrás -->
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
        <h2 class="mt-4 text-xl font-semibold text-text">Crear Cuenta</h2>
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
            <label for="email" class="block text-sm font-medium text-text">Email</label>
            <div class="mt-2">
              <input 
                v-model="formData.email"
                type="email" 
                name="email" 
                id="email" 
                required
                class="block w-full rounded-md border-0 py-1.5 px-3 text-text shadow-sm ring-1 ring-inset ring-secondary/30 placeholder:text-secondary focus:ring-2 focus:ring-inset focus:ring-primary"
              />
            </div>
          </div>

          <div>
            <label for="password" class="block text-sm font-medium text-text">Contraseña</label>
            <div class="mt-2 relative">
              <input 
                v-model="formData.password"
                :type="showPassword ? 'text' : 'password'" 
                name="password" 
                id="password" 
                required
                @input="checkPasswordRequirements"
                class="block w-full rounded-md border-0 py-1.5 px-3 text-text shadow-sm ring-1 ring-inset ring-secondary/30 placeholder:text-secondary focus:ring-2 focus:ring-inset focus:ring-primary pr-10"
              />
              <button 
                type="button" 
                @click="showPassword = !showPassword" 
                class="absolute inset-y-0 right-0 pr-3 flex items-center"
              >
                <EyeIcon v-if="!showPassword" class="h-5 w-5 text-secondary" />
                <EyeSlashIcon v-else class="h-5 w-5 text-secondary" />
              </button>
            </div>
            
            <!-- Requisitos de contraseña -->
            <div class="mt-2 space-y-1">
              <div class="text-sm font-medium text-text">Requisitos:</div>
              <div class="grid grid-cols-2 gap-2 text-xs">
                <div class="flex items-center gap-1">
                  <CheckCircleIcon v-if="passwordRequirements.length" class="h-4 w-4 text-green-500" />
                  <XCircleIcon v-else class="h-4 w-4 text-red-500" />
                  <span :class="passwordRequirements.length ? 'text-green-500' : 'text-red-500'">
                    Mínimo 8 caracteres
                  </span>
                </div>
                <div class="flex items-center gap-1">
                  <CheckCircleIcon v-if="passwordRequirements.uppercase" class="h-4 w-4 text-green-500" />
                  <XCircleIcon v-else class="h-4 w-4 text-red-500" />
                  <span :class="passwordRequirements.uppercase ? 'text-green-500' : 'text-red-500'">
                    Al menos 1 mayúscula
                  </span>
                </div>
                <div class="flex items-center gap-1">
                  <CheckCircleIcon v-if="passwordRequirements.number" class="h-4 w-4 text-green-500" />
                  <XCircleIcon v-else class="h-4 w-4 text-red-500" />
                  <span :class="passwordRequirements.number ? 'text-green-500' : 'text-red-500'">
                    Al menos 1 número
                  </span>
                </div>
                <div class="flex items-center gap-1">
                  <CheckCircleIcon v-if="passwordRequirements.special" class="h-4 w-4 text-green-500" />
                  <XCircleIcon v-else class="h-4 w-4 text-red-500" />
                  <span :class="passwordRequirements.special ? 'text-green-500' : 'text-red-500'">
                    Al menos 1 símbolo especial
                  </span>
                </div>
              </div>
            </div>
          </div>

          <div>
            <label for="confirmPassword" class="block text-sm font-medium text-text">Confirmar Contraseña</label>
            <div class="mt-2 relative">
              <input 
                v-model="formData.confirmPassword"
                :type="showConfirmPassword ? 'text' : 'password'" 
                name="confirmPassword" 
                id="confirmPassword" 
                required
                class="block w-full rounded-md border-0 py-1.5 px-3 text-text shadow-sm ring-1 ring-inset ring-secondary/30 placeholder:text-secondary focus:ring-2 focus:ring-inset focus:ring-primary pr-10"
              />
              <button 
                type="button" 
                @click="showConfirmPassword = !showConfirmPassword" 
                class="absolute inset-y-0 right-0 pr-3 flex items-center"
              >
                <EyeIcon v-if="!showConfirmPassword" class="h-5 w-5 text-secondary" />
                <EyeSlashIcon v-else class="h-5 w-5 text-secondary" />
              </button>
            </div>
            <div v-if="formData.confirmPassword && formData.password !== formData.confirmPassword" class="mt-1 text-xs text-red-500">
              Las contraseñas no coinciden
            </div>
          </div>

          <div v-if="error" class="text-red-500 text-sm text-center">
            {{ error }}
          </div>

          <div>
            <button 
              type="submit"
              :disabled="loading || !isPasswordValid || !isPasswordMatch"
              class="flex w-full justify-center rounded-md bg-primary px-3 py-1.5 text-sm font-semibold text-white shadow-sm hover:bg-accent focus-visible:outline focus-visible:outline-2 focus-visible:outline-offset-2 focus-visible:outline-primary disabled:opacity-50 disabled:cursor-not-allowed"
            >
              <span v-if="loading">Creando cuenta...</span>
              <span v-else>Crear Cuenta</span>
            </button>
          </div>
        </form>

        <p class="mt-8 text-center text-sm text-secondary">
          ¿Ya tienes una cuenta?
          <router-link to="/login" class="font-semibold text-primary hover:text-accent">
            Inicia sesión aquí
          </router-link>
        </p>
      </div>
    </div>
  </div>
</template>

<script setup>
import { ref, computed } from 'vue'
import { useRouter } from 'vue-router'
import { useAuth } from '@/composables/useAuth'
import { 
  ArrowLeftIcon, 
  EyeIcon, 
  EyeSlashIcon,
  CheckCircleIcon,
  XCircleIcon
} from '@heroicons/vue/24/outline'

const router = useRouter()
const { obtenerUsuario } = useAuth()

const formData = ref({
  username: '',
  email: '',
  password: '',
  confirmPassword: ''
})

const loading = ref(false)
const error = ref(null)
const showPassword = ref(false)
const showConfirmPassword = ref(false)

const passwordRequirements = ref({
  length: false,
  uppercase: false,
  number: false,
  special: false
})

const checkPasswordRequirements = () => {
  const password = formData.value.password
  
  // Verificar longitud mínima
  passwordRequirements.value.length = password.length >= 8
  
  // Verificar al menos una mayúscula
  passwordRequirements.value.uppercase = /[A-Z]/.test(password)
  
  // Verificar al menos un número
  passwordRequirements.value.number = /[0-9]/.test(password)
  
  // Verificar al menos un símbolo especial
  passwordRequirements.value.special = /[!@#$%^&*()_+\-=\[\]{};':"\\|,.<>\/?]/.test(password)
}

const isPasswordValid = computed(() => {
  return passwordRequirements.value.length && 
         passwordRequirements.value.uppercase && 
         passwordRequirements.value.number && 
         passwordRequirements.value.special
})

const isPasswordMatch = computed(() => {
  return !formData.value.confirmPassword || 
         (formData.value.password === formData.value.confirmPassword)
})

const handleSubmit = async () => {
  if (!isPasswordValid.value) {
    error.value = "La contraseña no cumple con los requisitos mínimos"
    return
  }
  
  if (!isPasswordMatch.value) {
    error.value = "Las contraseñas no coinciden"
    return
  }
  
  try {
    loading.value = true
    error.value = null
    
    const csrfToken = document.cookie.split('; ')
      .find(row => row.startsWith('csrftoken='))
      ?.split('=')[1];

    const response = await fetch('/api/usuarios/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrfToken || '',
      },
      body: JSON.stringify({
        username: formData.value.username,
        email: formData.value.email,
        password: formData.value.password
      }),
      credentials: 'include'
    })

    if (!response.ok) {
      const data = await response.json()
      throw new Error(Object.values(data)[0] || 'Error al crear la cuenta')
    }

    // Iniciar sesión automáticamente después del registro
    const loginResponse = await fetch('/api/login/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrfToken || '',
      },
      body: JSON.stringify({
        username: formData.value.username,
        password: formData.value.password
      }),
      credentials: 'include'
    })

    if (!loginResponse.ok) {
      throw new Error('Error al iniciar sesión automáticamente')
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