from .settings import *

DEBUG = True

# Não expor a chave em um projeto real
SECRET_KEY = 'j@M\.OaFSa%VB%q49bjq{[l`%Uy#IMoeyi9iH6~P`Qf%-vWG%'

ALLOWED_HOSTS = ['localhost', '127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}