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
            <div class="h-20 w-20 sm:h-24 sm:w-24 rounded-full overflow-hidden bg-background flex items-center justify-center">
              <img 
                v-if="previewImage" 
                :src="previewImage" 
                class="h-full w-full object-cover" 
                alt="Foto de perfil" 
              />
              <UserCircleIcon 
                v-else 
                class="h-full w-full text-primary" 
                aria-hidden="true" 
              />
            </div>
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
import { ref, onMounted, computed } from 'vue'
import { PhotoIcon, UserCircleIcon } from '@heroicons/vue/24/solid'

const formData = ref({
  username: '',
  email: '',
  first_name: '',
  last_name: '',
  biografia: '',
  foto_perfil: null
})

const previewImage = ref(null)
const originalData = ref(null)
const cargando = ref(true)
const error = ref(null)

onMounted(async () => {
  try {
    cargando.value = true
    const response = await fetch('/api/usuarios/me/', {
      credentials: 'include'
    })
    if (response.ok) {
      const data = await response.json()
      console.log('Datos del usuario recibidos:', data)
      
      formData.value = { ...data }
      
      // Inicializar la imagen de previsualización con la foto de perfil actual
      if (data.foto_perfil) {
        // Asegurarse de que la URL use localhost en lugar de backend
        previewImage.value = data.foto_perfil.replace('backend', 'localhost')
        console.log('URL de imagen inicializada:', previewImage.value)
      }
      
      originalData.value = { ...formData.value }
    }
  } catch (error) {
    console.error('Error al cargar datos del usuario:', error)
  } finally {
    cargando.value = false
  }
})

const handleFileChange = (event) => {
  const file = event.target.files[0]
  if (file) {
    // Revocar URL previa si existe
    if (previewImage.value && previewImage.value.startsWith('blob:')) {
      URL.revokeObjectURL(previewImage.value)
    }
    
    // Crear una URL temporal para previsualizar la imagen
    previewImage.value = URL.createObjectURL(file)
    console.log('URL de previsualización creada:', previewImage.value)
    
    formData.value = {
      ...formData.value,
      _foto_perfil_file: file // Guardamos el archivo separado
    }
  }
}

const handleSubmit = async (event) => {
  event.preventDefault()
  
  try {
    cargando.value = true
    error.value = null
    
    const form = new FormData()
    
    // Agregar todos los campos excepto foto_perfil
    Object.entries(formData.value).forEach(([key, value]) => {
      if (value !== null && value !== undefined && key !== 'foto_perfil' && !key.startsWith('_')) {
        form.append(key, value)
      }
    })

    // Agregar la foto solo si hay un nuevo archivo
    if (formData.value._foto_perfil_file) {
      console.log('Agregando archivo de imagen al formulario:', formData.value._foto_perfil_file.name)
      form.append('foto_perfil', formData.value._foto_perfil_file)
    }

    const csrfToken = document.cookie.split('; ')
      .find(row => row.startsWith('csrftoken='))
      ?.split('=')[1];

    console.log('Enviando formulario al servidor...')
    const response = await fetch('/api/usuarios/me/', {
      method: 'PATCH',
      body: form,
      credentials: 'include',
      headers: {
        'X-CSRFToken': csrfToken || '',
      }
    })

    const data = await response.json()
    console.log('Respuesta del servidor:', data)

    if (!response.ok) {
      // Manejar diferentes tipos de errores
      if (data.username) {
        throw new Error(`Nombre de usuario: ${data.username[0]}`)
      } else if (data.email) {
        throw new Error(`Email: ${data.email[0]}`)
      } else if (data.detail) {
        throw new Error(data.detail)
      } else {
        throw new Error('Error al actualizar el perfil')
      }
    }

    // Actualizar con la respuesta del servidor
    formData.value = { ...data }
    
    // Limpiar la URL temporal si existe
    if (previewImage.value && previewImage.value.startsWith('blob:')) {
      URL.revokeObjectURL(previewImage.value)
    }
    
    // Actualizar la imagen de previsualización con la URL del servidor
    if (data.foto_perfil) {
      previewImage.value = data.foto_perfil.replace('backend', 'localhost')
      console.log('URL de imagen actualizada:', previewImage.value)
    } else {
      previewImage.value = null
    }
    
    // Eliminar el archivo temporal
    if (formData.value._foto_perfil_file) {
      delete formData.value._foto_perfil_file
    }
    
    originalData.value = { ...formData.value }
    
    alert('Perfil actualizado correctamente')
  } catch (error) {
    console.error('Error al actualizar perfil:', error)
    alert(error.message)
  } finally {
    cargando.value = false
  }
}

const resetForm = () => {
  if (originalData.value) {
    formData.value = { ...originalData.value }
    
    // Revocar URL si existe
    if (previewImage.value && previewImage.value.startsWith('blob:')) {
      URL.revokeObjectURL(previewImage.value)
    }
    
    // Restaurar la imagen de previsualización original
    previewImage.value = originalData.value.foto_perfil
  }
}
</script>