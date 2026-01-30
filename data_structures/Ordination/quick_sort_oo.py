class QuickSort:

    def __init__(self, numbers:'List of numbers') -> None:
        self.__numbers = numbers
        self.__orders()

    def __orders(self) -> None:
        self.__partitions(self.__numbers, 0 , len(self.__numbers) - 1)

    def __partitions(self, numbers:'List of numbers', start: int, end: int) -> None:
        if end - start > 0:
            pivot, left, right = self.__numbers[start], start, end

            while left <= right:
                while self.__numbers[left] < pivot:
                    left += 1
                while self.__numbers[right] > pivot:
                    right -= 1
                
                if left <= right:
                    self.__numbers[left], self.__numbers[right] = self.__numbers[right], self.__numbers[left]
                    left += 1
                    right -= 1
            
            self.__partitions(self.__numbers, start, right)
            self.__partitions(self.__numbers, left, end)

    @property
    def result(self) -> 'List of numbers':
        return self.__numbers 

# example:
    
"""
>>> from quick_sort_oo import QuickSort
>>> l = [10, 4, 6, 32, 7]
>>> print(l)
>>> qs = QuickSort(l)
>>> print(qs.result)
"""