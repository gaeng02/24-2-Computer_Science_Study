# client interface
class Target : 
    def request (self) :
        return "Target"

# redefined interface
class Adaptee :
    def request (self) :
        return "Adaptee"

# connect interface
class Adapter (Target) :
    def __init__ (self, adaptee) :
        self.adaptee = adaptee

    def request (self) :
        return f"Adapter : {self.adaptee.request()}"


if (__name__ == "__main__") :

    adaptee = Adaptee()
    adapter = Adapter(adaptee)
    print(adapter.request())
