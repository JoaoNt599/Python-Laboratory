# Generator Lazy infinity:


def infinity():
    i = 0
    while True:
        yield i
        i += 1

for  n in infinity():
    if n == 5:
        break
    print(f"Lazy Infinity: {n}")