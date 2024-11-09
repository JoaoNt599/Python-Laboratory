from .settings import *

DEBUG = True

# Não expor a chave em um projeto real
SECRET_KEY = ',\%joX|w\2<QoHkby:,s(i)o"+OKWOAY~2vyEoB+~`~Eqtx~Dh'

ALLOWED_HOSTS = ['127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}