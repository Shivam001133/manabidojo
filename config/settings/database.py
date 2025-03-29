from pathlib import Path


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
