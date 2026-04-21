# Validação com regex (formato)

import re

def validate_email(email):
    default = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    if not re.match(default, email):
        raise ValueError("Invalid email address")
    return True

validate_email("joao@gmail.com")   # OK
#validate_email("joao@gmail")       # erro
