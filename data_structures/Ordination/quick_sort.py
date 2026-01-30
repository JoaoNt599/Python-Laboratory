def partition(array, low, high):

    pivot = array[high]
    i = low -1

    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1

            (array[i], array[j]) = (array[j], array[i])
    
    (array[i + 1], array[high]) = (array[high], array[i + 1])

    return i + 1

def quick_sort(array, low, high):
    if low < high:
        p = partition(array, low, high)
        quick_sort(array, low, p - 1)
        quick_sort(array, p + 1, high)

if __name__ == "__main__":
    data = [3, 6, 24, 46, 7, 2]
    print(data)
    size = len(data)
    quick_sort(data, 0, size - 1)
    print(data)

