import string

def cipher(a_string, key):
    uppercase = string.ascii_uppercase
    lowercase = string.ascii_lowercase
    encrypt = ''

    for i in a_string:
        if i in uppercase:
            new = (uppercase.index(i) + key) % 26
            encrypt += uppercase[new]
        elif i in lowercase:
            new = (lowercase.index(i) + key) % 26
            encrypt += lowercase[new]
        else:
            encrypt += i
    
    return encrypt