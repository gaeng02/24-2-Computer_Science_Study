class Subject :
    def __init__ (self) :
        self._observers = []

    def attach (self, observer) :
        self._observers.append(observer)

    def notify (self, message) :
        for observer in self._observers :
            observer.update(message)

class Observer :
    def update (self, message) :
        print(f"Observer notified : {message}")


if (__name__ == "__main__") :

    subject = Subject ()
    o1 = Observer()
    o2 = Observer()

    subject.attach(o1)
    subject.attach(o2)

    subject.notify("Interrupted") 
