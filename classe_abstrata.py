from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    pass

class Mamifero(Animal):
    @abstractmethod
    pass
class Ave(Animal):
    @abstractmethod
    pass

class Gato(Mamifero):
    pass
class Cachorro(Mamifero):
    pass

class Ornitorrinco(Mamifero):
    pass

class Pinguim(Ave):
    pass

class Aguia(Ave):
    pass