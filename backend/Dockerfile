FROM python:3.11-slim

WORKDIR /app/backend

# Instalar dependencias del sistema necesarias
RUN apt-get update && apt-get install -y \
    gcc \
    postgresql-client \
    libpq-dev \
    && rm -rf /var/lib/apt/lists/*

# Copiar requirements.txt primero para aprovechar la caché de Docker
COPY backend/requirements.txt .

# Instalar dependencias Python
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el código del proyecto
COPY backend/ .

# Script de inicio
COPY scripts/start-backend.sh /start-backend.sh
RUN chmod +x /start-backend.sh

# Puerto en el que corre el servidor Django
EXPOSE 8000

CMD ["/start-backend.sh"]