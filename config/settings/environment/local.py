from ..common import *
from ..database import sqlite, postgres, config


# DATABASES = sqlite(BASE_DIR)
db_postgres = postgres()

DATABASES = {
    'default': db_postgres
}

STATIC_URL = 'static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'
