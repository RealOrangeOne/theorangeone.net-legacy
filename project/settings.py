import os
import dj_database_url

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ALLOWED_HOSTS = ['*']

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = os.environ['DEBUG']
ENABLE_ADMIN = DEBUG

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ['SECRET_KEY']

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'


# Application definition
INSTALLED_APPS = [
    'wagtail.wagtailforms',
    'wagtail.wagtailredirects',
    'wagtail.wagtailembeds',
    'wagtail.wagtailsites',
    'wagtail.wagtailusers',
    'wagtail.wagtailsnippets',
    'wagtail.wagtaildocs',
    'wagtail.wagtailimages',
    'wagtail.wagtailsearch',
    'wagtail.wagtailadmin',
    'wagtail.wagtailcore',

    'wagtail.contrib.settings',
    "wagtail.contrib.table_block",
    'wagtail.contrib.wagtailstyleguide',
    'modelcluster',
    'taggit',

    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    'wagtailmetadata',

    'project.blog',
    'project.common',
    'project.home',
    'project.pages',
    'project.projects',
    'project.search',
]

if ENABLE_ADMIN:
    INSTALLED_APPS += ['django.contrib.admin']

# Harden Django!
if not DEBUG:
    SESSION_COOKIE_SECURE = True
    CSRF_COOKIE_SECURE = True
    CSRF_COOKIE_HTTPONLY = True
    SECURE_CONTENT_TYPE_NOSNIFF = True
    SECURE_BROWSER_XSS_FILTER = True
    SECURE_SSL_REDIRECT = True

X_FRAME_OPTIONS = 'DENY'
MAX_UPLOAD_SIZE = 5242880  # 5MB - 5242880


MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',

    'whitenoise.middleware.WhiteNoiseMiddleware',

    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

    'wagtail.wagtailcore.middleware.SiteMiddleware',
    'wagtail.wagtailredirects.middleware.RedirectMiddleware'
]

ROOT_URLCONF = 'project.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates'),
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'wagtail.contrib.settings.context_processors.settings',
                'project.common.context.settings_injector'
            ],
        },
    },
]

WSGI_APPLICATION = 'project.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases

DATABASES = {
    'default': dj_database_url.config(default="sqlite:///{}/db.sqlite3".format(BASE_DIR), conn_max_age=300)
}


# Internationalization
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'en-GB'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'static', 'build'),
]

STATIC_ROOT = os.path.join(BASE_DIR, 'collected-static')
STATIC_URL = '/static/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
MEDIA_URL = '/media/'

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'


# Wagtail settings

WAGTAIL_SITE_NAME = "TheOrangeOne"

WAGTAIL_PASSWORD_MANAGEMENT_ENABLED = True
WAGTAIL_ENABLE_UPDATE_CHECK = True
WAGTAIL_ALLOW_UNICODE_SLUGS = True
WAGTAIL_USAGE_COUNT_ENABLED = True
WAGTAILIMAGES_JPEG_QUALITY = 100


WAGTAILSEARCH_BACKENDS = {
    'default': {
        'BACKEND': 'wagtail.wagtailsearch.backends.db',
    }
}

# Base URL to use when referring to full URLs within the Wagtail admin backend -
# e.g. in notification emails. Don't include '/admin' or a trailing slash
BASE_URL = 'https://theorangeone.net'
SITE_URL = BASE_URL


# Password policy settings
SESSION_SERIALIZER = 'django.contrib.sessions.serializers.PickleSerializer'
PASSWORD_CHECK_ONLY_AT_LOGIN = True
PASSWORD_MIN_LENGTH = 7
PASSWORD_MAX_LENGTH = 25
PASSWORD_HISTORY_COUNT = 6
PASSWORD_MIN_LETTERS = 1
PASSWORD_MIN_NUMBERS = 1
PASSWORD_MIN_SYMBOLS = 1
PASSWORD_DIFFERENCE_DISTANCE = 3
