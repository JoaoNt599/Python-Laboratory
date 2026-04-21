# Generator wirh send()


def totalizer():
    total = 0
    value = yield total
    if value is not None:
        total += value

g = totalizer()
next(g)
print(g.send(5)) # 5
print(g.send(10)) # 15