#!/bin/sh

# Wait for the DB to get up
sleep 10

# Install dependencies from requirements.txt
pip install -r requirements.txt

# Install python-creditcard library directly from Git repository
pip install git+https://github.com/maistodos/python-creditcard.git@main

# Apply database migrations
echo "Apply database migrations"
python manage.py makemigrations
python manage.py migrate

echo "Creating superuser"
echo "
from django.contrib.auth import get_user_model
User = get_user_model()
if User.objects.filter(is_superuser=True).exists():
    print('Superuser already exists.')
else:
    User.objects.create_superuser('admin', 'admin@admin.com', 'admin')
    print('Superuser created.')
" | python manage.py shell

# Start server
echo "Starting server"
exec "$@"
