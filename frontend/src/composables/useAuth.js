import { ref } from 'vue'

const usuario = ref(null)
const cargando = ref(true)
const error = ref(null)

export function useAuth() {
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
      const response = await fetch('/api/usuarios/me/', {
        credentials: 'include'
      })
      if (!response.ok) throw new Error('No se pudo obtener la información del usuario')
      usuario.value = await response.json()
    } catch (e) {
      error.value = e.message
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

  return {
    usuario,
    cargando,
    error,
    obtenerUsuario,
    login,
    obtenerNotificacionesNoLeidas
  }
} 