// Create base super user
export DJANGO_SUPERUSER_PASSWORD="admin123"
export DJANGO_SUPERUSER_USERNAME="admin"
export DJANGO_SUPERUSER_EMAIL="admin@admin.com"
python3 manage.py createsuperuser --noinput
