class User:
    def  __init__(self, name):
        self.name = name


users = [User("Ana"), User("Maria")]

names = list(map(lambda u: u.name, users))

print(names)