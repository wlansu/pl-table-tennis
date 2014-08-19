"""Local settings for the table_tennis application."""
# noinspection PyUnresolvedReferences
from table_tennis.settings import *

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*-t&u2*@dg%nxr15)uno%8&=%8cxrw2z9xdk6##*t^0ti_7-$y'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'table_tennis',
        'USER': 'postgres',
        'PASSWORD': 'asdasd',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
