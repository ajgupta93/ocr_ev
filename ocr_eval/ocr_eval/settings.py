"""
Django settings for ocr_eval project.

For more information on this file, see
https://docs.djangoproject.com/en/1.6/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.6/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.6/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '*apbusvo0$41q%hc09ps@#(4+g+gi^kgms5+k^ak(n2k^tsxi0'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = [
    '*',
]


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
     # The Django sites framework is required
    'django.contrib.sites',
    'allauth',
    'allauth.account',
    'allauth.socialaccount',
    'ocr_evaluation',
    'filetransfers',
#    'south',
    'graphos',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'ocr_eval.urls'

WSGI_APPLICATION = 'ocr_eval.wsgi.application'

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    # Required by allauth template tags
    "django.core.context_processors.request",
    # allauth specific context processors
    "allauth.account.context_processors.account",
    "allauth.socialaccount.context_processors.socialaccount",
)

AUTHENTICATION_BACKENDS = (
    # Needed to login by username in Django admin, regardless of `allauth`
    "django.contrib.auth.backends.ModelBackend",
    # `allauth` specific authentication methods, such as login by e-mail
    "allauth.account.auth_backends.AuthenticationBackend",
)

SITE_ID = 1

# Settings for the app

TEMPLATE_DIRS = (
    os.path.join(BASE_DIR,'ocr_evaluation/templates'),
)

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# Specifies the login method to use -- whether the user logs in by entering his username, e-mail address, or either one of both.
ACCOUNT_AUTHENTICATION_METHOD ="username"

# Determines the expiration date of email confirmation mails (# of days).
ACCOUNT_EMAIL_CONFIRMATION_EXPIRE_DAYS = 5

# The user is required to hand over an e-mail address when signing up.
ACCOUNT_EMAIL_REQUIRED = True

# Determines the e-mail verification method during signup -- choose one of "mandatory", "optional", or "none". When set to "mandatory" the user is blocked from logging in until the email address is verified. Choose "optional" or "none" to allow logins with an unverified e-mail address. In case of "optional", the e-mail verification mail is still sent, whereas in case of "none" no e-mail verification mails are sent.
ACCOUNT_EMAIL_VERIFICATION = "mandatory"

# When signing up, let the user type in his password twice to avoid typo's.
ACCOUNT_SIGNUP_PASSWORD_VERIFICATION = True

# An integer specifying the minimum allowed length of a username.
ACCOUNT_USERNAME_MIN_LENGTH = 8

# An integer specifying the minimum password length.
ACCOUNT_PASSWORD_MIN_LENGTH = 6

# The default behaviour is to automatically log the user in once he confirms his email address. By changing this setting to False he will not be logged in, but redirected to the ACCOUNT_EMAIL_CONFIRMATION_ANONYMOUS_REDIRECT_URL
ACCOUNT_LOGIN_ON_EMAIL_CONFIRMATION = False

# Controls the life time of the session. Set to None to ask the user ("Remember me?"), False to not remember, and True to always remember.
ACCOUNT_SESSION_REMEMBER = None

# How long before the session cookie expires in seconds. Defaults to 1814400 seconds, or 3 weeks.
ACCOUNT_SESSION_COOKIE_AGE = 1814400

# Database
# https://docs.djangoproject.com/en/1.6/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'ocr_portal',                      
        'USER': 'django_login',                   
        'PASSWORD': 'ajitesh20',              
        'HOST': 'localhost',                      
        'PORT': '5432',           
    }
}

# Internationalization
# https://docs.djangoproject.com/en/1.6/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.6/howto/static-files/

STATIC_ROOT = BASE_DIR

STATIC_URL = '/static/'

STATICFILES_DIRS = (
    ('assets',os.path.join(BASE_DIR,'static')),
)

MEDIA_ROOT = os.path.join(BASE_DIR,'media')

MEDIA_URL = '/media/'
