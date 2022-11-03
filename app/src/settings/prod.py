from dotenv import load_dotenv

from .base import *

load_dotenv()

DEBUG = os.environ.get('DEBUG')

SITE_ID = 1

ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS').split(' ')

SECRET_KEY = os.getenv('SECRET_KEY')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': os.environ.get('DB_NAME'),
        'USER': os.environ.get('POSTGRES_USER'),
        'PASSWORD': os.environ.get('POSTGRES_PASSWORD'),
        'HOST': os.environ.get('DB_HOST'),
        'PORT': os.environ.get('DB_PORT'),
    }
}
