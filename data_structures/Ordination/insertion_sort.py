def insertion_sort(a_list):
    for i in range (1, len(a_list)):
        value = a_list[i]

        while i > 0 and a_list[i - 1] > value:
            a_list[i] = a_list[i -1]
            i = i -1 
        a_list[i] = value
        
    return a_list