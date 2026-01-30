def fibonacci(n: int) -> int:
    if n in {0, 1}:
        return n
    return fibonacci(n - 1) + fibonacci(n - 2)


# example:
if __name__ == "__main__":
    print(fibonacci(10))