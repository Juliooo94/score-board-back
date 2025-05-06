#!/bin/sh

# Exit immediately if a command exits with a non-zero status
set -e

# Wait for PostgreSQL to be ready
echo "Waiting for PostgreSQL..."
while ! nc -z $DB_HOST $DB_PORT; do
  sleep 1
done
echo "PostgreSQL is up."

# Run migrations
echo "Applying migrations..."
python manage.py migrate

# Collect static files (optional if you're serving them)
# python manage.py collectstatic --noinput

# Start the app
echo "Starting server..."
exec "$@"
