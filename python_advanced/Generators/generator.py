def counter(limit):
    present = 1
    while present <= limit:
        yield present
        present += 1

for n in counter(7):
    print(f"Generator: {n}")