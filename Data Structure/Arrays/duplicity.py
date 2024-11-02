a_set = set()
a_set.add("Kanye West")
a_set.add("Kendall Jenner")
a_set.add("Kendall Jenner")
a_set.add("Justin Bieber")
print(a_set)


def return_dups(an_iterable):
    
    dups = []
    a_set = set()

    for item in an_iterable:
        l1 = len(a_set)
        a_set.add(item)
        l2 = len(a_set)

        if l1 == l2:
            dups.append(item)
    
    return dups


a_list = [
    "Susan Adams",
    "Kwame Goodall",
    "Jill Hampton",
    "Susan Adams"]


if __name__ == "__main__":
    dups = return_dups(a_list)
    print(dups)