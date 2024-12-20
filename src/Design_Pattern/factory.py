from abc import ABC, abstractmethod

# Product Interface
class Phone (ABC) :
    @abstractmethod
    def specifications (self) -> str :
        pass

# Concrete Product
class Apple (Phone) :
    def specifications (self) -> str :
        return "Apple iPhone"

class Samsung (Phone) :
    def specifications (self) -> str :
        return "Samsung Galaxy"

# Creator Interface
class PhoneFactory (ABC) :
    @abstractmethod
    def create_phone (self) -> Phone :
        pass

# Concreate Creator
class AppleFactory (PhoneFactory) :
    def create_phone (self) -> Phone :
        return Apple()


class SamsungFactory (PhoneFactory) :
    def create_phone (self) -> Phone :
        return Samsung()


if (__name__ == "__main__") :

    apple = AppleFactory().create_phone()
    print(f"Created : {apple.specifications()}")

    samsung = SamsungFactory().create_phone()
    print(f"Created : {samsung.specifications()}")
