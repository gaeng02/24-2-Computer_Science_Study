def exchange_sort (array: list) -> list : 

    n = len(array)
    
    for i in range (n) :
        for j in range (i+1, n) :
            if (array[i] > array[j]) :
                array[i], array[j] = array[j], array[i]

    
if (__name__ == "__main__") : 
    array = list(map(str, input("Enter items separated by spaces \n").split()))

    exchange_sort(array)

    print(f"Sorted List")
    print(*array)
