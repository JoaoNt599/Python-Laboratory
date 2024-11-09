this_weeks_winners = [2, 43, 48, 62, 64, 28, 3]
most_common_winners = [1, 28, 42, 70, 2, 10, 62, 31, 4, 14]


def return_inter(list1, list2):

    list3 = [v for v in list1 if v in list2]
    return list3


if __name__ == "__main__":
    list1 = [2, 43, 48, 62, 64, 28, 3]
    list2 = [1, 28, 42, 70, 2, 10, 62, 31, 4, 14]
    print(return_inter(list1, list2))


# or


def return_inter(list1, list2):
    
    set1 = set(list1)
    set2 = set(list2)
    return list(set1.intersection(set2))


if __name__ == "__main__":
    list1 = [2, 43, 48, 62, 64, 28, 3]
    list2 = [1, 28, 42, 70, 2, 10, 62, 31, 4, 14]
    new_list = return_inter(list1, list2)
    print(new_list)