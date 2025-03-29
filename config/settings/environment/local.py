from ..common import *
from ..database import sqlite

DATABASES = sqlite(BASE_DIR)
