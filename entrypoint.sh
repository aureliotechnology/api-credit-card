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

# Create superuser
echo "Creating superuser"
echo "from django.contrib.auth import get_user_model; User = get_user_model(); User.objects.create_superuser('admin', 'admin@admin.com.br', 'admin')" | python manage.py shell


# Start server
echo "Starting server"
exec "$@"
