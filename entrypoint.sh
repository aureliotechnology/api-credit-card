#!/bin/sh

# Wait for the DB to get up
sleep 10

# Apply database migrations
echo "Apply database migrations"
python manage.py makemigrations
python manage.py migrate

# Create superuser
echo "Creating superuser"
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@admin.com.br', 'admin')" | python manage.py shell

# Start server
echo "Starting server"
exec "$@"
