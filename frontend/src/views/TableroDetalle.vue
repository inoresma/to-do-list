<template>
  <div class="min-h-screen bg-background px-4 py-4">
    <div class="max-w-7xl mx-auto">
      <div v-if="tablero" class="space-y-6">
        <!-- Encabezado -->
        <div class="flex justify-between items-center">
          <div class="flex items-center space-x-3">
            <component 
              :is="obtenerIcono(tablero.icono)" 
              class="h-8 w-8"
              :style="{ color: tablero.color }"
            />
            <div>
              <h1 class="text-2xl font-bold text-text">{{ tablero.nombre }}</h1>
              <p class="text-sm text-secondary">{{ tablero.descripcion }}</p>
            </div>
          </div>
          <button 
            @click="mostrarModalTarea = true"
            class="inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md text-white"
            :style="{ backgroundColor: tablero.color }"
          >
            <PlusIcon class="h-5 w-5 mr-2" />
            Nueva Tarea
          </button>
        </div>

        <!-- Columnas de tareas -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-6">
          <!-- Pendientes -->
          <div class="bg-white rounded-lg p-4 shadow-sm">
            <h3 class="font-medium text-text mb-4 flex items-center">
              <span class="w-3 h-3 rounded-full bg-yellow-400 mr-2"></span>
              Pendientes
              <span class="ml-2 text-sm text-secondary">({{ tareasPorEstado.pendiente.length }})</span>
            </h3>
            <draggable
              v-model="tareasPorEstado.pendiente"
              group="tareas"
              item-key="id"
              class="space-y-3 min-h-[50px]"
              @change="(e) => onDragChange(e, 'pendiente')"
            >
              <template #item="{ element: tarea }">
                <div 
                  class="rounded-lg p-3 transition-shadow cursor-move"
                  :class="[prioridadClase(tarea.prioridad)]"
                >
                  <div class="flex justify-between items-start">
                    <div class="flex-1 mr-4">
                      <h4 class="font-medium text-text">{{ tarea.titulo }}</h4>
                      <p class="text-sm text-secondary/80">{{ tarea.descripcion }}</p>
                      <div class="mt-2 flex items-center space-x-2">
                        <span v-if="tarea.fecha_vencimiento" class="text-xs text-secondary/90 bg-white/50 px-2 py-1 rounded-full">
                          {{ formatearFecha(tarea.fecha_vencimiento) }}
                        </span>
                      </div>
                    </div>
                    <div class="flex items-center space-x-2">
                      <button @click="editarTarea(tarea)" class="text-secondary/80 hover:text-primary p-1">
                        <PencilIcon class="h-4 w-4" />
                      </button>
                      <button @click="eliminarTarea(tarea)" class="text-secondary/80 hover:text-red-500 p-1">
                        <TrashIcon class="h-4 w-4" />
                      </button>
                    </div>
                  </div>
                </div>
              </template>
            </draggable>
          </div>

          <!-- En Progreso -->
          <div class="bg-white rounded-lg p-4 shadow-sm">
            <h3 class="font-medium text-text mb-4 flex items-center">
              <span class="w-3 h-3 rounded-full bg-blue-400 mr-2"></span>
              En Progreso
              <span class="ml-2 text-sm text-secondary">({{ tareasPorEstado.en_progreso.length }})</span>
            </h3>
            <draggable
              v-model="tareasPorEstado.en_progreso"
              group="tareas"
              item-key="id"
              class="space-y-3 min-h-[50px]"
              @change="(e) => onDragChange(e, 'en_progreso')"
            >
              <template #item="{ element: tarea }">
                <div 
                  class="rounded-lg p-3 transition-shadow cursor-move"
                  :class="[prioridadClase(tarea.prioridad)]"
                >
                  <div class="flex justify-between items-start">
                    <div class="flex-1 mr-4">
                      <h4 class="font-medium text-text">{{ tarea.titulo }}</h4>
                      <p class="text-sm text-secondary/80">{{ tarea.descripcion }}</p>
                      <div class="mt-2 flex items-center space-x-2">
                        <span v-if="tarea.fecha_vencimiento" class="text-xs text-secondary/90 bg-white/50 px-2 py-1 rounded-full">
                          {{ formatearFecha(tarea.fecha_vencimiento) }}
                        </span>
                      </div>
                    </div>
                    <div class="flex items-center space-x-2">
                      <button @click="editarTarea(tarea)" class="text-secondary/80 hover:text-primary p-1">
                        <PencilIcon class="h-4 w-4" />
                      </button>
                      <button @click="eliminarTarea(tarea)" class="text-secondary/80 hover:text-red-500 p-1">
                        <TrashIcon class="h-4 w-4" />
                      </button>
                    </div>
                  </div>
                </div>
              </template>
            </draggable>
          </div>

          <!-- Completadas -->
          <div class="bg-white rounded-lg p-4 shadow-sm">
            <h3 class="font-medium text-text mb-4 flex items-center">
              <span class="w-3 h-3 rounded-full bg-green-400 mr-2"></span>
              Completadas
              <span class="ml-2 text-sm text-secondary">({{ tareasPorEstado.completada.length }})</span>
            </h3>
            <draggable
              v-model="tareasPorEstado.completada"
              group="tareas"
              item-key="id"
              class="space-y-3 min-h-[50px]"
              @change="(e) => onDragChange(e, 'completada')"
            >
              <template #item="{ element: tarea }">
                <div 
                  class="rounded-lg p-3 transition-shadow cursor-move"
                  :class="[prioridadClase(tarea.prioridad)]"
                >
                  <div class="flex justify-between items-start">
                    <div class="flex-1 mr-4">
                      <h4 class="font-medium text-text" :class="{ 'line-through': tarea.estado === 'completada' }">{{ tarea.titulo }}</h4>
                      <p class="text-sm text-secondary/80">{{ tarea.descripcion }}</p>
                      <div class="mt-2 flex items-center space-x-2">
                        <span v-if="tarea.fecha_vencimiento" class="text-xs text-secondary/90 bg-white/50 px-2 py-1 rounded-full">
                          {{ formatearFecha(tarea.fecha_vencimiento) }}
                        </span>
                      </div>
                    </div>
                    <div class="flex items-center space-x-2">
                      <button @click="editarTarea(tarea)" class="text-secondary/80 hover:text-primary p-1">
                        <PencilIcon class="h-4 w-4" />
                      </button>
                      <button @click="eliminarTarea(tarea)" class="text-secondary/80 hover:text-red-500 p-1">
                        <TrashIcon class="h-4 w-4" />
                      </button>
                    </div>
                  </div>
                </div>
              </template>
            </draggable>
          </div>
        </div>
      </div>
    </div>

    <!-- Modal para crear/editar tarea -->
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
              class="mt-1 block w-full rounded-md border-0 py-1.5 px-3 text-text shadow-sm ring-1 ring-inset ring-secondary/30 placeholder:text-secondary focus:ring-2 focus:ring-inset focus:ring-primary"
            />
          </div>
          
          <div>
            <label for="descripcion" class="block text-sm font-medium text-text">Descripción</label>
            <textarea 
              id="descripcion"
              v-model="formTarea.descripcion"
              rows="3"
              class="mt-1 block w-full rounded-md border-0 py-1.5 px-3 text-text shadow-sm ring-1 ring-inset ring-secondary/30 placeholder:text-secondary focus:ring-2 focus:ring-inset focus:ring-primary"
            ></textarea>
          </div>

          <div class="grid grid-cols-2 gap-4">
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
              <label for="fecha_vencimiento" class="block text-sm font-medium text-text">Fecha de vencimiento</label>
              <input 
                type="datetime-local"
                id="fecha_vencimiento"
                v-model="formTarea.fecha_vencimiento"
                class="mt-1 block w-full rounded-md border-0 py-1.5 px-3 text-text shadow-sm ring-1 ring-inset ring-secondary/30 focus:ring-2 focus:ring-inset focus:ring-primary"
              />
            </div>
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
                :disabled="loading"
                class="px-4 py-2 text-sm font-medium text-white rounded-md disabled:opacity-50"
                :style="{ backgroundColor: tablero?.color }"
              >
                <span v-if="loading">Guardando...</span>
                <span v-else>{{ modoEdicion ? 'Guardar cambios' : 'Crear tarea' }}</span>
              </button>
            </div>
          </form>
        </template>
      </Modal>
    </div>
