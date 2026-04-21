# Generators with yield from


def numbers():
    for n in [1,2,3]:
        yield n

def spell():
    yield from "abc"

def all():
    yield from numbers()
    yield from  spell()