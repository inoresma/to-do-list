<template>
  <div class="min-h-screen bg-background px-4 py-4">
    <div class="max-w-7xl mx-auto">
      <div v-if="tablero" class="space-y-6">
        <!-- Encabezado del tablero -->
        <div class="flex justify-between items-center">
          <div>
            <h1 class="text-2xl font-bold text-text">{{ tablero.nombre }}</h1>
            <p class="text-sm text-secondary">{{ tablero.descripcion }}</p>
          </div>
          <button 
            @click="mostrarModalTarea = true"
            class="inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md text-white bg-primary hover:bg-accent"
          >
            <PlusIcon class="h-5 w-5 mr-2" />
            Nueva Tarea
          </button>
        </div>

        <!-- Lista de tareas -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
          <!-- Columna: Pendientes -->
          <div class="bg-white rounded-lg p-4 shadow-sm">
            <h3 class="font-medium text-text mb-4">Pendientes</h3>
            <div class="space-y-3">
              <div 
                v-for="tarea in tareasPorEstado.pendiente" 
                :key="tarea.id"
                class="bg-background rounded p-3"
              >
                <div class="flex justify-between items-start">
                  <div>
                    <h4 class="font-medium text-text">{{ tarea.titulo }}</h4>
                    <p class="text-sm text-secondary">{{ tarea.descripcion }}</p>
                  </div>
                  <button @click="editarTarea(tarea)" class="text-secondary hover:text-primary">
                    <PencilIcon class="h-4 w-4" />
                  </button>
                </div>
                <div class="mt-2 flex items-center justify-between">
                  <span :class="prioridadClase(tarea.prioridad)" class="text-xs px-2 py-1 rounded-full">
                    {{ tarea.prioridad }}
                  </span>
                  <button 
                    @click="actualizarEstadoTarea(tarea, 'en_progreso')"
                    class="text-xs text-primary hover:text-accent"
                  >
                    Mover a En Progreso →
                  </button>
                </div>
              </div>
            </div>
          </div>

          <!-- Columna: En Progreso -->
          <div class="bg-white rounded-lg p-4 shadow-sm">
            <h3 class="font-medium text-text mb-4">En Progreso</h3>
            <div class="space-y-3">
              <div 
                v-for="tarea in tareasPorEstado.en_progreso" 
                :key="tarea.id"
                class="bg-background rounded p-3"
              >
                <div class="flex justify-between items-start">
                  <div>
                    <h4 class="font-medium text-text">{{ tarea.titulo }}</h4>
                    <p class="text-sm text-secondary">{{ tarea.descripcion }}</p>
                  </div>
                  <button @click="editarTarea(tarea)" class="text-secondary hover:text-primary">
                    <PencilIcon class="h-4 w-4" />
                  </button>
                </div>
                <div class="mt-2 flex items-center justify-between">
                  <span :class="prioridadClase(tarea.prioridad)" class="text-xs px-2 py-1 rounded-full">
                    {{ tarea.prioridad }}
                  </span>
                  <button 
                    @click="actualizarEstadoTarea(tarea, 'completada')"
                    class="text-xs text-primary hover:text-accent"
                  >
                    Mover a Completadas →
                  </button>
                </div>
              </div>
            </div>
          </div>

          <!-- Columna: Completadas -->
          <div class="bg-white rounded-lg p-4 shadow-sm">
            <h3 class="font-medium text-text mb-4">Completadas</h3>
            <div class="space-y-3">
              <div 
                v-for="tarea in tareasPorEstado.completada" 
                :key="tarea.id"
                class="bg-background rounded p-3"
              >
                <div class="flex justify-between items-start">
                  <div>
                    <h4 class="font-medium text-text line-through">{{ tarea.titulo }}</h4>
                    <p class="text-sm text-secondary">{{ tarea.descripcion }}</p>
                  </div>
                  <button @click="editarTarea(tarea)" class="text-secondary hover:text-primary">
                    <PencilIcon class="h-4 w-4" />
                  </button>
                </div>
                <div class="mt-2">
                  <span :class="prioridadClase(tarea.prioridad)" class="text-xs px-2 py-1 rounded-full">
                    {{ tarea.prioridad }}
                  </span>
                </div>
              </div>
            </div>
          </div>
        </div>
      </div>

      <!-- Modal crear/editar tarea -->
      <Modal v-if="mostrarModalTarea" @close="cerrarModalTarea">
        <template #title>
          {{ modoEdicion ? 'Editar Tarea' : 'Nueva Tarea' }}
        </template>
        <template #content>
          <form @submit.prevent="guardarTarea" class="space-y-4">
            <div>
              <label for="titulo" class="block text-sm font-medium text-text">Título</label>
              <input 
                type="text"
                id="titulo"
                v-model="formTarea.titulo"
                required
                class="mt-1 block w-full rounded-md border-0 py-1.5 px-3 text-text shadow-sm ring-1 ring-inset ring-secondary/30 focus:ring-2 focus:ring-inset focus:ring-primary"
              />
            </div>
            
            <div>
              <label for="descripcion" class="block text-sm font-medium text-text">Descripción</label>
              <textarea 
                id="descripcion"
                v-model="formTarea.descripcion"
                rows="3"
                class="mt-1 block w-full rounded-md border-0 py-1.5 px-3 text-text shadow-sm ring-1 ring-inset ring-secondary/30 focus:ring-2 focus:ring-inset focus:ring-primary"
              ></textarea>
            </div>

            <div>
              <label for="prioridad" class="block text-sm font-medium text-text">Prioridad</label>
              <select 
                id="prioridad"
                v-model="formTarea.prioridad"
                class="mt-1 block w-full rounded-md border-0 py-1.5 px-3 text-text shadow-sm ring-1 ring-inset ring-secondary/30 focus:ring-2 focus:ring-inset focus:ring-primary"
              >
                <option value="baja">Baja</option>
                <option value="media">Media</option>
                <option value="alta">Alta</option>
              </select>
            </div>

            <div>
              <label for="fecha_vencimiento" class="block text-sm font-medium text-text">
                Fecha de vencimiento (opcional)
              </label>
              <input 
                type="datetime-local"
                id="fecha_vencimiento"
                v-model="formTarea.fecha_vencimiento"
                class="mt-1 block w-full rounded-md border-0 py-1.5 px-3 text-text shadow-sm ring-1 ring-inset ring-secondary/30 focus:ring-2 focus:ring-inset focus:ring-primary"
              />
            </div>

            <div class="flex justify-end space-x-3">
              <button 
                type="button"
                @click="cerrarModalTarea"
                class="px-4 py-2 text-sm font-medium text-secondary hover:text-text"
              >
                Cancelar
              </button>
              <button 
                type="submit"
                class="px-4 py-2 text-sm font-medium text-white bg-primary hover:bg-accent rounded-md"
              >
                {{ modoEdicion ? 'Guardar cambios' : 'Crear tarea' }}
              </button>
            </div>
          </form>
        </template>
      </Modal>
    </div>
  </div>
