import os
from dotenv import load_dotenv

# loading env file
load_dotenv()

environment = os.getenv("DJANGO_ENV", "local").lower()

if environment == "prod":
    from .environment.production import *
else:
    from .environment.local import *

