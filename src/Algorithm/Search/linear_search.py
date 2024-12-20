def linear_search (elements: list, value: str) -> int : 

    for index in range (len(elements)) : 
        if (elements[index] == value) : 
            return index
        
    return -1


if (__name__ == "__main__") : 
    try : 
        elements = list(map(str, input("Enter items separated by spaces \n").split()))
        value = input("Enter value you want to find \n")

        result = linear_search(elements, value)

        if (result >= 0) : print(f"Value is the elements[{result}].")
        else : print(f"Value is not in elements.")
    
    except : print(f"Wrong input")
