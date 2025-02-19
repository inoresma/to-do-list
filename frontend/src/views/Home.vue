<template>
  <div class="min-h-screen bg-background">
    <div class="max-w-7xl mx-auto px-4 py-16">
      <!-- Hero Section -->
      <div class="text-center space-y-6 mb-16">
        <h1 class="text-5xl font-bold tracking-tight text-text">
          Organiza tu trabajo de manera eficiente
        </h1>
        <p class="text-xl text-secondary max-w-2xl mx-auto">
          Gestiona tus tareas, proyectos y objetivos en un solo lugar. Simple, flexible y poderoso.
        </p>
        <div class="flex justify-center space-x-4">
          <template v-if="usuario">
            <router-link 
              to="/tableros" 
              class="px-6 py-3 bg-primary text-white rounded-lg font-medium hover:bg-primary/90 transition-colors"
            >
              Ir a mis tableros
            </router-link>
          </template>
          <template v-else>
            <router-link 
              to="/login?redirect=/tableros" 
              class="px-6 py-3 bg-primary text-white rounded-lg font-medium hover:bg-primary/90 transition-colors"
            >
              Iniciar Sesión
            </router-link>
            <router-link 
              to="/registro" 
              class="px-6 py-3 border border-primary text-primary rounded-lg font-medium hover:bg-primary/10 transition-colors"
            >
              Registrarse
            </router-link>
          </template>
        </div>
      </div>

      <!-- Features Section -->
      <div class="grid md:grid-cols-3 gap-8">
        <div class="bg-white rounded-lg p-6 shadow-sm hover:shadow-md transition-all">
          <CheckCircleIcon class="h-12 w-12 mb-4 text-primary" />
          <h3 class="text-xl font-semibold mb-2 text-text">Organización Simple</h3>
          <p class="text-secondary">
            Crea tableros personalizados y organiza tus tareas por estado: pendientes, en progreso y completadas.
          </p>
        </div>

        <div class="bg-white rounded-lg p-6 shadow-sm hover:shadow-md transition-all">
          <ArrowPathIcon class="h-12 w-12 mb-4 text-primary" />
          <h3 class="text-xl font-semibold mb-2 text-text">Flujo de Trabajo</h3>
          <p class="text-secondary">
            Arrastra y suelta tareas entre columnas para actualizar su estado de manera intuitiva.
          </p>
        </div>

        <div class="bg-white rounded-lg p-6 shadow-sm hover:shadow-md transition-all">
          <ClockIcon class="h-12 w-12 mb-4 text-primary" />
          <h3 class="text-xl font-semibold mb-2 text-text">Seguimiento de Tiempo</h3>
          <p class="text-secondary">
            Establece fechas de vencimiento y prioridades para mantener tus proyectos en tiempo.
          </p>
        </div>
      </div>
    </div>
  </div>
</template>

<script setup>
import { 
  CheckCircleIcon,
  ArrowPathIcon,
  ClockIcon
} from '@heroicons/vue/24/outline'
import { useAuthStore } from '@/stores/auth'
import { storeToRefs } from 'pinia'
import { onMounted } from 'vue'

const authStore = useAuthStore()
const { usuario } = storeToRefs(authStore)

onMounted(async () => {
  await authStore.obtenerUsuario()
})
</script> 