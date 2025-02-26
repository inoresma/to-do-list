﻿# ToDoList - Gestor de Tareas

## Descripción
Sistema de gestión de tareas que permite a los usuarios organizar sus actividades en tableros personalizados, con características como priorización, fechas de vencimiento y notificaciones.

## Características Principales
- Autenticación de usuarios
- Tableros personalizables con iconos y colores
- Sistema de tareas con prioridades y estados
- Notificaciones de vencimiento
- API REST documentada

## Tecnologías
- Backend:
  - Django 5.1
  - Django REST Framework
  - drf-spectacular (Documentación API)
  - Pillow (Manejo de imágenes)
  
- Frontend:
  - Vue.js 3
  - Tailwind CSS
  - Heroicons

## Requisitos
- Python 3.10+
- Node.js 18+
- PostgreSQL 14+


## Instalación

1. Clonar el repositorio:
   ```bash
   git clone https://github.com/inoresma/to-do-list.git
   cd to-do-list
   ```

2. Crear y activar entorno virtual:
   ```bash
   python -m venv env
   source venv/bin/activate # Linux/MacOS
   venv\Scripts\activate # Windows
   ```

3. Construir y levantar los contenedores:
   ```bash
   docker-compose up -d --build
   ```

4. Verificar que los servicios estén funcionando:
   ```bash
   docker-compose ps
   ```

5. Acceder a la aplicación:
   - Frontend: http://localhost:5173
   - API: http://localhost:8000/api/docs
   - Redoc: http://localhost:8000/api/redoc








