class ValidationError(Exception):
    pass


def validate_password(password):
    if len(password) < 8:
        raise ValidationError("The password must contain at least 8 characters")