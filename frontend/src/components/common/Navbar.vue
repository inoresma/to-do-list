<template>
  <nav v-if="!['login', 'registro'].includes($route.name)" class="bg-white border-b border-secondary/10">
    <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
      <div class="flex justify-between h-16">
        <div class="flex">
          <div class="flex-shrink-0 flex items-center">
            <router-link to="/" class="text-xl font-bold text-primary">ToDoList</router-link>
          </div>
          <div class="hidden sm:ml-6 sm:flex sm:space-x-8">
            <router-link 
              v-if="usuario"
              to="/tableros" 
              class="text-text hover:text-primary border-transparent hover:border-primary inline-flex items-center px-1 pt-1 border-b-2 text-sm font-medium"
              :class="{ 'border-primary text-primary': $route.path === '/tareas' }"
            >
              Tableros
            </router-link>
          </div>
        </div>
        <div class="hidden sm:ml-6 sm:flex sm:items-center space-x-4">
          <div v-if="cargando" class="animate-pulse">
            <div class="h-8 w-8 bg-secondary/20 rounded-full"></div>
          </div>

          <template v-else-if="usuario">
            <div class="relative">
              <button 
                @click="mostrarNotificaciones = !mostrarNotificaciones"
                class="p-2 text-secondary hover:text-primary rounded-full hover:bg-background focus:outline-none focus:ring-2 focus:ring-primary relative"
              >
                <span class="sr-only">Ver notificaciones</span>
                <BellIcon class="h-6 w-6" aria-hidden="true" />
                <span 
                  v-if="notificacionesNoLeidas > 0"
                  class="absolute top-0 right-0 -mt-1 -mr-1 h-4 w-4 rounded-full bg-accent text-xs text-white flex items-center justify-center"
                >
                  {{ notificacionesNoLeidas }}
                </span>
              </button>

              <div 
                v-if="mostrarNotificaciones"
                class="absolute right-0 mt-2 w-80 bg-white rounded-lg shadow-lg py-1 z-50 max-h-96 overflow-y-auto"
              >
                <div v-if="cargandoNotificaciones" class="p-4 text-center">
                  <div class="animate-spin h-5 w-5 border-2 border-primary border-t-transparent rounded-full mx-auto"></div>
                </div>
                
                <div v-else-if="notificaciones.length === 0" class="p-4 text-center text-secondary">
                  No hay notificaciones
                </div>
                
                <template v-else>
                  <div 
                    v-for="notificacion in notificaciones" 
                    :key="notificacion.id"
                    @click="manejarClickNotificacion(notificacion)"
                    class="p-4 hover:bg-gray-50 cursor-pointer"
                  >
                    <div class="flex items-start space-x-3">
                      <div class="flex-shrink-0">
                        <CheckCircleIcon v-if="notificacion.tipo === 'tarea_completada'" class="h-6 w-6 text-green-500" />
                        <ClockIcon v-else-if="notificacion.tipo === 'fecha_vencimiento'" class="h-6 w-6 text-yellow-500" />
                        <ExclamationCircleIcon v-else-if="notificacion.tipo === 'tarea_vencida'" class="h-6 w-6 text-red-500" />
                        <ChatBubbleLeftIcon v-else-if="notificacion.tipo === 'comentario_nuevo'" class="h-6 w-6 text-blue-500" />
                        <DocumentIcon v-else class="h-6 w-6 text-primary" />
                      </div>
                      
                      <div class="flex-1 min-w-0">
                        <p class="text-sm font-medium text-text">
                          {{ notificacion.mensaje }}
                        </p>
                        <p v-if="notificacion.tarea?.tablero_info" class="text-xs text-primary mt-1">
                          {{ notificacion.tarea.tablero_info.nombre }}
                        </p>
                        <p class="text-xs text-secondary mt-1">
                          {{ formatearFecha(notificacion.fecha_creacion) }}
                        </p>
                      </div>
                    </div>
                  </div>
                </template>
              </div>
            </div>

            <div class="relative">
              <router-link 
                to="/perfil" 
                class="flex items-center space-x-2 text-sm focus:outline-none focus:ring-2 focus:ring-primary focus:ring-offset-2 rounded-full p-1"
                :class="{ 'bg-background': $route.path === '/perfil' }"
              >
                <div class="h-8 w-8 rounded-full overflow-hidden bg-background flex items-center justify-center">
                  <img
                    v-if="usuario.foto_perfil"
                    :src="procesarUrlImagen(usuario.foto_perfil)"
                    class="h-full w-full object-cover"
                    :alt="`Foto de perfil de ${usuario.username}`"
                    @error="handleImageError"
                  />
                  <UserCircleIcon 
                    v-else
                    class="h-8 w-8 text-primary"
                    aria-hidden="true"
                  />
                </div>
                <span class="text-text font-medium">{{ usuario.first_name || usuario.username }}</span>
              </router-link>
            </div>

            <!-- Botón de cerrar sesión -->
            <button 
              @click="cerrarSesion"
              class="p-2 text-secondary hover:text-red-500 rounded-full hover:bg-red-50 focus:outline-none focus:ring-2 focus:ring-red-500 focus:ring-offset-2 transition-colors duration-200"
              title="Cerrar sesión"
            >
              <ArrowRightOnRectangleIcon class="h-5 w-5" aria-hidden="true" />
              <span class="sr-only">Cerrar sesión</span>
            </button>
          </template>

          <router-link 
            v-else
            to="/login" 
            class="inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md text-white bg-primary hover:bg-accent focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-primary"
          >
            Iniciar Sesión
          </router-link>
        </div>
      </div>
    </div>
  </nav>
