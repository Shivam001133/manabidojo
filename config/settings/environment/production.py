from ..helpers.cloudflare.settings import CLOUDFLARE_R2_CONFIG_OPTIONS


STATIC_URL = f"{CLOUDFLARE_R2_CONFIG_OPTIONS['endpoint_url']}/{CLOUDFLARE_R2_CONFIG_OPTIONS['bucket_name']}/static/"
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
