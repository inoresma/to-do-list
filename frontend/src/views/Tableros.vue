<template>
  <div class="min-h-screen bg-background px-4 py-4">
    <div class="max-w-7xl mx-auto">
      <div class="flex justify-between items-center mb-6">
        <h1 class="text-2xl font-bold text-text">Mis Tableros</h1>
        <button 
          @click="mostrarModalCrear = true"
          class="inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md text-white bg-primary hover:bg-accent focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-primary"
        >
          <PlusIcon class="h-5 w-5 mr-2" />
          Crear Tablero
        </button>
      </div>

      <!-- Estado de carga -->
      <div v-if="cargando" class="text-center py-12">
        <div class="animate-spin h-12 w-12 border-4 border-primary border-t-transparent rounded-full mx-auto"></div>
        <p class="mt-4 text-secondary">Cargando tableros...</p>
      </div>

      <!-- Estado vacío -->
      <div v-else-if="!tableros.length" class="text-center py-12">
        <div class="relative">
          <ClipboardDocumentListIcon class="mx-auto h-48 w-48 text-secondary/20" />
          <div class="mt-4">
            <h3 class="text-lg font-medium text-text">No hay tableros</h3>
            <p class="mt-1 text-sm text-secondary">
              Comienza creando tu primer tablero para organizar tus tareas
            </p>
            <button 
              @click="mostrarModalCrear = true"
              class="mt-4 inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md text-white bg-primary hover:bg-accent focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-primary"
            >
              Crear mi primer tablero
            </button>
          </div>
        </div>
      </div>

      <!-- Lista de tableros -->
      <div v-else class="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-4">
        <div 
          v-for="tablero in tableros" 
          :key="tablero.id"
          class="rounded-lg shadow-sm hover:shadow-md transition-shadow relative"
          :style="{ backgroundColor: tablero.color + '10' }"
        >
          <!-- Botones fuera del router-link -->
          <div class="absolute top-4 right-4 flex space-x-2 z-10">
            <button 
              @click="editarTablero(tablero)"
              class="text-secondary hover:text-primary bg-white rounded-full p-1"
            >
              <PencilIcon class="h-5 w-5" />
            </button>
            <button 
              @click="confirmarEliminar(tablero)"
              class="text-secondary hover:text-red-500 bg-white rounded-full p-1"
            >
              <TrashIcon class="h-5 w-5" />
            </button>
          </div>

          <router-link 
            :to="`/tableros/${tablero.id}`"
            class="block p-4"
          >
            <div class="flex items-start space-x-3 pr-20"> <!-- Añadido pr-20 para dar espacio a los botones -->
              <component 
                :is="obtenerIcono(tablero.icono)" 
                class="h-6 w-6"
                :style="{ color: tablero.color }"
              />
              <div>
                <h3 class="text-lg font-medium text-text">{{ tablero.nombre }}</h3>
                <p class="mt-1 text-sm text-secondary">{{ tablero.descripcion }}</p>
              </div>
            </div>
            <div class="mt-4 flex justify-between items-center">
              <span class="text-xs text-secondary">
                {{ tablero.tareas_count }} tareas
              </span>
              <span class="text-primary hover:text-accent text-sm font-medium">
                Ver tablero →
              </span>
            </div>
          </router-link>
        </div>
      </div>

      <!-- Modal crear/editar tablero -->
      <Modal v-if="mostrarModalCrear" @close="cerrarModal">
        <template #title>
          {{ modoEdicion ? 'Editar Tablero' : 'Crear Nuevo Tablero' }}
        </template>
        <template #content>
          <form @submit.prevent="guardarTablero" class="space-y-4">
            <div>
              <label for="nombre" class="block text-sm font-medium text-text">Nombre</label>
              <input 
                type="text"
                id="nombre"
                v-model="formTablero.nombre"
                required
                class="mt-1 block w-full rounded-md border-0 py-1.5 px-3 text-text shadow-sm ring-1 ring-inset ring-secondary/30 placeholder:text-secondary focus:ring-2 focus:ring-inset focus:ring-primary"
              />
            </div>
            <div>
              <label for="descripcion" class="block text-sm font-medium text-text">Descripción</label>
              <textarea 
                id="descripcion"
                v-model="formTablero.descripcion"
                rows="3"
                class="mt-1 block w-full rounded-md border-0 py-1.5 px-3 text-text shadow-sm ring-1 ring-inset ring-secondary/30 placeholder:text-secondary focus:ring-2 focus:ring-inset focus:ring-primary"
              ></textarea>
            </div>
            <div>
              <label class="block text-sm font-medium text-text">Color del tablero</label>
              <div class="mt-2 flex items-center space-x-2">
                <input 
                  type="color"
                  v-model="formTablero.color"
                  class="h-8 w-8 rounded cursor-pointer"
                />
                <span class="text-sm text-secondary">{{ formTablero.color }}</span>
              </div>
            </div>
            <div>
              <label class="block text-sm font-medium text-text">Icono</label>
              <div class="mt-2 grid grid-cols-4 gap-2">
                <button
                  v-for="icono in iconosDisponibles"
                  :key="icono.valor"
                  type="button"
                  class="p-2 rounded-lg border-2 flex items-center justify-center"
                  :class="formTablero.icono === icono.valor ? 'border-primary' : 'border-transparent'"
                  @click="formTablero.icono = icono.valor"
                >
                  <component :is="obtenerIcono(icono.valor)" class="h-6 w-6" />
                </button>
              </div>
            </div>
            <div class="flex justify-end space-x-3">
              <button 
                type="button"
                @click="cerrarModal"
                class="px-4 py-2 text-sm font-medium text-secondary hover:text-text"
              >
                Cancelar
              </button>
              <button 
                type="submit"
                :disabled="loading"
                class="px-4 py-2 text-sm font-medium text-white bg-primary hover:bg-accent rounded-md disabled:opacity-50"
              >
                <span v-if="loading">Guardando...</span>
                <span v-else>{{ modoEdicion ? 'Guardar cambios' : 'Crear tablero' }}</span>
              </button>
            </div>
            <p v-if="error" class="text-red-500 text-sm text-center">{{ error }}</p>
          </form>
        </template>
      </Modal>

      <!-- Modal de confirmación para eliminar -->
      <Modal v-if="mostrarModalEliminar" @close="cerrarModalEliminar">
        <template #title>
          Eliminar Tablero
        </template>
        <template #content>
          <div class="space-y-4">
            <p class="text-text">
              ¿Estás seguro de que deseas eliminar el tablero "{{ tableroEliminar?.nombre }}"?
            </p>
            <p class="text-sm text-secondary">
              Esta acción eliminará todas las tareas asociadas y no se puede deshacer.
            </p>
            <div class="flex justify-end space-x-3 mt-6">
              <button 
                @click="cerrarModalEliminar"
                class="px-4 py-2 text-sm font-medium text-secondary hover:text-text"
              >
                Cancelar
              </button>
              <button 
                @click="eliminarTablero"
                :disabled="loadingEliminar"
                class="px-4 py-2 text-sm font-medium text-white bg-red-500 hover:bg-red-600 rounded-md disabled:opacity-50"
              >
                <span v-if="loadingEliminar">Eliminando...</span>
                <span v-else>Eliminar tablero</span>
              </button>
            </div>
          </div>
        </template>
      </Modal>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted } from 'vue'
