def binary_search (elements: list, value: str) -> int : 

    low = 0; high = len(elements) - 1
    
    while (low <= high) :
        
        mid = (low + high) // 2
        
        if (value < elements[value]) : high = mid - 1
        elif (x > elements[value]) : low = mid + 1
        else : return mid
        
    return -1


if (__name__ == "__main__") : 
    try : 
        elements = list(map(str, input("Enter items separated by spaces \n").split()))
        value = input("Enter value you want to find \n")

        result = binary_search(elements, value)

        if (result >= 0) : print(f"Value is the elements[{result}].")
        else : print(f"Value is not in elements.")
    
    except : print(f"Wrong input")
