import os
from dotenv import load_dotenv


load_dotenv()


DATABASES = {
    'default': {
        'ENGINE': os.getenv('engine'),
        'HOST': os.getenv('host'),
        'PORT': os.getenv('port'),
        'NAME': os.getenv('name'),
        'USER': os.getenv('user'),
        'PASSWORD': os.getenv('password'),
    }
}

INSTALLED_APPS = ['datacenter']

SECRET_KEY = 'REPLACE_ME'

TIME_ZONE = 'Europe/Moscow'

USE_TZ = True