</template>

<script setup>
import { ref, computed, onMounted } from 'vue'
import { useRoute } from 'vue-router'
import draggable from 'vuedraggable'
import { 
  PlusIcon, PencilIcon, TrashIcon,
  ClipboardDocumentListIcon, CalendarIcon, StarIcon, HeartIcon,
  HomeIcon, BookOpenIcon, BriefcaseIcon, AcademicCapIcon
} from '@heroicons/vue/24/outline'
import Modal from '@/components/common/Modal.vue'

const route = useRoute()
const tablero = ref(null)
const tareas = ref([])
const loading = ref(false)
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
  console.log('Todas las tareas:', tareas.value)
  const result = {
    pendiente: tareas.value.filter(t => t.estado === 'pendiente'),
    en_progreso: tareas.value.filter(t => t.estado === 'en_progreso'),
    completada: tareas.value.filter(t => t.estado === 'completada')
  }
  console.log('Tareas filtradas:', result)
  return result
})

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
    const response = await fetch(`/api/tareas/?tablero=${route.params.id}`, {
      credentials: 'include'
    })
    if (response.ok) {
      const data = await response.json()
      tareas.value = data
      console.log('Tareas obtenidas:', data) // Para depuración
    }
  } catch (error) {
    console.error('Error al obtener tareas:', error)
  }
}

