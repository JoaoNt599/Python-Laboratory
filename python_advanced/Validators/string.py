# Validação de string (vazio, tamanho, formato simples)

def validate_name(name):
    if not name:
        raise ValueError("Name cannot be empty")
    if len(name) < 3:
        raise ValueError("Name must be at least 3 characters long")
    return True


validate_name("Joe")