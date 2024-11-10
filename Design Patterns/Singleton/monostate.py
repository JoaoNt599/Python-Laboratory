

class Monostate:

    __estado = {}

    def __new__(cls, *args, **kwargs):
        obj = super(Monostate, cls).__new__(cls, *args, **kwargs)
        obj.__dict__ = cls.__estado
        return obj


m1 = Monostate()
print(f'M1 ID: {id(m1)}')
print(m1.__dict__)

m2 = Monostate()
print(f'M2 ID: {id(m2)}')
print(m2.__dict__)

m1.nome = 'Felicity'

print(f'M1: {m1.__dict__}')
print(f'M2: {m2.__dict__}')