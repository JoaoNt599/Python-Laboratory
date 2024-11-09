from .settings import *
DEBUG = False

# Não expor a chave em um projeto real
SECRET_KEY = ';yN=:/)xYv>LJ4yEl.V(hNyEDm;rjX^f\07G(s<Is9OA*MRg!<'

ALLOWED_HOSTS = ['127.0.0.1']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}