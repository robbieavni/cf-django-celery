#!/bin/sh
echo "------ Create database tables ------"
python manage.py migrate --noinput

echo "------ import sample data ------"
python manage.py loaddata sample.json

echo "------ create default admin user ------"
echo "from django.contrib.auth.models import User; User.objects.create_superuser('robbie', 'robbieavni@gmail.com', 'laptop')" | python manage.py shell
