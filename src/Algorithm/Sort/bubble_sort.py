def bubble_sort (array: list) -> list : 

    n = len(array)
    
    for i in range (n-1, 0, -1) :
        for j in range (i) :
            if (array[j] > array[j+1]) :
                array[j], array[j+1] = array[j+1], array[j]


    
if (__name__ == "__main__") : 
    array = list(map(str, input("Enter items separated by spaces \n").split()))

    bubble_sort(array)

    print(f"Sorted List")
    print(*array)
