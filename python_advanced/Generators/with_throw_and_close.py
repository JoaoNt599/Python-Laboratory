# Generator with throw() and close()


def example():
    try:
        while True:
            yield "Running"
    except GeneratorExit:
        print("Close generator")

g = example()
print(next(g))
g.close()