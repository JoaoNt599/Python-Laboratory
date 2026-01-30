# Multiple iterables

numbers1 = [1,2,3]
numbers2 = [10, 20,30]

result = list(map(lambda a, b: a + b, numbers1 + numbers2))

print(result)