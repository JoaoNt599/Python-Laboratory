# Exemplo simples

numbers = [1,2,3]

for n in numbers:
    print(n)

# An iterator needs to implement two methods:
#__iter__()s
#__next__()

# Simple Interator:

class Counter:
    def __init__(self, limit):
        self.limit = limit
        self.present = 1
    
    def __iter__(self):
        return self
    
    def __next__(self):
        if self.present > self.limit:
            raise StopIteration
        
        value = self.present
        self.present += 1
        return value


counter = Counter(6)

for n in counter:
    print(f"Counter: {n}")

