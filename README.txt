// Create base super user
export DJANGO_SUPERUSER_PASSWORD="admin123"
export DJANGO_SUPERUSER_USERNAME="admin"
export DJANGO_SUPERUSER_EMAIL="admin@admin.com"
python3 manage.py createsuperuser --noinput


// Start project
pip install -r requirements.txt
// Change directory to main folder
cd payments
python manage.py runserver