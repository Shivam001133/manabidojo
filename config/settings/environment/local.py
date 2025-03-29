from ..common import *
from ..database import sqlite, postgres

# DATABASES = sqlite(BASE_DIR)
db_postgres = postgres()

DATABASES = {
    'default': db_postgres
}
