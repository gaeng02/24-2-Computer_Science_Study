def quick_sort (array: list) -> list : 

    n = len(array)
    _quick_sort(array, 0, n-1) 

def _quick_sort (array: list, low: int, high: int) -> list :
 
    if (low < high) :
        pivot = partition(array, low, high)
        _quick_sort(array, low, pivot-1)
        _quick_sort(array, pivot+1, high)

def partition (array: list, low: int, high: int) -> int :
  
    item = array[low]
    j = low
    for i in range (low+1, high+1) :
        if (array[i] < item) :
            j += 1
            array[i], array[j] = array[j], array[i]
    array[j], array[low] = array[low], array[j]
    return j


if (__name__ == "__main__") : 
    array = list(map(str, input("Enter items separated by spaces \n").split()))

    quick_sort(array)

    print(f"Sorted List")
    print(*array)
