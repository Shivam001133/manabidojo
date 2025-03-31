import os
from ..common import *
from ..database import postgres
from ..helpers.cloudflare.settings import CLOUDFLARE_R2_CONFIG_OPTIONS


# DATABASES = sqlite(BASE_DIR)
db_postgres = postgres()

DATABASES = {"default": db_postgres}

# Static config
STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')
STATIC_URL = f"{CLOUDFLARE_R2_CONFIG_OPTIONS['endpoint_url']}/{CLOUDFLARE_R2_CONFIG_OPTIONS['bucket_name']}/static/"
# media config
MEDIA_URL = f"{CLOUDFLARE_R2_CONFIG_OPTIONS['endpoint_url']}/{CLOUDFLARE_R2_CONFIG_OPTIONS['bucket_name']}/media/"

STORAGES = {
    "default": {
        "BACKEND": "config.settings.helpers.cloudflare.r2_storage.MediaFileStorage",
        "OPTIONS": CLOUDFLARE_R2_CONFIG_OPTIONS,
    },
    "staticfiles": {
        "BACKEND": "config.settings.helpers.cloudflare.r2_storage.StaticFileStorage",
        "OPTIONS": CLOUDFLARE_R2_CONFIG_OPTIONS,
    },
}
