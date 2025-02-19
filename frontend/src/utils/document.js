export const updateDocumentMeta = (title, icon) => {
  // Actualiza el titulo de la pagina
  document.title = title

  // Actualiza el icono de la pagina
  const favicon = document.querySelector('link[rel="icon"]') || document.createElement('link')
  favicon.rel = 'icon'
  favicon.href = `data:image/svg+xml,<svg xmlns=%22http://www.w3.org/2000/svg%22 viewBox=%220 0 100 100%22><text y=%22.9em%22 font-size=%2290%22>${icon}</text></svg>`
  
  if (!document.querySelector('link[rel="icon"]')) {
    document.head.appendChild(favicon)
  }
} 