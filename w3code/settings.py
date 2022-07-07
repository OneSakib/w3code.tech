"""
Django settings for w3code project.

Generated by 'django-admin startproject' using Django 4.0.3.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import os
from django.contrib.messages import constants as messages_constants

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

DOMAIN_NAME = '127.0.0.1'
HOST_NAME = 'http://' + DOMAIN_NAME + ":8000"

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-$h8&!iox$hjs*eeo2^9gt@k!1r#4@qey-&ormv_91$lb13@-41'
# SECRET_KEY = os.environ['SECRET_KEY']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [DOMAIN_NAME]

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sitemaps',
    'django.contrib.sites',
    "crispy_forms",
    "crispy_bootstrap5",
    'MainApp',
    'tinymce',
    'ProgrammingApp',
    'PreparationApp',
    'TheoryApp',
    'PythonApp',
    'JavaApp',
    'JavaScriptApp',
    'DatabaseApp',
    'WebApp',
    'MsApp',
    'VCApp',
    'Exercise',
    'Programmes',
    'Projects',
    'HostingApp',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'allauth.socialaccount.providers.google',
    'MainApp.templatetags'

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
# Crispy forms

CRISPY_ALLOWED_TEMPLATE_PACKS = "bootstrap5"

CRISPY_TEMPLATE_PACK = "bootstrap5"

ROOT_URLCONF = 'w3code.urls'

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
                'MainApp.context_preprocessor_tut.tut_list'
            ],
        },
    },
]

WSGI_APPLICATION = 'w3code.wsgi.application'

# Database
# https://docs.djangoproject.com/en/4.0/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}

# Password validation
# https://docs.djangoproject.com/en/4.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/4.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/


STATIC_URL = 'static/'

# Media url
MEDIA_URL = 'media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')

# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# TinyMCE online Editor
TINYMCE_DEFAULT_CONFIG = {
    'cleanup_on_startup': True,
    'custom_undo_redo_levels': 20,
    'selector': 'textarea',
    'theme': 'silver',
    'images_upload_url': '/upload_image/',
    'height': '300',
    'plugins': 'codesample'
               '''
                   textcolor save link image media preview codesample contextmenu
                   table code lists fullscreen  insertdatetime  nonbreaking
                   contextmenu directionality searchreplace wordcount visualblocks
                   visualchars code fullscreen autolink lists  charmap print  hr
                   anchor pagebreak
                   ''',
    'toolbar1': 'codesample'
                '''
                    fullscreen preview bold italic underline print fullpage | fontselect,
                    fontsizeselect  | forecolor backcolor emotions | alignleft alignright |
                    aligncenter alignjustify | indent outdent | bullist numlist table |
                    | link image media | codesample | undo redo | styleselect | uploadimage help 
                    ''',
    'paste_data_images': 'true',
    'toolbar2': '''
            visualblocks visualchars |
            charmap hr pagebreak nonbreaking anchor |  code |
            ''',
    'codesample_global_prismjs': True,
    'contextmenu': 'formats | link image',
    'menubar': True,
    'statusbar': True,

}

# messages tags

MESSAGE_TAGS = {
    messages_constants.ERROR: 'danger'
}

# Authentivation
AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    'allauth.account.auth_backends.AuthenticationBackend'
]

SOCIALACCOUNT_PROVIDERS = {
    'google': {
        'SCOPE': [
            'profile',
            'email',
        ],
        'AUTH_PARAMS': {
            'access_type': 'online',
        }
    }
}

SITE_ID = 2
LOGIN_REDIRECT_URL = '/'
LOGOUT_REDIRECT_URL = '/'
SOCIALACCOUNT_LOGIN_ON_GET = True
