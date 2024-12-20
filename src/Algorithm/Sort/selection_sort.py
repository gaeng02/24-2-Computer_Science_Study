def selection_sort (array: list) -> list : 

    n = len(array)
    
    for i in range (n) :
        min_index = i
        
        for j in range (i+1, n) :
            if (array[min_index] > array[j]) :
                min_index = j

        array[i], array[min_index] = array[min_index], array[i]


    
if (__name__ == "__main__") : 
    array = list(map(str, input("Enter items separated by spaces \n").split()))

    selection_sort(array)

    print(f"Sorted List")
    print(*array)
