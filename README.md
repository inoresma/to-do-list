﻿# ToDoList - Gestor de Tareas

## Descripción
Sistema de gestión de tareas que permite a los usuarios organizar sus actividades en tableros personalizados, con características como priorización, fechas de vencimiento y notificaciones.

## Características Principales
- Autenticación de usuarios
- Tableros personalizables con iconos y colores
- Sistema de tareas con prioridades y estados
- Notificaciones de vencimiento
- API REST documentada
- Perfil de usuario con foto personalizable

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
  - Pinia (Gestión de estado)


.[!IMPORTANT]
## Requisitos previos
Antes de comenzar, asegúrate de tener instalado:

- Git (https://git-scm.com/downloads)
- Python 3.10+ (https://www.python.org/downloads/)
- Node.js 18+ y npm (https://nodejs.org/en/download/)
- PostgreSQL 14+ (solo si no usas Docker) (https://www.postgresql.org/download/)
- Docker Desktop (https://www.docker.com/products/docker-desktop/)
- Docker Compose (incluido en Docker Desktop para Windows/Mac)

.[!TIP]
## Instalación con Docker

### 1. Clonar el repositorio:
```bash
git clone https://github.com/inoresma/to-do-list.git
cd to-do-list
```

### 2. Configuración del entorno virtual (recomendado incluso con Docker):

#### En Windows:
```bash
# Crear el entorno virtual
python -m venv venv

# Activar el entorno virtual
venv\Scripts\activate

# Verificar que el entorno está activado (debería mostrar el prefijo (venv))
```

#### En macOS/Linux:
```bash
# Crear el entorno virtual
python3 -m venv venv

# Activar el entorno virtual
source venv/bin/activate

# Verificar que el entorno está activado (debería mostrar el prefijo (venv))
```

### 3. Configurar variables de entorno:
```bash
# Crear archivo .env en la raíz del proyecto
# Puedes copiar desde el ejemplo proporcionado:
cp .env.example .env

# Editar el archivo .env con tu editor preferido:
# Windows:
notepad .env
# macOS/Linux:
nano .env
```

Ejemplo de contenido del archivo `.env`:
```
POSTGRES_USER=postgres
POSTGRES_PASSWORD=postgres
POSTGRES_DB=todolistdb
POSTGRES_HOST=db
POSTGRES_PORT=5432
SECRET_KEY=tu-clave-secreta-personalizada
DEBUG=True
```

### 4. Construir y levantar los contenedores:
```bash
# Asegúrate de que Docker Desktop esté en ejecución
docker-compose up -d --build
```

Este comando:
- Construirá las imágenes necesarias (frontend, backend, base de datos)
- Creará los contenedores
- Iniciará los servicios en modo detached (en segundo plano)




### 5. Verificar que los servicios estén funcionando:
```bash
docker-compose ps
```

Deberías ver tres servicios en estado "Up":
- to-do-list-db-1
- to-do-list-backend-1
- to-do-list-frontend-1

### 6. Comandos útiles para gestionar los contenedores:

#### Para detener los servicios:
```bash
docker-compose down
```

#### Para ver los logs:
```bash
# Ver todos los logs
docker-compose logs

# Ver logs de un servicio específico (ej: backend, db, frontend)
docker-compose logs backend

# Ver logs en tiempo real
docker-compose logs -f
```

#### Para reiniciar los servicios después de cambios:
```bash
docker-compose down
docker-compose up -d
```

#### Para reiniciar solo un servicio:
```bash
docker-compose restart backend
```
### 7. Crear un superusuario (administrador django):
```bash
docker-compose exec backend python manage.py createsuperuser
```
Sigue las instrucciones para crear un nombre de usuario, email y contraseña.



.[!NOTE]
## Acceso a la aplicación
Una vez que los contenedores estén en funcionamiento, puedes acceder a:

- **Aplicación web (Frontend)**: http://localhost:5173
- **API Docs (Swagger UI)**: http://localhost:8000/api/docs
- **API Docs (ReDoc)**: http://localhost:8000/api/redoc
- **Admin de Django**: http://localhost:8000/admin (usa el superusuario creado anteriormente)


