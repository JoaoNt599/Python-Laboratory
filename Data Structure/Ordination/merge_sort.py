def merge_sort(a_list):

    if len(a_list) > 1:
        mid = len(a_list) // 2
        left_falf = a_list[:mid]
        right_half = a_list[:mid]
        merge_sort(left_falf)
        merge_sort(right_half)

        left_ind = 0
        right_ind = 0
        alist_ind = 0

        while left_ind < len(left_falf) and right_ind < len(right_half):
            if left_falf[left_ind] <= right_half[right_ind]:
                a_list[alist_ind] = left_falf[left_ind]
                left_ind += 1
            else:
                a_list[alist_ind] = right_half[right_ind]
                right_ind += 1
            alist_ind += 1

        while left_ind < len(left_falf):
            a_list[alist_ind] = left_falf[left_ind]
            left_ind += 1
            alist_ind += 1

        while right_ind < len(right_half):
            a_list[alist_ind] = right_half[right_ind]
            right_ind += 1
            alist_ind += 1