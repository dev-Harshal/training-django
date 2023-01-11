from .base import *
from src import vault

DEBUG = True

ALLOWED_HOSTS = ["localhost", "127.0.0.1", "0.0.0.0"]

DATABASES = {
    "default": {
        "ENGINE": vault.DB_ENGINE,
        "NAME": vault.DB_NAME,
        "USER": vault.DB_USER,
        "PASSWORD": vault.DB_PASSWORD,
        "HOST": vault.DB_HOST,  # set in docker-compose.yml
        "PORT": vault.DB_PORT,  # default postgres port
    },
}

EMAIL = vault.EMAIL
PASSWORD = vault.PASSWORD

# AWS credentials

# DEV SECRET KEYS
S3_BUCKET = vault.S3_BUCKET
AWS_KEY_ID = vault.AWS_KEY_ID
AWS_SECRET_KEY = vault.AWS_SECRET_KEY
REGION = vault.REGION
AWS_URL = vault.AWS_URL
REGION = vault.REGION
# Uncomment to disable DRF Class View IN Production
# REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = (
#         'rest_framework.renderers.JSONRenderer',
#     )
