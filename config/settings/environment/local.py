from ..common import *
from ..database import sqlite, postgres, config


# DATABASES = sqlite(BASE_DIR)
db_postgres = postgres()

DATABASES = {"default": db_postgres}

# static config
STATIC_URL = "static/"
print(BASE_DIR)
STATICFILES_DIRS = [
    BASE_DIR / 'manabhi_dojo' / 'static',
]

# mdedia config
MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"
