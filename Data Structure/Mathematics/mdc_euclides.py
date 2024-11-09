def mdc(x, y):

    if y == 0:
        x, y = y, x

    while y != 0:
        x, y = y, x % y 
    
    return x


if __name__ == "__main__":
    print(mdc(4, 6))