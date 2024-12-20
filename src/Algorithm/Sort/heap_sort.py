def heapify (array: list, index: int, size: int) -> list :
    largest = index
    left = 2 * index + 1
    right = 2 * index + 2

    if ((size > left) and (array[left] > array[largest])) : largest = left
    if ((size > right) and (array[right] > array[largest])) : largest = right
    if (largest != index) :
        array[index], array[largest] = array[largest], array[index]
        heapify(array, largest, size)    
    

def heap_sort (array: list) -> list : 

    n = len(array)
    for index in range (n//2 -1, -1, -1) : heapify(array, index, n)
    for index in range (n-1, 0, -1) :
        array[0], array[index] = array[index], array[0]
        heapify(array, 0, index)

    
if (__name__ == "__main__") : 
    array = list(map(str, input("Enter items separated by spaces \n").split()))

    heap_sort(array)

    print(f"Sorted List")
    print(*array)
