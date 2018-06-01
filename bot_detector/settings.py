"""
Django settings for bot_detector project.

Generated by 'django-admin startproject' using Django 1.11.10.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
PROJECT_ROOT = os.path.dirname(os.path.realpath(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'w^c6=l8e&@zgpp3v_m*(pppw%3p5+5nzy8$gqy^9ob5jwez#a0'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['0.0.0.0', 'localhost', '127.0.0.1']
LOGIN_REDIRECT_URL = '/'

# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'bot_finder',
]

MIDDLEWARE_CLASSES = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'bot_detector.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [PROJECT_ROOT + '/templates/'],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.core.context_processors.media',
                'django.core.context_processors.static',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'bot_detector.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases



# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': "bot_detection_webapp",
        'USER': "koray",
        'PASSWORD': "koray",
        'HOST': '',
        'PORT': '',
    }
}

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.11/topics/i18n/

LANGUAGE_CODE = 'tr'

TIME_ZONE = 'Europe/Istanbul'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/


STATIC_URL = PROJECT_ROOT + '/static/'
STATIC_ROOT = PROJECT_ROOT + '/static/'
print (BASE_DIR)
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, '/static/'),
)

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR, '/templates/'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)


access_token = "75166266-lKHuaTrC4WBGdzp9oFvSJN2jFNe6BzEW1a7NHA59n"
access_secret = "3gorUNeoPdJHDzV1X02zoiuygRxOO9iwG82dUmHkKWfA1"
consumer_key = "zRuKIDvTumdERI0gi2MvoUAyG"
consumer_secret = "UkC1vHhQpxenaxXlyS2XFOMCsmLv1vsYGeVUbc1VkHQXT3iyg0"

avg_tweet_cutoff = 50 #bot sayilmasi icin gunde ortalama kac tweet'ten fazla atmasi gerekiyor bir profilin?
RT_cutoff = 95 #bot sayilmasi icin RT oraninin kaca esit veya uzerinde olmasi gerekiyor