#!/bin/bash
set -e

# Esperar a que PostgreSQL esté disponible
until PGPASSWORD=$POSTGRES_PASSWORD psql -h db -U $POSTGRES_USER -d $POSTGRES_DB -c '\q'; do
  echo "PostgreSQL aún no está disponible - esperando..."
  sleep 2
done

echo "PostgreSQL está disponible, continuando..."

# Ejecutar migraciones
python manage.py migrate

# Recopilar archivos estáticos
python manage.py collectstatic --noinput

# Iniciar Gunicorn
gunicorn core.wsgi:application --bind 0.0.0.0:8000