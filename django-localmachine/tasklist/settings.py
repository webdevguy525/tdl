"""
Django settings for tasklist project.
"""
import os
from django.urls import reverse_lazy
import dj_database_url
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SECRET_KEY = 'i7@ysk_cg#6o5c49zt(nh61a2$io9477n(bka+v4n=6gwa!2pk'

DEBUG = True
# ALLOWED_HOSTS = ['127.0.0.1', '.herokuapp.com']

# Application definition
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.sites',
    'django_comments',
    'django.contrib.humanize',
    'crispy_forms',
    'django_tables2',
    'tasks',
)

MIDDLEWARE = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'tasklist.urls'
WSGI_APPLICATION = 'tasklist.wsgi.application'

# Database
SQLITE_DB = os.path.join(BASE_DIR, 'db.sqlite3')
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': SQLITE_DB,
    }
}

# Internationalization
LANGUAGE_CODE = 'en-US'
TIME_ZONE = 'US/Eastern'
USE_I18N = True
USE_L10N = False
USE_TZ = True

SHORT_DATE_FORMAT = 'N j, Y'
STATIC_ROOT = ""
STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static'),
)
CRISPY_TEMPLATE_PACK = 'bootstrap3'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, 'templates/'),os.path.join(BASE_DIR, 'templates/')],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                "django.contrib.auth.context_processors.auth",
            ],
        },
    },
]

LOGIN_URL = reverse_lazy('login')
LOGIN_REDIRECT_URL = reverse_lazy('list_tasks')
SITE_ID = 1
