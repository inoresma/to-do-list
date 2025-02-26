<template>
  <div class="min-h-screen bg-background px-4 py-4">
    <div class="max-w-7xl mx-auto">
      <!-- Botón de volver a tableros -->
      <button 
        @click="router.push('/tableros')" 
        class="mb-4 inline-flex items-center text-secondary hover:text-primary"
      >
        <ArrowUturnLeftIcon class="h-5 w-5 mr-1" />
        Volver a tableros
      </button>
      
      <!-- Mensaje de error -->
      <div v-if="error" class="bg-red-100 border border-red-400 text-red-700 px-4 py-3 rounded mb-4">
        <p>{{ error }}</p>
        <button @click="recargarDatos" class="underline">Intentar de nuevo</button>
      </div>

      <!-- Estado de carga inicial -->
      <div v-if="cargando" class="text-center py-12">
        <div class="animate-spin h-12 w-12 border-4 border-primary border-t-transparent rounded-full mx-auto"></div>
        <p class="mt-4 text-secondary">Cargando tablero...</p>
      </div>

      <div v-else-if="tablero" class="space-y-6">
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
            @click="abrirModalCrearTarea"
            class="inline-flex items-center px-4 py-2 border border-transparent text-sm font-medium rounded-md text-white"
            :style="{ backgroundColor: tablero.color }"
          >
            <PlusIcon class="h-5 w-5 mr-2" />
            Nueva Tarea
          </button>
        </div>

        <!-- Tablero Kanban -->
        <div class="grid grid-cols-1 md:grid-cols-3 gap-4">
          <!-- Columna: Pendiente -->
          <div class="bg-card rounded-lg shadow p-4">
            <h2 class="font-medium text-text mb-3 flex items-center">
              <span class="w-3 h-3 rounded-full bg-yellow-400 mr-2"></span>
              Pendiente
              <span class="ml-2 text-xs bg-secondary/20 text-secondary rounded-full px-2 py-0.5">
                {{ tareasFiltradasPorEstado.pendiente.length }}
              </span>
            </h2>
            <draggable 
              class="min-h-[200px] space-y-2"
              v-model="tareasFiltradasPorEstado.pendiente" 
              group="tareas"
              item-key="id"
              @change="e => onDragChange(e, 'pendiente')"
            >
              <template #item="{ element }">
                <div 
                  class="p-3 rounded-md shadow-sm cursor-pointer border-l-4 bg-white"
                  :class="[prioridadClase(element.prioridad)]"
                  :style="{ borderLeftColor: tablero.color }"
                  @click="editarTarea(element)"
                >
                  <div class="flex justify-between">
                    <h3 class="font-medium text-text">{{ element.titulo }}</h3>
                    <div class="flex space-x-1">
                      <button @click.stop="editarTarea(element)" class="text-secondary hover:text-primary">
                        <PencilIcon class="h-4 w-4" />
                      </button>
                      <button @click.stop="eliminarTarea(element)" class="text-secondary hover:text-red-500">
                        <TrashIcon class="h-4 w-4" />
                      </button>
                    </div>
                  </div>
                  <p class="text-xs text-secondary truncate mt-1">{{ element.descripcion }}</p>
                  <div class="mt-2 flex justify-between items-center text-xs">
                    <span class="text-secondary">
                      {{ element.fecha_vencimiento ? formatearFecha(element.fecha_vencimiento) : 'Sin fecha' }}
                    </span>
                    <span 
                      class="px-2 py-0.5 rounded-full text-xs"
                      :class="{
                        'bg-green-100 text-green-800': element.prioridad === 'baja',
                        'bg-yellow-100 text-yellow-800': element.prioridad === 'media',
                        'bg-red-100 text-red-800': element.prioridad === 'alta'
                      }"
                    >
                      {{ element.prioridad }}
                    </span>
                  </div>
                </div>
              </template>
            </draggable>
          </div>
          
          <!-- Columna: En Progreso -->
          <div class="bg-card rounded-lg shadow p-4">
            <h2 class="font-medium text-text mb-3 flex items-center">
              <span class="w-3 h-3 rounded-full bg-blue-400 mr-2"></span>
              En Progreso
              <span class="ml-2 text-xs bg-secondary/20 text-secondary rounded-full px-2 py-0.5">
                {{ tareasFiltradasPorEstado.en_progreso.length }}
              </span>
            </h2>
            <draggable 
              class="min-h-[200px] space-y-2"
              v-model="tareasFiltradasPorEstado.en_progreso" 
              group="tareas"
              item-key="id"
              @change="e => onDragChange(e, 'en_progreso')"
            >
              <template #item="{ element }">
                <div 
                  class="p-3 rounded-md shadow-sm cursor-pointer border-l-4 bg-white"
                  :class="[prioridadClase(element.prioridad)]"
                  :style="{ borderLeftColor: tablero.color }"
                  @click="editarTarea(element)"
                >
                  <div class="flex justify-between">
                    <h3 class="font-medium text-text">{{ element.titulo }}</h3>
                    <div class="flex space-x-1">
                      <button @click.stop="editarTarea(element)" class="text-secondary hover:text-primary">
                        <PencilIcon class="h-4 w-4" />
                      </button>
                      <button @click.stop="eliminarTarea(element)" class="text-secondary hover:text-red-500">
                        <TrashIcon class="h-4 w-4" />
                      </button>
                    </div>
                  </div>
                  <p class="text-xs text-secondary truncate mt-1">{{ element.descripcion }}</p>
                  <div class="mt-2 flex justify-between items-center text-xs">
                    <span class="text-secondary">
                      {{ element.fecha_vencimiento ? formatearFecha(element.fecha_vencimiento) : 'Sin fecha' }}
                    </span>
                    <span 
                      class="px-2 py-0.5 rounded-full text-xs"
                      :class="{
                        'bg-green-100 text-green-800': element.prioridad === 'baja',
                        'bg-yellow-100 text-yellow-800': element.prioridad === 'media',
                        'bg-red-100 text-red-800': element.prioridad === 'alta'
                      }"
                    >
                      {{ element.prioridad }}
                    </span>
                  </div>
                </div>
              </template>
            </draggable>
          </div>
          
          <!-- Columna: Completada -->
          <div class="bg-card rounded-lg shadow p-4">
            <h2 class="font-medium text-text mb-3 flex items-center">
              <span class="w-3 h-3 rounded-full bg-green-400 mr-2"></span>
              Completada
              <span class="ml-2 text-xs bg-secondary/20 text-secondary rounded-full px-2 py-0.5">
                {{ tareasFiltradasPorEstado.completada.length }}
              </span>
            </h2>
            <draggable 
              class="min-h-[200px] space-y-2"
              v-model="tareasFiltradasPorEstado.completada" 
              group="tareas"
              item-key="id"
              @change="e => onDragChange(e, 'completada')"
            >
              <template #item="{ element }">
                <div 
                  class="p-3 rounded-md shadow-sm cursor-pointer border-l-4 bg-white"
                  :class="[prioridadClase(element.prioridad)]"
                  :style="{ borderLeftColor: tablero.color }"
                  @click="editarTarea(element)"
                >
                  <div class="flex justify-between">
                    <h3 class="font-medium text-text line-through">{{ element.titulo }}</h3>
                    <div class="flex space-x-1">
                      <button @click.stop="editarTarea(element)" class="text-secondary hover:text-primary">
                        <PencilIcon class="h-4 w-4" />
                      </button>
                      <button @click.stop="eliminarTarea(element)" class="text-secondary hover:text-red-500">
                        <TrashIcon class="h-4 w-4" />
                      </button>
                    </div>
                  </div>
                  <p class="text-xs text-secondary truncate mt-1">{{ element.descripcion }}</p>
                  <div class="mt-2 flex justify-between items-center text-xs">
                    <span class="text-secondary">
                      {{ element.fecha_vencimiento ? formatearFecha(element.fecha_vencimiento) : 'Sin fecha' }}
                    </span>
                    <span 
                      class="px-2 py-0.5 rounded-full text-xs"
                      :class="{
                        'bg-green-100 text-green-800': element.prioridad === 'baja',
                        'bg-yellow-100 text-yellow-800': element.prioridad === 'media',
                        'bg-red-100 text-red-800': element.prioridad === 'alta'
                      }"
                    >
                      {{ element.prioridad }}
                    </span>
                  </div>
                </div>
              </template>
            </draggable>
          </div>
        </div>
      </div>

      <!-- Modal para crear o editar tarea -->
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

            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
              <!-- Solo mostrar selector de estado en modo edición -->
              <div v-if="modoEdicion">
                <label for="estado" class="block text-sm font-medium text-text">Estado</label>
                <select 
                  id="estado" 
                  v-model="formTarea.estado"
                  class="mt-1 block w-full rounded-md border-0 py-1.5 px-3 text-text shadow-sm ring-1 ring-inset ring-secondary/30 focus:ring-2 focus:ring-inset focus:ring-primary"
                >
                  <option value="pendiente">Pendiente</option>
                  <option value="en_progreso">En Progreso</option>
                  <option value="completada">Completada</option>
                </select>
              </div>
              
              <div :class="{ 'md:col-span-2': !modoEdicion }">
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
            </div>

            <div>
              <label for="fecha_vencimiento" class="block text-sm font-medium text-text">
                Fecha de vencimiento 
                <span class="text-secondary text-xs">(opcional)</span>
              </label>
              <input 
                type="datetime-local"
                id="fecha_vencimiento"
                v-model="formTarea.fecha_vencimiento"
                class="mt-1 block w-full rounded-md border-0 py-1.5 px-3 text-text shadow-sm ring-1 ring-inset ring-secondary/30 focus:ring-2 focus:ring-inset focus:ring-primary"
              />
            </div>
            
            <div class="flex justify-end space-x-3 mt-6">
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
                class="px-4 py-2 text-sm font-medium text-white rounded-md"
                :style="{ backgroundColor: tablero?.color || '#4F46E5' }"
              >
                <span v-if="loading">Guardando...</span>
                <span v-else>{{ modoEdicion ? 'Actualizar' : 'Crear' }}</span>
              </button>
            </div>
          </form>
        </template>
      </Modal>
    </div>
  </div>
