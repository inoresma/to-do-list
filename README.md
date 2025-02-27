# ToDoList Responsivo - Gestor de Tareas

## Capturas de pantalla

![Página de inicio](/screenshots/inicio.png)
*Página de inicio de ToDoList*

![Tableros](/screenshots/tableros.png)
*Vista de tableros personalizados*

![Tableros](/screenshots/tableros_responsive.png)
*Vista de tableros responsive*

![Tareas](/screenshots/tareas.png)
*Gestión de tareas con prioridades*

![Tareas](/screenshots/tareas_responsive.png)
*Gestión de tareas responsive*

![Perfil de usuario](/screenshots/perfil.png)
*Página de perfil de usuario*

## Descripción
Sistema de gestión de tareas que permite a los usuarios organizar sus actividades en tableros personalizados, con características como priorización, fechas de vencimiento y notificaciones, lo que se podria decir que hace especial a este proyecto es que esta hecho responsivamente con TailwindCSS.

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

## Paleta de colores
La aplicación utiliza la siguiente paleta de colores:

| Nombre        | Uso                  | Código Hex | Muestra |
|--------------|----------------------|------------|---------|
| `primary`    | Color principal      | `#3B82F6`  | <span style="display:inline-block;width:20px;height:20px;background:#3B82F6;"></span> |
| `accent`     | Acentos y destacados | `#2563EB`  | <span style="display:inline-block;width:20px;height:20px;background:#2563EB;"></span> |
| `background` | Fondo principal      | `#F9FAFB`  | <span style="display:inline-block;width:20px;height:20px;background:#F9FAFB;border:1px solid #ccc;"></span> |
| `text`       | Texto principal      | `#1F2937`  | <span style="display:inline-block;width:20px;height:20px;background:#1F2937;"></span> |
| `secondary`  | Texto secundario     | `#6B7280`  | <span style="display:inline-block;width:20px;height:20px;background:#6B7280;"></span> |

*Esta paleta está basada en Tailwind CSS*


## Estructura del proyecto

```
to-do-list/
├── backend/                # Servidor Django
│   ├── apps/               # Aplicaciones Django
│   │   ├── tableros_app/   # App para tableros
│   │   ├── tareas_app/     # App para tareas
│   │   └── usuarios_app/   # App para usuarios
│   ├── core/               # Configuración principal de Django
│   └── requirements.txt    # Dependencias de Python
├── frontend/               # Cliente Vue.js
│   ├── public/             # Archivos estáticos públicos
│   ├── src/                # Código fuente Vue
│   │   ├── assets/         # Recursos (CSS, imágenes)
│   │   ├── components/     # Componentes Vue
│   │   ├── composables/    # Hooks personalizados
│   │   ├── router/         # Configuración de rutas
│   │   ├── stores/         # Estados de Pinia
│   │   └── views/          # Páginas principales
│   └── package.json        # Dependencias de Node
└── docker-compose.yml      # Configuración de Docker
```


.[!IMPORTANT]
a
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


### 3. Construir y levantar los contenedores:
```bash
# Asegúrate de que Docker Desktop esté en ejecución
docker-compose up -d --build
```

Este comando:
- Construirá las imágenes necesarias (frontend, backend, base de datos)
- Creará los contenedores
- Iniciará los servicios en modo detached (en segundo plano)




### 4. Verificar que los servicios estén funcionando:
```bash
docker-compose ps
```

Deberías ver tres servicios en estado "Up":
- to-do-list-db-1
- to-do-list-backend-1
- to-do-list-frontend-1

### 5. Comandos útiles para gestionar los contenedores:

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
### 6. Crear un superusuario (administrador django):
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


## Licencia
Este proyecto está licenciado bajo la Licencia MIT - ver el archivo LICENSE para más detalles.
---
Desarrollado por inoresma © 2025
