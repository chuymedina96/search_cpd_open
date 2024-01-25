web: gunicorn pd_searchv3.wsgi
release: python manage.py migrate
release: python manage.py makemigrations
release: python manage.py migrate --run-syncdb


