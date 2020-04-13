from . import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'travis_test'
        'USER': os.enrivon.get('POSTGRES_USER'),
        'PASSWORD': os.enrivon.get('POSTGRES_PASS'),
        'HOST': 'localhost',
        'PORT': '5432',
    },
}