</template>

<script setup>
import { ref, onMounted, computed } from 'vue'
import { useRoute } from 'vue-router'
import { PlusIcon, PencilIcon } from '@heroicons/vue/24/outline'
import Modal from '@/components/common/Modal.vue'

const route = useRoute()
const tablero = ref(null)
const tareas = ref([])
const mostrarModalTarea = ref(false)
const modoEdicion = ref(false)
const tareaEditando = ref(null)

const formTarea = ref({
  titulo: '',
  descripcion: '',
  prioridad: 'media',
  fecha_vencimiento: null,
  estado: 'pendiente'
})

const tareasPorEstado = computed(() => {
  return {
    pendiente: tareas.value.filter(t => t.estado === 'pendiente'),
    en_progreso: tareas.value.filter(t => t.estado === 'en_progreso'),
    completada: tareas.value.filter(t => t.estado === 'completada')
  }
})

const obtenerTablero = async () => {
  try {
    const response = await fetch(`/api/tableros/${route.params.id}/`, {
      credentials: 'include'
    })
    if (response.ok) {
      tablero.value = await response.json()
    }
  } catch (error) {
    console.error('Error al obtener tablero:', error)
  }
}

const obtenerTareas = async () => {
  try {
    const response = await fetch(`/api/tableros/${route.params.id}/tareas/`, {
      credentials: 'include'
    })
    if (response.ok) {
      tareas.value = await response.json()
    }
  } catch (error) {
    console.error('Error al obtener tareas:', error)
  }
}

const guardarTarea = async () => {
  try {
    const url = modoEdicion.value 
      ? `/api/tareas/${tareaEditando.value.id}/`
      : '/api/tareas/'
    
    const method = modoEdicion.value ? 'PUT' : 'POST'
    
    const datos = {
      ...formTarea.value,
      tablero: route.params.id
    }
    
    const response = await fetch(url, {
      method,
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(datos),
      credentials: 'include'
    })

    if (response.ok) {
      await obtenerTareas()
      cerrarModalTarea()
    }
  } catch (error) {
    console.error('Error al guardar tarea:', error)
  }
}

const actualizarEstadoTarea = async (tarea, nuevoEstado) => {
  try {
    const response = await fetch(`/api/tareas/${tarea.id}/`, {
      method: 'PATCH',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify({ estado: nuevoEstado }),
      credentials: 'include'
    })

    if (response.ok) {
      await obtenerTareas()
    }
  } catch (error) {
    console.error('Error al actualizar estado:', error)
  }
}

const editarTarea = (tarea) => {
  tareaEditando.value = tarea
  formTarea.value = {
    titulo: tarea.titulo,
    descripcion: tarea.descripcion,
    prioridad: tarea.prioridad,
    fecha_vencimiento: tarea.fecha_vencimiento,
    estado: tarea.estado
  }
  modoEdicion.value = true
  mostrarModalTarea.value = true
}

const cerrarModalTarea = () => {
  mostrarModalTarea.value = false
  modoEdicion.value = false
  tareaEditando.value = null
  formTarea.value = {
    titulo: '',
    descripcion: '',
    prioridad: 'media',
    fecha_vencimiento: null,
    estado: 'pendiente'
  }
}

const prioridadClase = (prioridad) => {
  const clases = {
    baja: 'bg-green-100 text-green-800',
    media: 'bg-yellow-100 text-yellow-800',
    alta: 'bg-red-100 text-red-800'
  }
  return clases[prioridad]
}

onMounted(() => {
  obtenerTablero()
  obtenerTareas()
})
</script> 