import os

environment = os.getenv("DJANGO_ENV", "local").lower()

if environment == "prod":
    from .environment.production import *
else:
    from .environment.local import *

