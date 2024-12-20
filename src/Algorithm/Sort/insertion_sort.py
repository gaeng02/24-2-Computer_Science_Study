def insection_sort (array: list) -> list : 

    n = len(array)
    
    for i in range (1, n) :
        for j in range (i, 0, -1) :
            if (array[j-1] > array[j]) :
                array[j-1], array[j] = array[j], array[j-1]
                
            else : break


if (__name__ == "__main__") : 
    array = list(map(str, input("Enter items separated by spaces \n").split()))

    insection_sort(array)

    print(f"Sorted List")
    print(*array)
