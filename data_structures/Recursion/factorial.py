def factorial(n: int) -> int:
    if n == 0:
        return 1
    return n * factorial(n - 1)


# example:
if __name__ =="__main__":
    fact = factorial(5)
    print(fact)