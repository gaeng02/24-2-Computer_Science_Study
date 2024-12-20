def change (money : int) -> None :
    '''
    
    '''
    
    coin = [500, 100, 50, 10]
    count = [0, 0, 0, 0]
    
    for i in range (len(coin)) :
        count[i] = money // coin[i]
        money %= coin[i]

    for i in range (len(coin)) : 
        print(f"{coin[i]}원 : {count[i]}개")
        
    print(f"Total : {sum(count)}")
   
if (__name__ == "__main__") :
    change(1960)
