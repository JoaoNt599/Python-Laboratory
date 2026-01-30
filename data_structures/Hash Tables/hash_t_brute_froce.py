# list [1, 2, 3, 4, 7]
# target: 5

def two_sum_brute(the_list, target):
    index_list = []

    for i in range(0, len(the_list)):
        for j in range(i, len(the_list)):
            if the_list[i] + the_list[j] == target:
                return [the_list[i], the_list[j]]