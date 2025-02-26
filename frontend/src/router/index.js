import { createRouter, createWebHistory } from 'vue-router'
import PerfilUsuario from '../components/usuarios/PerfilUsuario.vue'
import Home from '@/views/Home.vue'
import { useAuthStore } from '@/stores/auth'

const updateDocumentMeta = (title, icon) => {
  document.title = title
  const faviconElement = document.querySelector('link[rel="icon"]')
  if (faviconElement) {
    faviconElement.href = `data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>${icon}</text></svg>`
  }
}

const router = createRouter({
  history: createWebHistory(import.meta.env.BASE_URL),
  routes: [
    {
      path: '/',
      name: 'home',
      component: () => import('../views/Home.vue'),
      meta: {
        title: 'ToDoList | Inicio',
        icon: '📋'
      }
    },
    {
      path: '/perfil',
      name: 'perfil',
      component: PerfilUsuario,
      meta: {
        requiresAuth: true,
        title: 'Mi Perfil | ToDoList',
        icon: '👤'
      }
    },
    {
      path: '/login',
      name: 'login',
      component: () => import('../views/Login.vue'),
      meta: {
        title: 'Iniciar Sesión | ToDoList',
        icon: '🔑'
      }
    },
    {
      path: '/registro',
      name: 'registro',
      component: () => import('../views/Register.vue'),
      meta: {
        title: 'Crear Cuenta | ToDoList',
        icon: '✍️'
      }
    },
    {
      path: '/tableros',
      name: 'tableros',
      component: () => import('../views/Tableros.vue'),
      meta: {
        requiresAuth: true,
        title: 'ToDoList | Mis Tableros',
        icon: '📊'
      }
    },
    {
      path: '/tableros/:id',
      name: 'tablero-detalle',
      component: () => import('../views/TableroDetalle.vue'),
      meta: {
        requiresAuth: true,
        title: 'Tablero | ToDoList',
        icon: '📊'
      }
    }
  ]
})

// Antes de navegar a la pagina
router.beforeEach(async (to, from, next) => {
  const authStore = useAuthStore()
  
  try {
    // Si el usuario aún no se ha intentado cargar, obtenerlo
    if (authStore.cargando) {
      await authStore.obtenerUsuario()
    }

    // Actualiza el título y el icono de la pagina
    if (to.meta.title && to.meta.icon) {
      updateDocumentMeta(to.meta.title, to.meta.icon)
    }

    // Actualiza el titulo para el tablero-detalle
    if (to.name === 'tablero-detalle' && to.params.id) {
      try {
        const response = await fetch(`/api/tableros/${to.params.id}/`, {
          credentials: 'include'
        })
        if (response.ok) {
          const tablero = await response.json()
          document.title = `${tablero.nombre} | ToDoList`
        }
      } catch (error) {
        console.error('Error al obtener tablero:', error)
      }
    }

    // Si el usuario está autenticado y trata de acceder a login/registro
    if (authStore.usuario && (to.name === 'login' || to.name === 'registro')) {
      return next('/tableros')
    }

    // Si la ruta requiere autenticación y el usuario no está autenticado
    if (to.meta.requiresAuth && !authStore.usuario) {
      return next({ 
        path: '/login', 
        query: { redirect: to.fullPath }
      })
    }

    next()
  } catch (error) {
    console.error('Error en router.beforeEach:', error)
    next()
  }
})

export default router 