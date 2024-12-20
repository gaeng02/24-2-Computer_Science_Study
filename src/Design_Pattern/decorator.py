class Component :
    def operation (self) :
        return "Component"

class Decorator (Component) :
    def __init__ (self, component) :
        self._component = component

    def operation (self) :
        return f"Decorator({self._component.operation()})"

class DecoratorA (Decorator) :
    def operation (self) :
        return f"DecoratorA({self._component.operation()})"

class DecoratorB (Decorator) :
    def operation (self) :
        return f"DecoratorB({self._component.operation()})"

if (__name__ == "__main__") :

    component = Component()
    
    decorated = Decorator(component)
    print(decorated.operation())
    
    decorated_A = DecoratorA(component)
    print(decorated_A.operation())
    
    decorated_B = DecoratorB(decorated_A)
    print(decorated_B.operation())
