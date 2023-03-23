"""
Generated by 'django-admin startproject' using Django 4.1.7.
"""
from datetime import timedelta
from pathlib import Path
import socket

BASE_DIR = Path(__file__).resolve().parent.parent

# In seconds
MAX_OTP_TIME_LIMIT = 300

SECRET_KEY = 'django-insecure-yf$(ex(=lxge2k9cla*z1h+hg%ird%%sth0*&qsb*ycxp^e-je'

DEBUG = True

ALLOWED_HOSTS = []
#Affiliate Commision in Percentage

AFFILIATE_COMMISION_PERCENTAGE = 20



# ___________________________________________
PCLOUD_BASE_URL = "https://eapi.pcloud.com"

PCLOUD_PUB_PATH = "https://eapi.pcloud.com/getpubthumb?code={code}&size={size}"

OTP_EXPIRE_IN_MIN = 10

# ____________________________________________

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'rest_framework',
    'debug_toolbar',
    'api',
    'core',
    'organization',
    'users',
    'event',
    'affiliate',
    'accounts'
]


AUTHENTICATION_BACKENDS = [
    'users.backends.EmailOrPhoneNumberBackend',
    'organization.backends.FeaturePermissionBackend',
    'django.contrib.auth.backends.ModelBackend',
]

# _______________ JWT SETTINGS _______________________________________________
REST_FRAMEWORK = {
    'COERCE_DECIMAL_TO_STRING': False,
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'users.backends.EmailOrPhoneNumberJWTAuthentication',
        'rest_framework_simplejwt.authentication.JWTAuthentication'
    ),
}

SIMPLE_JWT = {
   'AUTH_HEADER_TYPES': ('JWT',),
    'ACCESS_TOKEN_LIFETIME': timedelta(days=5),

}




MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]


hostname, _, ips = socket.gethostbyname_ex(socket.gethostname())
INTERNAL_IPS = [ip[:-1] + "1" for ip in ips]
ALLOWED_HOSTS += ['127.0.0.1', 'localhost'] + INTERNAL_IPS

if DEBUG:
    MIDDLEWARE += [
        'debug_toolbar.middleware.DebugToolbarMiddleware',
    ]
    DEBUG_TOOLBAR_CONFIG = {
        'SHOW_TOOLBAR_CALLBACK': lambda request: True,
    }


ROOT_URLCONF = 'framespik.urls'

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

WSGI_APPLICATION = 'framespik.wsgi.application'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'framespik',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'Sampath@123'
    }
}


# User Model
AUTH_USER_MODEL = 'users.User'


DJOSER = {
    'SERIALIZERS':{
        'user_create': 'users.serializers.UserCreateSerializer',
        'current_user': 'users.serializers.UserSerializer',
        'user': 'users.serializers.UserSerializer',
    }
    
}



# Password validation
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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'Asia/Kolkata'

USE_I18N = True

USE_TZ = True


STATIC_URL = 'static/'

# Default primary key field type
DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
