from abc import ABC, abstractmethod

class Superclasse1:
    def __init__(self, valor):
        self.atrib_super1 = valor

    def metodo_super1(self):
        print('Metodo super1')

class Superclasse2(ABC):
    def __init__(self, valor):
        self.atrib_super2 = valor

    @abstractmethod
    def metodo_super2(self):
        print('Metodo super2')

class Subclasse(Superclasse1, Superclasse2):
    def __init__(self, valor):
        Superclasse1.__init__(self, 0) # atribui 0 a atrib_super1
        Superclasse2.__init__(self, 1) # atribui 1 a atrib_super2
        self.atrib_sub = valor

    def metodo_sub(self):
        print('Metodo sub')

    def metodo_super2(self):
        print('Metodo super2')

if __name__ == "__main__":
    obj = Subclasse(50)
    print(obj.atrib_super1)
    print(obj.atrib_super2)
    print(obj.atrib_sub)
    obj.metodo_super1()
    obj.metodo_super2()
    obj.metodo_sub()