</template>

<script setup>
import { onMounted, ref, watch } from 'vue'
import { 
  BellIcon, 
  UserCircleIcon,
  CheckCircleIcon,
  ClockIcon,
  ChatBubbleLeftIcon,
  DocumentIcon,
  ArrowRightOnRectangleIcon,
  ExclamationCircleIcon
} from '@heroicons/vue/24/outline'
import { useAuth } from '@/composables/useAuth'
import { useRouter } from 'vue-router'
import { formatearFecha } from '@/utils/formatters'
import { useAuthStore } from '@/stores/auth'

const { usuario, cargando, error, obtenerUsuario, obtenerNotificacionesNoLeidas, logout } = useAuth()
const authStore = useAuthStore()
const notificacionesNoLeidas = ref(0)
const notificaciones = ref([])
const cargandoNotificaciones = ref(false)
const mostrarNotificaciones = ref(false)
const router = useRouter()

// Función para procesar URLs de imágenes
const procesarUrlImagen = (url) => {
  if (!url) return null
  
  // Reemplazar 'backend' por 'localhost' si está presente
  if (url.includes('backend')) {
    url = url.replace('backend', 'localhost')
  }
  
  try {
    // Verificar si la URL es válida
    new URL(url)
    return url
  } catch (e) {
    // Si no es una URL válida, construirla
    return `${window.location.origin}/media/${url}`
  }
}

const obtenerNotificaciones = async () => {
  try {
    cargandoNotificaciones.value = true
    const response = await fetch('/api/notificaciones/', {
      credentials: 'include'
    })
    if (response.ok) {
      const data = await response.json()
      notificaciones.value = data
    }
  } catch (error) {
    console.error('Error al obtener notificaciones:', error)
  } finally {
    cargandoNotificaciones.value = false
  }
}

const manejarClickNotificacion = async (notificacion) => {
  try {
    // Marcar como leída la notificación
    const response = await fetch(`/api/notificaciones/${notificacion.id}/marcar-leida/`, {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': document.cookie.split('; ')
          .find(row => row.startsWith('csrftoken='))
          ?.split('=')[1] || '',
      },
      credentials: 'include'
    })

    if (!response.ok) {
      throw new Error('Error al marcar la notificación como leída')
    }

    // Actualizar contador de notificaciones
    await obtenerNotificacionesNoLeidas()
    
    // Cerrar el menú de notificaciones
    mostrarNotificaciones.value = false

    // Redirigir al tablero correspondiente
    if (notificacion.tarea && notificacion.tarea.tablero) {
      await router.push(`/tableros/${notificacion.tarea.tablero}`)
    }
  } catch (error) {
    console.error('Error:', error)
  }
}

const cerrarSesion = async () => {
  try {
    await logout()
    // Forzar una recarga completa para reiniciar el estado
    window.location.href = '/'
  } catch (error) {
    console.error('Error al cerrar sesión:', error)
    alert('Error al cerrar sesión')
  }
}

const handleImageError = () => {
  // Handle image loading error
  console.error('Error al cargar la imagen del perfil')
}

onMounted(async () => {
  await obtenerUsuario()
  if (usuario.value) {
    notificacionesNoLeidas.value = await obtenerNotificacionesNoLeidas()
  }
})

watch(() => router.currentRoute.value.path, async () => {
  if (usuario.value) {
    notificacionesNoLeidas.value = await obtenerNotificacionesNoLeidas()
  }
})

watch(mostrarNotificaciones, async (nuevo) => {
  if (nuevo && usuario.value) {
    await obtenerNotificaciones()
  }
})
</script>