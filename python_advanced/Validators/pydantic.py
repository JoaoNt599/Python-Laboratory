from pydantic import BaseModel, EmailStr


class User(BaseModel):
    name: str
    email: EmailStr
    age: int

    @classmethod
    def validate_age(cls, age):
        if age < 18:
            raise ValueError("Menor de idade")


User(name="João", email="joao@gmail.com", age=25)
