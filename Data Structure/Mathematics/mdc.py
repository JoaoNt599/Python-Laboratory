def mdc(i1, i2):

    mdc = None

    if i1 < 0 or i2 < 0:
        raise ValueError("Numbers must be positive.")

    if i1 > i2:
        smaller = i2
    else:
        smaller = i1

    for divisor in range(1, smaller + 1):
        if(i1 % divisor == 0) and (i2 % divisor == 0):
            mdc = divisor
    
    return mdc


if __name__ == "__main__":
   print(mdc(2, 20))