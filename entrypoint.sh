#!/bin/sh

sleep 10

pip install -r requirements.txt
pip install git+https://github.com/maistodos/python-creditcard.git@main

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

echo "Starting server"
exec "$@"
