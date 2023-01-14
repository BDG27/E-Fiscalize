from pathlib import Path, os
from dotenv import load_dotenv
from distutils.util import strtobool
import os, json, socket, platform


# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent
# Carrega Variaveis de Ambiente
HOST_IP = socket.gethostbyname(socket.gethostname())

if(HOST_IP == '0.0.0.0'): ENVIRONMENT = 'production'
elif(HOST_IP == '0.0.0.0'): ENVIRONMENT = 'test'
else: ENVIRONMENT = 'dev'

if ENVIRONMENT == 'dev':load_dotenv(BASE_DIR / '.env.development')
elif ENVIRONMENT == 'production':load_dotenv(BASE_DIR / '.env.production')
elif ENVIRONMENT == 'test':load_dotenv(BASE_DIR / '.env.test')

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-25s4%0(4_)mghm%y($fd4n)h+@7-#iot*=$uffv=i(%#e2zet#'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = bool(strtobool(os.getenv('APP_DEBUG')))

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'apps.company',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'core.urls'

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

WSGI_APPLICATION = 'core.wsgi.application'


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASE_CONFIG = {
    'ENGINE': 'django.db.backends.postgresql_psycopg2',
    'NAME': os.getenv('DB_NAME'),
    'USER': os.getenv('DB_USER'),
    'PASSWORD': os.getenv('DB_PASSWORD'),
    'HOST': os.getenv('DB_HOST'),
    'PORT': os.getenv('DB_PORT')
}

DATABASES = {
    'default': DATABASE_CONFIG,
    'vr': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'vr',
        'USER': 'postgres',
        'PASSWORD': 'postgres',
        'HOST': 'ldbcoopbom.com.br',
        'PORT': '8745'
    },
}


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

LANGUAGE_CODE = 'pt-br'

TIME_ZONE = 'America/Sao_Paulo'

USE_I18N = True

USE_TZ = True

USE_L10N = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = 'static/'

STATIC_ROOT = os.path.join(BASE_DIR, "public")

# STATICFILES_DIRS = [
#     os.path.join(BASE_DIR, 'assets'),
# ]

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR , 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