</template>

<script>
import { ref, computed, onMounted } from 'vue'
import { useRoute, useRouter } from 'vue-router'
import Modal from '@/components/common/Modal.vue'
import { 
  PlusIcon, PencilIcon, TrashIcon, ClipboardDocumentListIcon,
  CalendarIcon, StarIcon, HeartIcon, HomeIcon,
  BookOpenIcon, BriefcaseIcon, AcademicCapIcon,
  ArrowUturnLeftIcon
} from '@heroicons/vue/24/outline'
import draggable from 'vuedraggable'

export default {
  components: {
    Modal,
    draggable,
    PlusIcon, 
    PencilIcon, 
    TrashIcon, 
    ClipboardDocumentListIcon,
    CalendarIcon, 
    StarIcon, 
    HeartIcon, 
    HomeIcon,
    BookOpenIcon, 
    BriefcaseIcon, 
    AcademicCapIcon,
    ArrowUturnLeftIcon
  },
  setup() {
    const route = useRoute();
    const router = useRouter();
    const tableroId = route.params.id;

    const tablero = ref(null);
    const tareas = ref([]);
    const cargando = ref(false);
    const error = ref(null);
    const mostrarModalTarea = ref(false);
    const formTarea = ref({
      titulo: '',
      descripcion: '',
      fecha_vencimiento: '',
      estado: 'pendiente',
      prioridad: 'media'
    });
    const loading = ref(false);
    const modoEdicion = ref(false);
    const tareaEditando = ref(null);

    const iconosDisponibles = [
      { valor: 'clipboard', componente: ClipboardDocumentListIcon },
      { valor: 'calendar', componente: CalendarIcon },
      { valor: 'star', componente: StarIcon },
      { valor: 'heart', componente: HeartIcon },
      { valor: 'home', componente: HomeIcon },
      { valor: 'book', componente: BookOpenIcon },
      { valor: 'briefcase', componente: BriefcaseIcon },
      { valor: 'academic-cap', componente: AcademicCapIcon },
    ];
    
    const obtenerIcono = (nombre) => {
      return iconosDisponibles.find(i => i.valor === nombre)?.componente || ClipboardDocumentListIcon;
    };
    
    const tareasFiltradasPorEstado = computed(() => {
      return {
        pendiente: tareas.value.filter(t => t.estado === 'pendiente'),
        en_progreso: tareas.value.filter(t => t.estado === 'en_progreso'),
        completada: tareas.value.filter(t => t.estado === 'completada')
      };
    });
    
    // Cargar datos del tablero y tareas
    const cargarDatos = async () => {
      cargando.value = true;
      error.value = null;
      
      try {
        // Cargar tablero
        const tableroResponse = await fetch(`/api/tableros/${tableroId}/`, {
          credentials: 'include',
          headers: { 'Cache-Control': 'no-cache' }
        });
        
        if (!tableroResponse.ok) {
          throw new Error(`Error al cargar el tablero (${tableroResponse.status})`);
        }
        
        tablero.value = await tableroResponse.json();
        
        // Cargar tareas
        const tareasResponse = await fetch(`/api/tareas/?tablero=${tableroId}`, {
          credentials: 'include',
          headers: { 'Cache-Control': 'no-cache' }
        });
        
        if (!tareasResponse.ok) {
          throw new Error(`Error al cargar las tareas (${tareasResponse.status})`);
        }
        
        tareas.value = await tareasResponse.json();
      } catch (err) {
        error.value = err.message;
        tareas.value = []; 
      } finally {
        cargando.value = false;
      }
    };
    
    // Botón para recargar datos
    const recargarDatos = () => {
      cargarDatos();
    };
    
    // Abrir modal para crear tarea
    const abrirModalCrearTarea = () => {
      inicializarFormularioTarea();
      mostrarModalTarea.value = true;
    };
    
    // Inicializar formulario
    const inicializarFormularioTarea = () => {
      formTarea.value = {
        titulo: '',
        descripcion: '',
        fecha_vencimiento: '',
        estado: 'pendiente',
        prioridad: 'media'
      };
      modoEdicion.value = false;
      tareaEditando.value = null;
    };
    
    // Editar tarea
    const editarTarea = (tarea) => {
      formTarea.value = { ...tarea };
      modoEdicion.value = true;
      tareaEditando.value = tarea;
      mostrarModalTarea.value = true;
    };
    
    // Guardar tarea (crear o actualizar)
    const guardarTarea = async () => {
      try {
        loading.value = true;
        
        const csrfToken = document.cookie.split('; ')
          .find(row => row.startsWith('csrftoken='))
          ?.split('=')[1];
        
        // Si fecha_vencimiento está vacío, enviar null
        const datos = {
          ...formTarea.value,
          fecha_vencimiento: formTarea.value.fecha_vencimiento || null,
          tablero: tableroId
        };
        
        // Si es creación nueva, siempre estado pendiente
        if (!modoEdicion.value) {
          datos.estado = 'pendiente';
        }
        
        const url = modoEdicion.value 
          ? `/api/tareas/${tareaEditando.value.id}/` 
          : `/api/tareas/`;
        
        const method = modoEdicion.value ? 'PUT' : 'POST';
        
        const response = await fetch(url, {
          method,
          headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken || '',
          },
          body: JSON.stringify(datos),
          credentials: 'include'
        });
        
        if (!response.ok) {
          const errorData = await response.json();
          throw new Error(errorData.detail || 'Error al guardar la tarea');
        }
        
        // Recargar tareas
        const tareasResponse = await fetch(`/api/tareas/?tablero=${tableroId}`, {
          credentials: 'include',
          headers: { 'Cache-Control': 'no-cache' }
        });
        
        if (tareasResponse.ok) {
          tareas.value = await tareasResponse.json();
        }
        
        mostrarModalTarea.value = false;
      } catch (error) {
        alert(error.message);
      } finally {
        loading.value = false;
      }
    };
    
    // Actualizar estado al arrastrar
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
          body: JSON.stringify({
            estado: nuevoEstado
          }),
          credentials: 'include'
        });
        
        if (!response.ok) {
          throw new Error('Error al actualizar estado');
        }
        
        // Actualizar la tarea en el array local
        const index = tareas.value.findIndex(t => t.id === tarea.id);
        if (index !== -1) {
          tareas.value[index].estado = nuevoEstado;
        }
      } catch (error) {
        alert('Error al actualizar el estado de la tarea');
      }
    };
    
    // Eliminar tarea
    const eliminarTarea = async (tarea) => {
      if (!confirm(`¿Estás seguro de eliminar la tarea "${tarea.titulo}"?`)) {
        return;
      }
      
      try {
        const csrfToken = document.cookie.split('; ')
          .find(row => row.startsWith('csrftoken='))
          ?.split('=')[1];
        
        const response = await fetch(`/api/tareas/${tarea.id}/`, {
          method: 'DELETE',
          headers: {
            'Content-Type': 'application/json',
            'X-CSRFToken': csrfToken || '',
          },
          credentials: 'include'
        });

        if (!response.ok) {
          throw new Error(`Error al eliminar tarea (${response.status})`);
        }
        
        // Eliminar tarea del array local
        tareas.value = tareas.value.filter(t => t.id !== tarea.id);
      } catch (error) {
        alert('Error al eliminar la tarea');
      }
    };
    
    // Cerrar modal de tarea
    const cerrarModalTarea = () => {
      mostrarModalTarea.value = false;
      inicializarFormularioTarea();
    };
    
    // Manejar cambio al arrastrar
    const onDragChange = async (e, columna) => {
      if (e.added) {
        const tarea = e.added.element;
        if (tarea.estado !== columna) {
          await actualizarEstadoTarea(tarea, columna);
        }
      }
    };
    
    // Formatear fecha
    const formatearFecha = (fecha) => {
      if (!fecha) return 'Sin fecha';
      return new Date(fecha).toLocaleString('es-ES', {
        day: 'numeric',
        month: 'short',
        hour: '2-digit',
        minute: '2-digit'
      });
    };
    
    // Obtener clase según prioridad
    const prioridadClase = (prioridad) => {
      const clases = {
        baja: 'bg-green-50/80 hover:bg-green-100/80',
        media: 'bg-yellow-50/80 hover:bg-yellow-100/80',
        alta: 'bg-red-50/80 hover:bg-red-100/80'
      };
      return clases[prioridad] || 'bg-white hover:bg-gray-50/80';
    };
    
    onMounted(() => {
      cargarDatos();
    });
    
    return {
      route,
      router,
      tablero,
      tareas,
      cargando,
      error,
      mostrarModalTarea,
      formTarea,
      loading,
      modoEdicion,
      tareaEditando,
      tareasFiltradasPorEstado,
      obtenerIcono,
      cargarDatos,
      recargarDatos,
      abrirModalCrearTarea,
      editarTarea,
      guardarTarea,
      actualizarEstadoTarea,
      eliminarTarea,
      cerrarModalTarea,
      formatearFecha,
      prioridadClase,
      onDragChange
    };
  }
};
</script>