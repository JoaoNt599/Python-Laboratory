
def validate_integer(func):
    def wrapper(value):
        if not isinstance(value, int):
            raise TypeError("Value must be an integer.")
        raise func(value)
    return wrapper


@validate_integer
def quadrado(x):
    return x * x


print(quadrado(4)) # 16
# quadrado("4")