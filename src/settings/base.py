from pathlib import Path
import os
from datetime import timedelta

# Project Name
PROJECT_NAME = "message-board"

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent.parent

# Create log directory
# Create log directory
LOGS_DIR = os.path.join(BASE_DIR, 'logs')
API_LOG_DIR = os.path.join(LOGS_DIR, "api")
GUNICORN_LOG_DIR = os.path.join(LOGS_DIR, 'gunicorn')
CELERY_LOG_DIR = os.path.join(LOGS_DIR, 'celery')
EXCEPTION_LOG_DIR = os.path.join(LOGS_DIR, "exceptions")

if not os.path.exists(LOGS_DIR):
    os.mkdir(LOGS_DIR)
    os.mkdir(API_LOG_DIR)
    os.mkdir(GUNICORN_LOG_DIR)
    os.mkdir(CELERY_LOG_DIR)
    os.mkdir(EXCEPTION_LOG_DIR)
    # os.mkdir(exception_error_file)

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-y*z$q8($bqrrpz6^f0g$dfg*=d23p3eq+ciig46x69^ia=dvyk'

# SECURITY WARNING: don't run with debug turned on in production!


# Application definition

INSTALLED_APPS = [
    "whitenoise.runserver_nostatic",
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    "rest_framework",
    "corsheaders",
    "django_filters",
    "django_extensions",
    "atomicloops",
    "drf_api_logger",
    "django_rest_passwordreset",
    "drf_yasg",
    "debug_toolbar",
    "import_export",
    "rest_framework_simplejwt.token_blacklist",
    "messenger",
]

MIDDLEWARE = [
    "whitenoise.middleware.WhiteNoiseMiddleware",
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    "debug_toolbar.middleware.DebugToolbarMiddleware",  # Debugger Middleware
    'drf_api_logger.middleware.api_logger_middleware.APILoggerMiddleware',  # Add here
]

CORS_ORIGIN_ALLOW_ALL = True
ROOT_URLCONF = 'src.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates',
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]


# Logger Configuration
DRF_API_LOGGER_DATABASE = True
DRF_API_LOGGER_DEFAULT_DATABASE = 'default'
DRF_API_LOGGER_EXCLUDE_KEYS = ['password', 'token', 'access', 'refresh']

WSGI_APPLICATION = 'src.wsgi.application'

# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

# Change Timezone
TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATIC_ROOT = os.path.join(BASE_DIR, 'staticfiles')

# CUSTOM MODEL
AUTH_USER_MODEL = 'atomicloops.Users'

# JWT Configuration
SIMPLE_JWT = { 
    'ACCESS_TOKEN_LIFETIME': timedelta(days=1),
    'REFRESH_TOKEN_LIFETIME': timedelta(days=7),
    "SIGNING_KEY": "tc!6bn-gztojg@-bz!phc3=&i@*j7)$a97+emlz1z^x^6o5@k0",
    'ROTATE_REFRESH_TOKENS': True,
    'BLACKLIST_AFTER_ROTATION': True
}


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587


# Debugger Tool
# INTERNAL_IPS = (INTERNAL_IPS = ('127.0.0.1',))
INTERNAL_IPS = ('127.0.0.1',)


def show_toolbar(*args, **kwargs):
    return True


DEBUG_TOOLBAR_CONFIG = {
    'SHOW_TOOLBAR_CALLBACK': show_toolbar,
}

# Django Reset Passwod Configuration
DJANGO_REST_PASSWORDRESET_TOKEN_CONFIG = {
    "CLASS": "django_rest_passwordreset.tokens.RandomNumberTokenGenerator",
    "OPTIONS": {
        "min_number": 100000,
        "max_number": 999999
    }
}

# Rest Framework Configuration
REST_FRAMEWORK = {
    'DATETIME_FORMAT': "%Y-%m-%dT%S:%M:%H",
    'DEFAULT_PAGINATION_CLASS': 'atomicloops.pagination.AtomicloopsPagination',
    'PAGE_SIZE': 10,
    'DEFAULT_AUTHENTICATION_CLASSES': [
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    ],
    'DEFAULT_PERMISSION_CLASSES': [
        'atomicloops.permissions.IsOwnerOrAdminOrReadOnly',
        'rest_framework.permissions.IsAuthenticated',

    ],
    'DEFAULT_RENDERER_CLASSES': [
        'atomicloops.renderers.AtomicJsonRenderer',
    ],
    'DEFAULT_FILTER_BACKENDS': [
        'django_filters.rest_framework.DjangoFilterBackend',
        'rest_framework.filters.SearchFilter',
    ],
}

# RabbitMQ configuration
CELERY_BROKER_URL = 'amqp://admin:admin@demo-rabbit-mq'

# REDIS Server
CACHES = {
    "default": {
        "BACKEND": "django_redis.cache.RedisCache",
        "LOCATION": "redis://redis:6379/1",
        "OPTIONS": {
            "CLIENT_CLASS": "django_redis.client.DefaultClient"
        },
        "KEY_PREFIX": "example"
    }
}

# TIMEOUT for REDIS 5 minutes
CACHE_TTL = 60 * 5

#
APPEND_SLASH = False
