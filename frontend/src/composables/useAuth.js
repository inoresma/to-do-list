import { ref } from 'vue'

const usuario = ref(null)
const cargando = ref(true)
const error = ref(null)

export function useAuth() {
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

  return {
    usuario,
    cargando,
    error,
    obtenerUsuario
  }
} 