import os

def sqllite(BASE_DIR: str):
    # Database
    # https://docs.djangoproject.com/en/5.1/ref/settings/#databases

    os.makedirs("db", exist_ok=True)
    db_dir = os.path.join(BASE_DIR, "db")

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': db_dir / 'db.sqlite3',
        }
    }
