export const formatearFecha = (fecha) => {
  if (!fecha) return ''
  
  const date = new Date(fecha)
  
  // Opciones para formatear la fecha
  const opciones = {
    day: '2-digit',
    month: '2-digit',
    year: 'numeric',
    hour: '2-digit',
    minute: '2-digit',
    hour12: true
  }
  
  return date.toLocaleString('es-ES', opciones)
} 