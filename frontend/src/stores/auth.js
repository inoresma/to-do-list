import { defineStore } from 'pinia'
import { ref } from 'vue'

export const useAuthStore = defineStore('auth', () => {
  const usuario = ref(null)
  const cargando = ref(true)

  const obtenerUsuario = async () => {
    try {
      const response = await fetch('/api/usuarios/me/', {
        credentials: 'include'
      })
      if (response.ok) {
        usuario.value = await response.json()
      } else {
        usuario.value = null
      }
    } catch (error) {
      console.error('Error al obtener usuario:', error)
      usuario.value = null
    } finally {
      cargando.value = false
    }
  }

  const cerrarSesion = async () => {
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
      }
    } catch (error) {
      console.error('Error al cerrar sesión:', error)
    }
  }

  return {
    usuario,
    cargando,
    obtenerUsuario,
    cerrarSesion
  }
}) 