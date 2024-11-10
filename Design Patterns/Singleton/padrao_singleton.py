

class Singleton(object):

    def __new__(cls):
        if not hasattr(cls, 'instance'):
            cls.instance = super(Singleton, cls).__new__(cls)
            print(f'Criando o objeto: {cls.instance}')
        return cls.instance


s1 = Singleton()
print(f'Instância 1: {id(s1)}')

s2 = Singleton()
print(f'Instância 2: {id(s2)}')