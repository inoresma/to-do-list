#!/bin/bash
set -e

# Para desarrollo
if [ "$NODE_ENV" = "development" ]; then
  npm run dev -- --host
else
  # Para producción
  npm run build
  # Usar un servidor ligero para servir la aplicación compilada
  npm install -g serve
  serve -s dist -l 5173
fi