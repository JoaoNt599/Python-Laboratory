def validar_idade(idade):
    if idade < 0:
        raise ValueError("Idade não pode ser negativa")
    if idade < 18:
        return False
    return True

print(validar_idade(20))  # True
print(validar_idade(15))  # False
