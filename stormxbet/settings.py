"""
Django settings for Project project.

Generated by 'django-admin startproject' using Django 4.0.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path
import os


 

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
#SECRET_KEY = 'django-insecure-h_-mw2x7)q**%bi%pjwaewxcuy*-ziit_5e-&q68l&*k=w7=$b'
SECRET_KEY ='django-insecure-h_-mw2x7)q**%bi%pjwaewxcuy*-ziit_5e-&q68l&*k=w7=$b'


PAYSTACK_PUBLIC_KEY ='pk_test_1bfedd2d003e06ff8e3dd6608c5cf8e4af6e3bad' 
PAYSTACK_SECRET_KEY ='sk_test_9c401b00dbe5c711464411947179fa9e5870582c' 
FLUTTERWAVE_PUBLIC_KEY ='FLWPUBK_TEST-1e07aacf87e94a2315d1b372df9971c7-X'
FLUTTERWAVE_SECRET_KEY ='FLWSECK_TEST-30d35ad2524523a9d0ccea9586b86de0-X'

# SECURITY WARNING: don't run with debug turned on in production!

DEBUG =True

ALLOWED_HOSTS = ['*']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'website.apps.WebsiteConfig',
    'paystack.apps.PaystackConfig',
    'flutterwave.apps.FlutterwaveConfig',
    'Admin.apps.AdminConfig',
    

    #external installed app

    'rest_framework',
    'django_filters',
    'django_celery_beat',
    #'storages',
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

ROOT_URLCONF = 'stormxbet.urls'

AUTH_USER_MODEL = 'website.Custom'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'website.context_processors.number',
            ],
        },
    },
]

WSGI_APPLICATION = 'stormxbet.wsgi.application'




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

TIME_ZONE = 'Africa/Lagos'

USE_I18N = True

USE_TZ = True



# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.0/howto/static-files/

STATIC_URL = '/static/'
STATIC_ROOT = '/static/'
MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATIC_FILES = [
    os.path.join(BASE_DIR, 'static')
]

CELERY_BROKER_URL='amqp://guest:guest@localhost:5672//'



# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME':'Bet',
        'USER':'postgres',
        'PASSWORD':'46347223',
        'HOST':'localhost',
        'PORT':5432
    }
}


EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_HOST = 'localhost'
EMAIL_USE_TLS = True
EMAIL_HOST_USER = 'okoriek55@gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_PASSWORD = ''



LOGIN_REDIRECT_URL = 'loginsuccess'
LOGOUT_REDIRECT_URL = 'logoutsuccess'
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

#S3 BUCKETS CONFIG


#AWS_ACCESS_KEY_ID = 'AKIA2OYYUX6SIGE2TEFP'
#AWS_SECRET_ACCESS_KEY = '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'
#AWS_STORAGE_BUCKET_NAME = 'kwex'
#AWS_S3_FILE_OVERWRITE = False
#AWS_DEFAULT_ACL = None
#DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
#STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'





