# ToDoList - Gestor de Tareas

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


## Instalación con Docker:
- Clonar el repositorio
```bash
git clone https://github.com/inoresma/to-do-list.git
cd to-do-list
```
- Ejecutar: docker-compose up -d

- Ejecutar migraciones: docker-compose exec backend python manage.py migrate

- Crear superusuario: docker-compose exec backend python manage.py createsuperuser

- Iniciar el frontend: cd frontend && npm install && npm run dev

- Iniciar el backend: docker-compose exec backend python manage.py runserver


## Accesos:
- Frontend: http://localhost:5173
- Backend API: http://localhost:8000/api
- Documentación API: http://localhost:8000/api/docs
- Base de datos PostgreSQL: localhost:5433

## Comandos útiles:
- Ver logs: docker-compose logs -f
- Detener servicios: docker-compose down
- Reiniciar un servicio: docker-compose restart [servicio]