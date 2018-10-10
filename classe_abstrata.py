from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def __init__(self):
        pass
        
    def nasce(self):
        print('nasci')
    
    def morre(self):
        print('morri')

    @abstractmethod
    def emite_som(self):
        pass

class Mamifero(Animal):
    @abstractmethod
    def __init__(self):
        # Animal.__init__(self):
        pass
    
    def amamenta(self):
        print('estou mamando')

class Ave(Animal):
    @abstractmethod
    def __init__(self):
        # Animal.__init__(self):
        pass

    def voa(self):
        print('estou voando')

class Gato(Mamifero):
    def __init__(self):
        pass
        
    def emite_som(self):
        return 'miau'

class Cachorro(Mamifero):
    def __init__(self):
        pass
        
    def emite_som(self):
        return 'auau'

class Ornitorrinco(Mamifero):
    def __init__(self):
        pass
        
    def emite_som(self):
        return 'adfsijo'

class Pinguim(Ave):
    def __init__(self):
        pass
        
    def emite_som(self):
        return 'fute fute'

class Aguia(Ave):
    def __init__(self):
        pass
        
    def emite_som(self):
        return 'ieeeem'

if __name__ == "__main__":
    gato = Gato()
    
    gato.nasce()
    print(gato.emite_som())
    gato.amamenta()
    print(gato.emite_som())
    gato.morre()
