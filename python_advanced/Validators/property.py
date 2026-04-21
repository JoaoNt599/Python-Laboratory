
class User():
    def __init__(self, email):
        self.email = email
    

    @property
    def email(self):
        return self._email
    
    @email.setter
    def email(self, value):
        if "@" not in value:
            raise ValueError("Emaiil is not valid")
        self._email = value


u = User("joao@gmail.com")
# u.email = "invalido"  # error