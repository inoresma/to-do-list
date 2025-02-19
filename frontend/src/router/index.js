import { createRouter, createWebHistory } from 'vue-router'
import PerfilUsuario from '../components/usuarios/PerfilUsuario.vue'
import Home from '@/views/Home.vue'
import { useAuthStore } from '@/stores/auth'
import { updateDocumentMeta } from '@/utils/document'

const routes = [
  {
    path: '/',
    name: 'home',
    component: Home,
    meta: {
      title: 'ToDoList - Organiza tu trabajo',
      icon: '📝'
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
      title: 'Mis Tableros | ToDoList',
      icon: '📋'
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

const router = createRouter({
  history: createWebHistory(),
  routes
})

// Antes de navegar a la pagina
router.beforeEach(async (to, from, next) => {
  const authStore = useAuthStore()
  
  // Actualiza el titulo y el icono de la pagina
  if (to.meta.title && to.meta.icon) {
    updateDocumentMeta(to.meta.title, to.meta.icon)
  }

  // Actualiza el titulo y el icono de la pagina para el tablero-detalle
  if (to.name === 'tablero-detalle' && to.params.id) {
    try {
      const response = await fetch(`/api/tableros/${to.params.id}/`, {
        credentials: 'include'
      })
      if (response.ok) {
        const tablero = await response.json()
        updateDocumentMeta(`${tablero.nombre} | ToDoList`, '📊')
      }
    } catch (error) {
      console.error('Error al obtener tablero:', error)
    }
  }

  // Si el usuario está autenticado y trata de acceder a login/registro
  if (authStore.usuario && (to.name === 'login' || to.name === 'registro')) {
    next('/tableros')
    return
  }

  // Si la ruta requiere autenticación y el usuario no está autenticado
  if (to.meta.requiresAuth && !authStore.usuario) {
    next({ 
      path: '/login', 
      query: { redirect: to.fullPath }
    })
    return
  }

  next()
})

export default router 