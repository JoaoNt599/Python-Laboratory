# Generator Expression

gen = (x * 2 for x in range(5))
print(next(gen)) # 0 
print(next(gen)) # 2