import { useRouter } from 'vue-router'
import { 
  PlusIcon, ClipboardDocumentListIcon, PencilIcon,
  TrashIcon,
  CalendarIcon, StarIcon, HeartIcon, HomeIcon,
  BookOpenIcon, BriefcaseIcon, AcademicCapIcon
} from '@heroicons/vue/24/outline'
import Modal from '@/components/common/Modal.vue'

const tableros = ref([])
const mostrarModalCrear = ref(false)
const modoEdicion = ref(false)
const tableroEditando = ref(null)
const formTablero = ref({
  nombre: '',
  descripcion: '',
  color: '#4F46E5',
  icono: 'clipboard'
})
const loading = ref(false)
const error = ref(null)
const cargando = ref(true)

const mostrarModalEliminar = ref(false)
const tableroEliminar = ref(null)
const loadingEliminar = ref(false)

const router = useRouter()

const iconosDisponibles = [
  { valor: 'clipboard', componente: ClipboardDocumentListIcon },
  { valor: 'calendar', componente: CalendarIcon },
  { valor: 'star', componente: StarIcon },
  { valor: 'heart', componente: HeartIcon },
  { valor: 'home', componente: HomeIcon },
  { valor: 'book', componente: BookOpenIcon },
  { valor: 'briefcase', componente: BriefcaseIcon },
  { valor: 'academic-cap', componente: AcademicCapIcon },
]

