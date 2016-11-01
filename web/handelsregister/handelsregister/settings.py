"""
Django settings for handelsregister project.

Generated by 'django-admin startproject' using Django 1.9.2.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.9/ref/settings/
"""
import re
import os
import sys

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


def _get_docker_host():
    d_host = os.getenv('DOCKER_HOST', None)
    if d_host:
        return re.match(r'tcp://(.*?):\d+', d_host).group(1)
    return '0.0.0.0'


VBO_URI = "https://api-acc.datapunt.amsterdam.nl/bag/verblijfsobject/"
CBS_URI = 'http://sbi.cbs.nl/cbs.typeermodule.typeerservicewebapi/api/sbianswer/getNextQuestion/{}'
CSB_SEARCH = 'http://sbi.cbs.nl/cbs.typeermodule.typeerservicewebapi/api/SBISearch/search/{}'

# SECURITY WARNING: keep the secret key used in production secret!
insecure_key = 'insecure'
SECRET_KEY = os.getenv('HANDELSREGISTER_SECRET_KEY', insecure_key)

DEBUG = SECRET_KEY == insecure_key

ALLOWED_HOSTS = ['*']


PARTIAL_IMPORT = {
    'numerator': 0,
    'denominator': 1,
}

PROJECT_APPS = [
    'handelsregister',
    'datasets.kvkdump',
    'datasets.hr',
    'geo_views',
]

DATAPUNT_API_URL = 'https://api.datapunt.amsterdam.nl/'

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',

    'django_extensions',

    'django.contrib.gis',
    'rest_framework',
    'rest_framework_gis',
    'rest_framework_swagger',

] + PROJECT_APPS

if DEBUG:
    INSTALLED_APPS += (
        'debug_toolbar', 'explorer')

SITE_ID = 1

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]


ROOT_URLCONF = 'handelsregister.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
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

WSGI_APPLICATION = 'handelsregister.wsgi.application'


def get_docker_host():
    """Find the local docker-deamon
    """
    d_host = os.getenv('DOCKER_HOST', None)
    if d_host:
        if re.match(r'^\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}$', d_host):
            return d_host
        return re.match(r'tcp://(.*?):\d+', d_host).group(1)
    return 'localhost'

# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

#database = os.environ.get('DATABASE_1_ENV_POSTGRES_DB', 'handelregister')
#    password = os.environ.get('DATABASE_ENV_POSTGRES_PASSWORD', 'insecure')
#    user = os.environ.get('DATABASE_1_ENV_POSTGRES_USER', 'handelsregister')
#    port = os.environ.get('DATABASE_1_PORT_5432_TCP_PORT', 5432)
#    host = os.environ.get(
#        'HANDELSREGISTER_DATABASE_1_PORT_5432_TCP_ADDR', '127.0.0.1')


DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': os.getenv('DATABASE_NAME', 'handelsregister'),
        'USER': os.getenv('DATABASE_USER', 'handelsregister'),
        'PASSWORD': os.getenv('DATABASE_PASSWORD', 'insecure'),
        'HOST': os.getenv('DATABASE_PORT_5432_TCP_ADDR', get_docker_host()),
        'PORT': os.getenv('DATABASE_PORT_5432_TCP_PORT', '5406'),
    }
}


ELASTIC_SEARCH_HOSTS = ["{}:{}".format(
    os.getenv('ELASTICSEARCH_PORT_9200_TCP_ADDR', _get_docker_host()),
    os.getenv('ELASTICSEARCH_PORT_9200_TCP_PORT', 9200))]


# Password validation
# https://docs.djangoproject.com/en/1.9/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.9/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

DUMP_DIR = 'mks-dump'

TESTING = len(sys.argv) > 1 and sys.argv[1] == 'test'

ELASTIC_INDICES = {
    'HR': 'handelsregister',
}

if TESTING:
    for k, v in ELASTIC_INDICES.items():
        ELASTIC_INDICES[k] = ELASTIC_INDICES[k] + 'test'

BATCH_SETTINGS = dict(
    batch_size=4000
)


REST_FRAMEWORK = dict(
    PAGE_SIZE=25,

    MAX_PAGINATE_BY=100,
    DEFAULT_AUTHENTICATION_CLASSES=(
        'rest_framework.authentication.BasicAuthentication',
        'rest_framework.authentication.SessionAuthentication',
    ),
    DEFAULT_PAGINATION_CLASS='drf_hal_json.pagination.HalPageNumberPagination',
    DEFAULT_PARSER_CLASSES=('drf_hal_json.parsers.JsonHalParser',),
    DEFAULT_RENDERER_CLASSES=(
        'rest_framework.renderers.JSONRenderer',
        'rest_framework.renderers.BrowsableAPIRenderer'
    ),
    DEFAULT_FILTER_BACKENDS=(
        'rest_framework.filters.DjangoFilterBackend',
        'rest_framework.filters.OrderingFilter',

        ),
    COERCE_DECIMAL_TO_STRING=True,
)

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.9/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.abspath(os.path.join(BASE_DIR, '..', 'static'))

HEALTH_MODEL = 'hr.MaatschappelijkeActiviteit'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,

    'formatters': {
        'console': {
            'format': '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        },
    },

    'handlers': {
        'console': {
            'level': 'DEBUG',
            'class': 'logging.StreamHandler',
            'formatter': 'console',
        },
    },

    'root': {
        'level': 'DEBUG',
        'handlers': ['console'],
    },


    'loggers': {
        'django': {
            'handlers': ['console'],
            'level': 'ERROR',
        },

        # Debug all batch jobs
        'doc': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },
        'index': {
            'handlers': ['console'],
            'level': 'DEBUG',
            'propagate': False,
        },

        'search': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': False,
        },

        'elasticsearch': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': False,
        },

        'urllib3': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': False,
        },

        'factory.containers': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },

        'factory.generate': {
            'handlers': ['console'],
            'level': 'INFO',
            'propagate': False,
        },

        'requests.packages.urllib3.connectionpool': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': False,
        },

        # Log all unhandled exceptions
        'django.request': {
            'handlers': ['console'],
            'level': 'ERROR',
            'propagate': False,
        },

    },
}
