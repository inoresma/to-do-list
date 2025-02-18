<template>
  <div class="min-h-screen bg-background px-4 py-4 sm:py-8">
    <div class="max-w-3xl mx-auto">
      <!-- Encabezado -->
      <div class="mb-6 sm:mb-8">
        <h1 class="text-xl sm:text-2xl font-bold text-text">Configuración del Perfil</h1>
        <p class="mt-1 text-sm text-secondary">
          Gestiona tu información personal y cómo otros te ven en la plataforma.
        </p>
      </div>

      <form @submit.prevent="handleSubmit" class="space-y-6 bg-white shadow-sm rounded-lg p-4 sm:p-6">
        <!-- Sección de Foto de Perfil -->
        <div class="flex flex-col sm:flex-row items-center gap-4 sm:gap-6">
          <div class="shrink-0">
            <img 
              v-if="formData.foto_perfil" 
              :src="formData.foto_perfil" 
              class="h-20 w-20 sm:h-24 sm:w-24 rounded-full object-cover border-4 border-white shadow-lg" 
              alt="Foto de perfil" 
            />
            <UserCircleIcon 
              v-else 
              class="h-20 w-20 sm:h-24 sm:w-24 text-secondary rounded-full bg-background p-1" 
              aria-hidden="true" 
            />
          </div>
          <div class="w-full sm:w-auto">
            <label class="block">
              <span class="text-sm font-medium text-text">Foto de perfil</span>
              <input 
                type="file" 
                @change="handleFileChange"
                accept="image/*"
                class="mt-1 block w-full text-sm text-secondary
                  file:mr-4 file:py-2 file:px-4
                  file:rounded-full file:border-0
                  file:text-sm file:font-semibold
                  file:bg-primary file:text-white
                  hover:file:bg-accent cursor-pointer"
              />
            </label>
            <p class="mt-1 text-xs text-secondary">PNG, JPG, GIF hasta 10MB</p>
          </div>
        </div>

        <div class="grid grid-cols-1 gap-6 mt-6 sm:mt-8">
          <!-- Información Básica -->
          <div class="border-b border-gray-200 pb-6">
            <h2 class="text-base sm:text-lg font-medium text-gray-900 mb-4">Información Básica</h2>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
              <div class="col-span-1">
                <label for="username" class="block text-sm font-medium text-gray-700">
                  Nombre de usuario
                </label>
                <input 
                  type="text"
                  id="username"
                  v-model="formData.username"
                  class="mt-1 block w-full rounded-md border-gray-300 shadow-sm 
                         focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm
                         px-3 py-2"
                />
              </div>
              <div class="col-span-1">
                <label for="email" class="block text-sm font-medium text-gray-700">
                  Correo electrónico
                </label>
                <input 
                  type="email"
                  id="email"
                  v-model="formData.email"
                  class="mt-1 block w-full rounded-md border-gray-300 shadow-sm 
                         focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm
                         px-3 py-2"
                />
              </div>
            </div>
          </div>

          <!-- Información Personal -->
          <div class="border-b border-gray-200 pb-6">
            <h2 class="text-base sm:text-lg font-medium text-gray-900 mb-4">Información Personal</h2>
            <div class="grid grid-cols-1 sm:grid-cols-2 gap-4">
              <div class="col-span-1">
                <label for="first_name" class="block text-sm font-medium text-gray-700">
                  Nombre
                </label>
                <input 
                  type="text"
                  id="first_name"
                  v-model="formData.first_name"
                  class="mt-1 block w-full rounded-md border-gray-300 shadow-sm 
                         focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm
                         px-3 py-2"
                />
              </div>
              <div class="col-span-1">
                <label for="last_name" class="block text-sm font-medium text-gray-700">
                  Apellido
                </label>
                <input 
                  type="text"
                  id="last_name"
                  v-model="formData.last_name"
                  class="mt-1 block w-full rounded-md border-gray-300 shadow-sm 
                         focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm
                         px-3 py-2"
                />
              </div>
            </div>
          </div>

          <!-- Biografía -->
          <div>
            <label for="biografia" class="block text-sm font-medium text-gray-700">
              Biografía
            </label>
            <textarea
              id="biografia"
              v-model="formData.biografia"
              rows="4"
              class="mt-1 block w-full rounded-md border-gray-300 shadow-sm 
                     focus:border-indigo-500 focus:ring-indigo-500 sm:text-sm
                     px-3 py-2"
              placeholder="Cuéntanos un poco sobre ti..."
            />
            <p class="mt-2 text-sm text-gray-500">
              Breve descripción para tu perfil público.
            </p>
          </div>
        </div>

        <!-- Botones de acción -->
        <div class="flex flex-col-reverse sm:flex-row justify-end gap-3 sm:gap-4 pt-6">
          <button
            type="button"
            @click="resetForm"
            class="w-full sm:w-auto px-4 py-2 text-sm font-medium text-gray-700 
                   bg-white border border-gray-300 rounded-md shadow-sm 
                   hover:bg-gray-50 focus:outline-none focus:ring-2 
                   focus:ring-indigo-500 focus:ring-offset-2"
          >
            Cancelar
          </button>
          <button
            type="submit"
            class="w-full sm:w-auto px-4 py-2 text-sm font-medium text-white 
                   bg-indigo-600 border border-transparent rounded-md shadow-sm 
                   hover:bg-indigo-700 focus:outline-none focus:ring-2 
                   focus:ring-indigo-500 focus:ring-offset-2"
          >
            Guardar cambios
          </button>
        </div>
      </form>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { PhotoIcon, UserCircleIcon } from '@heroicons/vue/24/solid'

const formData = ref({
  username: '',
  email: '',
  first_name: '',
  last_name: '',
  biografia: '',
  foto_perfil: null
})

const originalData = ref(null)

onMounted(async () => {
  try {
    const response = await fetch('/api/usuarios/me/')
    if (response.ok) {
      const data = await response.json()
      formData.value = { ...data }
      originalData.value = { ...data }
    }
  } catch (error) {
    console.error('Error al cargar datos del usuario:', error)
  }
})

const handleFileChange = (event) => {
  const file = event.target.files[0]
  if (file) {
    formData.value.foto_perfil = file
  }
}

const handleSubmit = async (event) => {
  event.preventDefault()
  
  try {
    const form = new FormData()
    for (const [key, value] of Object.entries(formData.value)) {
      if (value !== null && value !== undefined) {
        if (key === 'foto_perfil' && typeof value === 'string') {
          continue
        }
        form.append(key, value)
      }
    }

    const csrfToken = document.cookie.split('; ')
      .find(row => row.startsWith('csrftoken='))
      ?.split('=')[1];

    const response = await fetch('/api/usuarios/me/', {
      method: 'PATCH',
      body: form,
      credentials: 'include',
      headers: {
        'X-CSRFToken': csrfToken || '',
      }
    })

    if (!response.ok) {
      const contentType = response.headers.get('content-type')
      if (contentType && contentType.includes('application/json')) {
        const errorData = await response.json()
        throw new Error(errorData.detail || 'Error al actualizar el perfil')
      } else {
        throw new Error('Error en la respuesta del servidor')
      }
    }

    const data = await response.json()
    formData.value = { ...data }
    originalData.value = { ...data }
    alert('Perfil actualizado correctamente')
  } catch (error) {
    console.error('Error al actualizar perfil:', error)
    alert(error.message || 'Error al actualizar el perfil')
  }
}

const resetForm = () => {
  if (originalData.value) {
    formData.value = { ...originalData.value }
  }
}
</script>