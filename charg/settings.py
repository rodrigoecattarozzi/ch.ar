import os
from django.contrib import messages
from pathlib import Path
# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = Path(__file__).resolve().parent.parent


SECRET_KEY = '#7(^)qnh55*ac)6*+4=)&&v13vv@yemdbbkt!oiwkzkky$^o9f'

# SECURITY WARNING: don't run with debug turned on in production!





INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    #'django_filters',
    'apps.usuarios',
    'apps.categorias',
    'apps.preguntas',
    'apps.respuestas',
    'apps.partidas',
    
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

ROOT_URLCONF = 'charg.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ["templates"],
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

WSGI_APPLICATION = 'charg.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases




# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'es-ar'

TIME_ZONE = 'America/Argentina/Buenos_Aires'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR / "static"),
)
STATIC_ROOT = os.path.join(BASE_DIR, "staticfiles")
print("\n\n"+STATIC_ROOT+"\n\n")
LOGIN_URL = "usuarios:login"
LOGIN_REDIRECT_URL = 'home'
LOGOUT_REDIRECT_URL = 'home'

MESSAGE_STORAGE = "django.contrib.messages.storage.cookie.CookieStorage"

#MESSAGE_TAGS = {
#    messages.DEBUG: 'alert-info',
#    messages.INFO: 'alert-info',
#    messages.SUCCESS: 'alert-success',
#    messages.WARNING: 'alert-warning',
#    messages.ERROR: 'alert-danger',
#}

ENVIROMENT = os.environ.get("ENVIROMENT","LOCAL")

if ENVIROMENT == "PROD":
    # Usar conf de heroku
    DEBUG = os.environ.get("DEBUG", False)
    import django_heroku
    django_heroku.settings(locals())
elif ENVIROMENT == "LOCAL":
    # para usar sqlit
    DEBUG = True

    ALLOWED_HOSTS = []

    DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.sqlite3',
            'NAME': BASE_DIR / 'db.sqlite3',
        }
    }
else:
    #para que siga funcionando con sqlserver como estaba antes
    DEBUG = True
    ALLOWED_HOSTS = []
    DATABASES = {
        'default': {
            'ENGINE': 'sql_server.pyodbc',
            'NAME': 'FINAL',
            'Trusted_Connection':'yes',
            'HOST':'localhost\\SQLEXPRESS',
            'OPTIONS':{
                'driver':'SQL Server Native Client 11.0',
            }
        }
    }    