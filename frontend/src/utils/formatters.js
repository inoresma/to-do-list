export const formatearFecha = (fecha, formato = 'completo') => {
  if (!fecha) return ''
  
  const date = new Date(fecha)
  
  if (formato === 'corto') {
    return date.toLocaleString('es-ES', {
      day: 'numeric',
      month: 'short',
      hour: '2-digit',
      minute: '2-digit'
    })
  }
  
  // Formato completo por defecto
  return date.toLocaleString('es-ES', {
    day: '2-digit',
    month: '2-digit',
    year: 'numeric',
    hour: '2-digit',
    minute: '2-digit',
    hour12: true
  })
} 