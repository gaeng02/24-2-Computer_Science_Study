class Singleton :
    _instance = None

    def __new__ (cls) :
        
        print("__new__ is called \n") 
        
        if not cls._instance :
            cls._instance = super().__new__(cls)
            print("Instance is created \n")

        else : print("Instance is already called \n")
        
        return cls._instance

    def __init__ (self) :
        
        print("__init__ is called")
        

if (__name__ == "__main__") :

    s1 = Singleton()
    s2 = Singleton()

    print(s1 is s2)
