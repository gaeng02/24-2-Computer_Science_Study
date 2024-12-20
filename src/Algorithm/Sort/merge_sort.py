def merge_sort (array: list) -> list : 

    n = len(array)
    
    if (n == 1) : return ;

    m = n // 2
    left = array[ : m]
    right = array[m : ]

    merge_sort(left)
    merge_sort(right)
    merge(m, n-m, left, right, array)

def merge (l, r, left, right, array) :

    l, r = l - 1, r - 1
    i, j, k = 0, 0, 0
    
    while ((i <= l) and (j <= r)) :
        if (left[i] < right[j]) : 
            array[k] = left[i]
            i += 1
        elif (left[i] >= right[j]) :
            array[k] = right[j]
            j += 1
        k += 1
        
    while (i <= l) :
        array[k] = left[i]
        i += 1
        k += 1

    while (j <= r) :
        array[k] = right[j]
        j += 1
        k += 1 


if (__name__ == "__main__") : 
    array = list(map(str, input("Enter items separated by spaces \n").split()))

    merge_sort(array)

    print(f"Sorted List")
    print(*array)