const guardarTarea = async () => {
  try {
    loading.value = true
    const csrfToken = document.cookie.split('; ')
      .find(row => row.startsWith('csrftoken='))
      ?.split('=')[1];

    // Formatear la fecha correctamente si existe
    let fechaVencimiento = null
    if (formTarea.value.fecha_vencimiento) {
      fechaVencimiento = new Date(formTarea.value.fecha_vencimiento)
        .toISOString()
        .slice(0, 16) // Formato YYYY-MM-DDTHH:mm
    }

    const datos = {
      titulo: formTarea.value.titulo,
      descripcion: formTarea.value.descripcion,
      prioridad: formTarea.value.prioridad,
      fecha_vencimiento: fechaVencimiento,
      estado: formTarea.value.estado,
      tablero: Number(route.params.id)
    }
    
    console.log('Enviando datos:', datos)

    const response = await fetch('/api/tareas/', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrfToken || '',
      },
      body: JSON.stringify(datos),
      credentials: 'include'
    })

    const responseText = await response.text()
    console.log('Respuesta del servidor:', responseText)

    let data
    try {
      data = JSON.parse(responseText)
    } catch (e) {
      console.error('Error al parsear respuesta:', responseText)
      throw new Error('Respuesta inválida del servidor')
    }

    if (!response.ok) {
      throw new Error(data.detail || Object.values(data)[0] || 'Error al guardar la tarea')
    }

    await obtenerTareas()
    cerrarModalTarea()
  } catch (error) {
    console.error('Error al guardar tarea:', error)
    alert(error.message)
  } finally {
    loading.value = false
  }
}

const actualizarEstadoTarea = async (tarea, nuevoEstado) => {
  try {
    const csrfToken = document.cookie.split('; ')
      .find(row => row.startsWith('csrftoken='))
      ?.split('=')[1];

    const response = await fetch(`/api/tareas/${tarea.id}/`, {
      method: 'PATCH',
      headers: {
        'Content-Type': 'application/json',
        'X-CSRFToken': csrfToken || '',
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
    baja: 'bg-green-50/80 hover:bg-green-100/80',
    media: 'bg-yellow-50/80 hover:bg-yellow-100/80',
    alta: 'bg-red-50/80 hover:bg-red-100/80'
  }
  return clases[prioridad]
}

const formatearFecha = (fecha) => {
  return new Date(fecha).toLocaleString('es-ES', {
    day: 'numeric',
    month: 'short',
    hour: '2-digit',
    minute: '2-digit'
  })
}

const eliminarTarea = async (tarea) => {
  if (!confirm('¿Estás seguro de que deseas eliminar esta tarea?')) return

  try {
    const csrfToken = document.cookie.split('; ')
      .find(row => row.startsWith('csrftoken='))
      ?.split('=')[1];

    const response = await fetch(`/api/tareas/${tarea.id}/`, {
      method: 'DELETE',
      headers: {
        'X-CSRFToken': csrfToken || '',
      },
      credentials: 'include'
    })

    if (response.ok) {
      await obtenerTareas()
    }
  } catch (error) {
    console.error('Error al eliminar tarea:', error)
  }
}

const onDragChange = async (e, columna) => {
  // Si hay un elemento añadido a esta columna
  if (e.added) {
    const tarea = e.added.element
    if (tarea.estado !== columna) {
      await actualizarEstadoTarea(tarea, columna)
    }
  }
}

onMounted(() => {
  obtenerTablero()
  obtenerTareas()
})
</script> 