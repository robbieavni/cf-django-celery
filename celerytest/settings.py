"""
Django settings for celerytest project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

#: Only add pickle to this list if your broker is secured
#: from unwanted access (see userguide/security.html)
CELERY_ACCEPT_CONTENT = ['json']
CELERY_TASK_SERIALIZER = 'json'
CELERY_RESULT_SERIALIZER = 'json'

from datetime import timedelta

CELERYBEAT_SCHEDULE = {
    'add-every-10-seconds': {
        'task': 'app.tasks.add_one',
        'schedule': timedelta(seconds=10),
    },
}

CELERY_TIMEZONE = 'UTC'

CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'j9w_bm(+_3_@ah0pp3#%2wd$5!%x7ug4$vti&m^q74=(^77e_$'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []

# Application definition

INSTALLED_APPS = (
    'app',
    'djcelery',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'celerytest.urls'

WSGI_APPLICATION = 'celerytest.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

if 'VCAP_SERVICES' in os.environ:
  import json
  vcap_services = json.loads(os.environ['VCAP_SERVICES'])
  mysql_srv = vcap_services['p-mysql'][0]
  cred = mysql_srv = mysql_srv['credentials']
  DATABASES = {
    'default': {
    'ENGINE': 'django.db.backends.mysql',
    'NAME': cred['name'],
    'USER': cred['username'],
    'PASSWORD': cred['password'],
    'HOST': cred['hostname'],
    'PORT': cred['port'],
  }
}
  rabbit_srv = vcap_services['p-rabbitmq'][0]
  cred_r = rabbit_srv['credentials']
  BROKER_URL = cred_r['uri']

else:
  DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
  BROKER_URL = 'amqp://guest:guest@localhost:5672//'

# Internationalization
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATICFILES_STORAGE = 'whitenoise.django.GzipManifestStaticFilesStorage'
