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
import dj_database_url


 

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-h_-mw2x7)q**%bi%pjwaewxcuy*-ziit_5e-&q68l&*k=w7=$b'
#SECRET_KEY =os.getenv('DJANGO_SECRET_KEY')


PAYSTACK_PUBLIC_KEY =os.getenv('PAYSTACK_PUBLIC_KEY') 
PAYSTACK_SECRET_KEY =os.getenv('PAYSTACK_SECRET_KEY') 
FLUTTERWAVE_PUBLIC_KEY =os.getenv('FLUTTERWAVE_PUBLIC_KEY')
FLUTTERWAVE_SECRET_KEY =os.getenv('FLUTTERWAVE_SECRET_KEY')

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
    'storages',
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

AUTH_USER_MODEL = 'website.Account'

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





# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


DATABASES = {
    'default': dj_database_url.parse(os.getenv('Stormxbet_Database'))
}


EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
EMAIL_HOST='smtppro.zoho.com'
EMAIL_HOST_PASSWORD='WyQwJ4f53UyK'
EMAIL_HOST_USER='admin@stormxbet.com'
EMAIL_USE_TLS = True
EMAIL_PORT = 587



LOGIN_REDIRECT_URL = 'loginsuccess'
LOGOUT_REDIRECT_URL = 'logoutsuccess'
SESSION_EXPIRE_AT_BROWSER_CLOSE = True

#S3 BUCKETS CONFIG

AWS_ACCESS_KEY_ID='AKIA2OYYUX6SNI3FTV6T'
AWS_SECRET_ACCESS_KEY='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'
AWS_STORAGE_BUCKET_NAME = 'stormxbet'
DEFAULT_FILE_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'
STATICFILES_STORAGE = 'storages.backends.s3boto3.S3Boto3Storage'







