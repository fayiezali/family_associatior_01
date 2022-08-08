"""
Django settings for PROJECT project.

Generated by 'django-admin startproject' using Django 4.0.5.

For more information on this file, see
https://docs.djangoproject.com/en/4.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.0/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-%_h+d+)q56wif)t6cl9*lbaxtf2)0g+syp)fh6(b#xtqu&1keo'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # an Application Improved Forms Design and That Beautifies The Look Of HTML Pages
    'crispy_forms', 
    'widget_tweaks', 
    # ----------------------------------
    # Applications OTP (1)
    'django_otp',
    'django_otp.plugins.otp_totp',
    # ----------------------------------
    # User Accounts Application
    'accounts',
    #  Home Pages Application
    'home',
    # Application Send messages
    'sms',
    # 'social_django',# 04 Login With Social Media(Facebook , Instagram ,......)
    # 'django_countries',# تطبيق معد مسبقاً يحتوي على جميع اسماء دول العالم
    'phonenumber_field',
]
#
MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # ----------------------------------
    # Applications OTP (2)
    'django_otp.middleware.OTPMiddleware',
    # ----------------------------------
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]

ROOT_URLCONF = 'PROJECT.urls'

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
            ],
        },
    },
]

WSGI_APPLICATION = 'PROJECT.wsgi.application'


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
# 
# To Access "static" Files In App Only
STATIC_URL = 'static/'
#
# To Access "static" Files In Project (All App)
STATICFILES_DIRS = [ BASE_DIR / "static"]
# '/media/':  الوسائط المتعددة"Media" بإدارة ملفات الـ "static" يقوم مجلد 
# '/media/': التي يحتاجها المشروع "Documents ,Images , Audio , Video,"هو مجلد  يتحوي على جميع ملفات 
# '/media/': يتم إستدعائها عن طريق هذا المجلد . هذاالمجلد فيه جميع إعدادت وتنسيقات الصفحة  "app"في التطبيق  "html"أي صفحة 
# To Access "media" Files In App Only
MEDIA_URL = 'media/'
#
# To Access "media" Files In Project (All App)
MEDIA_ROOT = (BASE_DIR /'media')
#
# Default primary key field type
# https://docs.djangoproject.com/en/4.0/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


LOGIN_REDIRECT_URL = 'index_pageURL' # Go To Home Page HTML
LOGOUT_REDIRECT_URL = 'LogoutDoneURL' # Go To LogoutDone.html Page HTML
LOGIN_ERROR_URL = 'login'


#Call Class Sign  In with Email
AUTHENTICATION_BACKENDS = ['accounts.backends.EmailBackend']

# EMAIL_BACKEND = "django.core.mail.backends.filebased.EmailBackend"
EMAIL_FILE_PATH = str(BASE_DIR.joinpath('sent_emails'))

# Email Settings
from accounts.email_info import EMAIL_BACKEND , EMAIL_HOST , EMAIL_HOST_USER , EMAIL_HOST_PASSWORD , EMAIL_PORT ,  EMAIL_USE_TLS , PASSWORD_RESET_TIMEOUT_DAYS
EMAIL_BACKEND = EMAIL_BACKEND
EMAIL_HOST = EMAIL_HOST # mail service smtp
EMAIL_HOST_USER = EMAIL_HOST_USER# email id
EMAIL_HOST_PASSWORD = EMAIL_HOST_PASSWORD # password
EMAIL_PORT = EMAIL_PORT
EMAIL_USE_TLS = EMAIL_USE_TLS
PASSWORD_RESET_TIMEOUT_DAYS = PASSWORD_RESET_TIMEOUT_DAYS
#
# Applications OTP (3)
ECURE_SSL_REDIRECT = True
SESSION_COOKIE_SECURE = True
SESSION_COOKIE_SECURE = True
SECURE_BROWSER_XSS_FILTER = True
SECURE_HSTS_SECONDS = 31536000
SECURE_HSTS_INCLUDE_SUBDOMAINS = True
SECURE_HSTS_PRELOAD = True
SECURE_CONTENT_TYPE_NOSNIFF = True
CSRF_COOKIE_SECURE = True
# social auth
# SOCIAL_AUTH_URL_NAMESPACE = 'social'
# SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = os.getenv('SOCIAL_AUTH_GOOGLE_OAUTH2_KEY')
# SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = os.getenv('SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET')

SOCIAL_AUTH_PIPELINE = (
    'social_core.pipeline.social_auth.social_details',
    'social_core.pipeline.social_auth.social_uid',
    'social_core.pipeline.social_auth.auth_allowed',
    'social_core.pipeline.social_auth.social_user',
    'social_core.pipeline.user.get_username',
    'social_core.pipeline.user.create_user',
    'social_core.pipeline.social_auth.associate_user',
    'social_core.pipeline.social_auth.load_extra_data',
    'social_core.pipeline.user.user_details',
)
