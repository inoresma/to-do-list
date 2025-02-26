FROM node:18-alpine

WORKDIR /app/frontend

# Copiar package.json y package-lock.json (o yarn.lock)
COPY frontend/package*.json ./

# Instalar dependencias
RUN npm install

# Copiar el código fuente
COPY frontend/ ./

# Puerto donde corre Vite durante desarrollo
EXPOSE 5173

# Script de inicio
COPY scripts/start-frontend.sh /start-frontend.sh
RUN chmod +x /start-frontend.sh

CMD ["/start-frontend.sh"]