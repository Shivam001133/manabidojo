import dj_database_url
from pathlib import Path
from os import environ


def sqlite(BASE_DIR: Path):
    # Ensure db directory exists
    db_dir = BASE_DIR / "db"
    db_dir.mkdir(exist_ok=True)

    return {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': db_dir / 'db.sqlite3',
        }
    }


def postgres()-> dj_database_url:
    print("*"*100)
    print(environ.get('DATABASE_URL'))
    return dj_database_url.config(default=environ.get('DATABASE_URL'))
