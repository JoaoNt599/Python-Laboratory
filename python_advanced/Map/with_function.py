# Map with function

def square(n):
    return n * n


numbers = [2,3,4]

result = map(square, numbers)

print(list(result))