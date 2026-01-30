def linear_search(a_list, n: int) -> int:
    for i in a_list:
        if i == n:
            return True
    return False
    
    
if __name__ == "__main__":
    a_list = [2, 23, 78, 3, 4, 7]
    print(linear_search(a_list, 7))