const obtenerIcono = (nombre) => {
  return iconosDisponibles.find(i => i.valor === nombre)?.componente || ClipboardDocumentListIcon
}

const obtenerTableros = async () => {
  try {
    cargando.value = true
    
    const response = await fetch('/api/tableros/', {
      credentials: 'include',
      headers: {
        'Cache-Control': 'no-cache'
      }
    })
    
    if (!response.ok) {
      throw new Error('Error al obtener tableros')
    }
    
    const data = await response.json()
    tableros.value = data
    
    if (data) {
      localStorage.setItem('tableros_cache', JSON.stringify(data))
    }
  } catch (e) {
    console.error('Error:', e)
    error.value = e.message
    tableros.value = []
  } finally {
    cargando.value = false
  }
}

const guardarTablero = async () => {
  try {
    loading.value = true
    error.value = null
    
    const csrfToken = document.cookie.split('; ')
      .find(row => row.startsWith('csrftoken='))
      ?.split('=')[1];

    const url = modoEdicion.value 
      ? `/api/tableros/${tableroEditando.value.id}/`
      : '/api/tableros/'
    
    const method = modoEdicion.value ? 'PUT' : 'POST'
    
    const response = await fetch(url, {
      method,
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrfToken || '',
      },
      body: JSON.stringify(formTablero.value),
      credentials: 'include'
    })

    const data = await response.json()

    if (!response.ok) {
      throw new Error(data.detail || Object.values(data)[0] || 'Error al guardar el tablero')
    }

    await obtenerTableros()
    cerrarModal()
  } catch (e) {
    error.value = e.message
    console.error('Error al guardar tablero:', e)
  } finally {
    loading.value = false
  }
}

const editarTablero = (tablero) => {
  tableroEditando.value = tablero
  formTablero.value = {
    nombre: tablero.nombre,
    descripcion: tablero.descripcion,
    color: tablero.color,
    icono: tablero.icono
  }
  modoEdicion.value = true
  mostrarModalCrear.value = true
}

const cerrarModal = () => {
  mostrarModalCrear.value = false
  modoEdicion.value = false
  tableroEditando.value = null
  formTablero.value = {
    nombre: '',
    descripcion: '',
    color: '#4F46E5',
    icono: 'clipboard'
  }
}

const confirmarEliminar = (tablero) => {
  tableroEliminar.value = tablero
  mostrarModalEliminar.value = true
}

const cerrarModalEliminar = () => {
  mostrarModalEliminar.value = false
  tableroEliminar.value = null
}

const eliminarTablero = async () => {
  try {
    loadingEliminar.value = true
    
    const csrfToken = document.cookie.split('; ')
      .find(row => row.startsWith('csrftoken='))
      ?.split('=')[1];

    const response = await fetch(`/api/tableros/${tableroEliminar.value.id}/`, {
      method: 'DELETE',
      headers: {
        'X-CSRFToken': csrfToken || '',
      },
      credentials: 'include'
    })

    if (!response.ok) {
      throw new Error('Error al eliminar el tablero')
    }

    await obtenerTableros()
    cerrarModalEliminar()
  } catch (error) {
    console.error('Error:', error)
  } finally {
    loadingEliminar.value = false
  }
}

onMounted(async () => {
  try {
    const cachedTableros = localStorage.getItem('tableros_cache')
    if (cachedTableros) {
      try {
        const parsed = JSON.parse(cachedTableros)
        if (parsed && Array.isArray(parsed)) {
          tableros.value = parsed
        }
      } catch (e) {
        console.error('Error al parsear caché:', e)
        localStorage.removeItem('tableros_cache')
      }
    }
    
    await obtenerTableros()
  } catch (e) {
    console.error('Error en onMounted:', e)
    cargando.value = false
  }
})
</script> 