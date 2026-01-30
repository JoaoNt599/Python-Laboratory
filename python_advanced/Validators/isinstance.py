
def validar_numero(valor):
    if not isinstance(valor, int):
        raise TypeError("Value must be an integer")
    return True

validar_numero(10)    # OK
validar_numero("10") # erro
