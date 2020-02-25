release: python manage.py migrate
heroku ps:scale web=1
web: gunicorn primo_django.wsgi --log-file -
web: python manage.py runserver 0.0.0.0:$PORT --noreload

