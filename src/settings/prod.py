from .base import *
from src import vault
DEBUG = True

ALLOWED_HOSTS = ["*"]

DATABASES = {
    "default": {
        "ENGINE": vault.PROD_DB_ENGINE,
        "NAME": vault.PROD_DB_NAME,
        "USER": vault.PROD_DB_USER,
        "PASSWORD": vault.PROD_DB_PASSWORD,
        "HOST": vault.PROD_DB_HOST,  # set in docker-compose.yml
        "PORT": vault.PROD_DB_PORT,  # default postgres port
    },
}

EMAIL = vault.PROD_EMAIL
PASSWORD = vault.PROD_PASSWORD

# AWS credentials

# DEV SECRET KEYS
S3_BUCKET = vault.PROD_S3_BUCKET
AWS_KEY_ID = vault.PROD_AWS_KEY_ID
AWS_SECRET_KEY = vault.PROD_AWS_SECRET_KEY
REGION = vault.PROD_REGION
AWS_URL = vault.PROD_AWS_URL
REGION = vault.PROD_REGION

# TODO: More details on it.
if not DEBUG:
    SECURE_HSTS_SECONDS = 86400
    SECURE_HSTS_INCLUDE_SUBDOMAINS = True
    SECURE_HSTS_PRELOAD = True
    SECURE_SSL_REDIRECT = True
    CSRF_COOKIE_SECURE = True
    SESSION_COOKIE_SECURE = True
