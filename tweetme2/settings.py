import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'ny%n!3pz3piy(pj)zyiyjngp^pgy(ryt151&)55rr57q&c$uxg'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

#  basically use this for is_safe_url  for more information check views.py
ALLOWED_HOSTS = ['127.0.0.1' , '.myhost.sh','localhost']

# naresh self difind this login url is not givin default
LOGIN_URL = '/login'
MAX_TWEET_LENGTH = 240


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # Third-Party
    'corsheaders',
    'rest_framework',
    # internal
    'tweets',
    'profiles',
    'accounts',
    'crispy_forms',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    # django coreheaders middleware
    'corsheaders.middleware.CorsMiddleware',
]

ROOT_URLCONF = 'tweetme2.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR , 'templates'],
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

WSGI_APPLICATION = 'tweetme2.wsgi.application'


# Database
# https://docs.djangoproject.com/en/2.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/2.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/2.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/2.2/howto/static-files/


STATICFILES_DIRS = [
    os.path.join(BASE_DIR,'tweetme2/static')
]

STATIC_ROOT = os.path.join(BASE_DIR,'static')
STATIC_URL = '/static/'


CORS_ORIGIN_ALLOW_ALL = True   # any website access to my api
CORS_URLS_REGEX = r'^/api/.*$'

DEFAULT_RENDERER_CLASSES = [
        'rest_framework.renderers.JSONRenderer',
    ]




# if django a on debug then we show our in rest_framework view
if DEBUG:
    DEFAULT_AUTHENTICATION_CLASSES = [ 
    'rest_framework.authentication.SessionAuthentication',
    ]
    # DEFAULT_AUTHENTICATION_CLASSES += [
    #      'tweetme2.rest_api.dev.DevAuthentication'
    # ]
    DEFAULT_RENDERER_CLASSES.append('rest_framework.renderers.BrowsableAPIRenderer')

# Third pary for create a seeion for every view
REST_FRAMEWORK = { 
   'DEFAULT_AUTHENTICATION_CLASSES' : DEFAULT_AUTHENTICATION_CLASSES,
    # These class show your json data as a normal view
    'DEFAULT_RENDERER_CLASSES': DEFAULT_RENDERER_CLASSES

}


CRISPY_TEMPLATE_PACK = 'bootstrap4'