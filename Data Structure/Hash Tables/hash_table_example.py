def count(a_string):
    a_dict = {}

    for char in a_string:
        if char in a_dict:
            a_dict[char] += 1
        else:
            a_dict[char] = 1
        
        print(a_dict)