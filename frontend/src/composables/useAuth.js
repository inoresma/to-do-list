import { ref } from 'vue'
import { useAuthStore } from '@/stores/auth'

const usuario = ref(null)
const cargando = ref(true)
const error = ref(null)

export function useAuth() {
  const authStore = useAuthStore()

  const obtenerNotificacionesNoLeidas = async () => {
    try {
      const response = await fetch('/api/notificaciones/no-leidas/', {
        credentials: 'include'
      })
      if (response.ok) {
        const data = await response.json()
        return data.count
      }
      return 0
    } catch (error) {
      console.error('Error al obtener notificaciones:', error)
      return 0
    }
  }

  const obtenerUsuario = async () => {
    try {
      cargando.value = true
      error.value = null
      
      // Simplificar - sólo obtener del servidor para depuración
      const response = await fetch('/api/usuarios/me/', {
        credentials: 'include',
        headers: {
          'Cache-Control': 'no-cache'
        }
      })
      
      if (!response.ok) {
        usuario.value = null
        localStorage.removeItem('usuario')
        throw new Error('No se pudo obtener la información del usuario')
      }
      
      const data = await response.json()
      if (data && data.id) {
        usuario.value = data
        localStorage.setItem('usuario', JSON.stringify(data))
      } else {
        usuario.value = null
        localStorage.removeItem('usuario')
      }
    } catch (e) {
      error.value = e.message
      usuario.value = null
    } finally {
      cargando.value = false
    }
  }

  const login = async (credentials) => {
    try {
      const response = await fetch('/api/login/', {
        method: 'POST',
        headers: {
          'Content-Type': 'application/json',
        },
        body: JSON.stringify(credentials),
        credentials: 'include'
      })
  
      const data = await response.json()
  
      if (!response.ok) {
        throw new Error(data.error || 'Error al iniciar sesión')
      }
  
      await obtenerUsuario()
      return {
        success: true,
        user: usuario.value,
        message: data.message,
        tareas_por_vencer: data.tareas_por_vencer
      }
    } catch (error) {
      console.error('Error en login:', error)
      throw error
    }
  }

  const logout = async () => {
    try {
      const csrfToken = document.cookie.split('; ')
        .find(row => row.startsWith('csrftoken='))
        ?.split('=')[1];

      const response = await fetch('/api/logout/', {
        method: 'POST',
        credentials: 'include',
        headers: {
          'Content-Type': 'application/json',
          'X-CSRFToken': csrfToken || '',
        }
      })
  
      if (response.ok) {
        usuario.value = null
        authStore.usuario = null
        localStorage.removeItem('usuario')
      }
      
      return true
    } catch (error) {
      console.error('Error en logout:', error)
      throw error
    }
  }

  return {
    usuario,
    cargando,
    error,
    obtenerUsuario,
    login,
    logout,
    obtenerNotificacionesNoLeidas
  }
} 