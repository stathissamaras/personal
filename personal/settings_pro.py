from .settings import *
from decouple import config
import dj_database_url

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = ['personal-vhgz.onrender.com']


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'personalapp',
]

# Database
# https://docs.djangoproject.com/en/5.0/ref/settings/#databases

# DATABASES = {
     #'default': {
         #'ENGINE': 'django.db.backends.postgresql',
         #'NAME': config('DB_NAME'),
         #'USER': config('DB_USER'),
         #'PASSWORD': config('DB_PASSWORD'),
         #'HOST': config('DB_HOST', default='localhost'),
     #}
 #}
DATABASES = {
    'default': dj_database_url.config(default=config('DATABASE_URL'))
}

# HTTPS settings
#SESSION_COOKIE_SECURE = True
#CSRF_COOKIE_SECURE = True
#SECURE_SSL_REDIRECT = True

# HSTS settings
#SECURE_HSTS_SECONDS = 31536000
#SECURE_HSTS_PRELOAD = True
#SECURE_HSTS_INCLUDE_SUBDOMAINS = True

EMAIL_HOST = 'smtppro.zoho.eu'
EMAIL_HOST_USER = 'info@oileco.gr'
EMAIL_HOST_PASSWORD = '$tathis$amarasOkto_Web2023'
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
DEFAULT_FROM_EMAIL = 'info@oileco.gr'

# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.0/howto/static-files/

STATIC_URL = '/static/'
# STATICFILES_DIRS = [os.path.join(BASE_DIR, 'static')]
# STATIC_ROOT = os.path.join(BASE_DIR, 'assets')
if DEBUG:
    STATICFILES_DIRS = [
        os.path.join(BASE_DIR, 'static')
    ]
else:
    STATIC_ROOT = os.path.join(BASE_DIR, 'static')

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
