# -*- encoding: utf-8 -*-

import math
from abc import ABC, abstractmethod

class Poligono(ABC):
    @abstractmethod
    def __init__(self, tupla1=(), tupla2=()):
        """Classe abstrata Poligono"""
        ABC.__init__(self)
        self.__numero_lados = 3
        self._tupla1 = tupla1
        self._tupla2 = tupla2

    
    def distancia(tupla1, tupla2):
        """calcula a distancia entre dois pontos"""
        # d = ( ( (tupla1.index(0) - tupla2.index[0]) + (tupla1.index[1] - tupla2.index(0) ) ** 0.5)
        d = 10
        return d
    
    @abstractmethod
    def perimetro(self):
        """calcula o perimetro do polígono"""
        return 0
    
    @abstractmethod
    def area(self):
        """calcula a área do polígono"""
        pass

    @abstractmethod
    def imprimir_poligono(self):
        """imprime o polígono"""
        pass
    
    
    def eh_regular(self):
        """ verifica se o polígono é regular"""
        pass

class PoligonoRegular(Poligono):
    def __init__(self, tupla1, tupla2):
        """Classe PoligonoRegular"""
        Poligono.__init__(self, tupla1, tupla2)
    
    def perimetro(self):
        """calcula o perimetro do polígono"""
        return 

    def checa_poligono(self):
        pass
    
    def imprimir_poligono(self):
        """imprime o polígono"""
        pass

    def area(self):
        """calcula a área do polígono"""
        pass

    def __repr__(self):
        r = 'Poligono regular de n lados, lado igual a '
        return r

class TrianguloEquilatero(PoligonoRegular):
    def __init__(self, tupla1, tupla2):
        """Classe TrianguloEquilatero"""
        Poligono.__init__(self, tupla1, tupla2)


    def imprimir_poligono(self):
        """imprime o polígono"""
        pass

    def area(self):
        """calcula a área do polígono"""
        pass

    def __repr__(self):
        r = 'TrianguloEquilatero'
        return r

class Quadrado(PoligonoRegular):
    def __init__(self, tupla1, tupla2):
        """Classe Quadrado"""
        PoligonoRegular.__init__(self, tupla1, tupla2)
        self._lados = 4

    def imprimir_poligono(self):
        """imprime o polígono"""
        pass

    def area(self):
        """calcula a área do polígono"""
        pass

    def __repr__(self):
        r = f'Quadrado com lado igual a {self._lados}.'
        return r

"""
POO 2018.2: segunda avaliacao
"""

if __name__ == "__main__":
    t1 = TrianguloEquilatero((5.0, 5.0), 2)
    print(t1)
    print(">Perimetro: {}".format(t1.perimetro()))
    print(">Area: {}".format(t1.area()))
    t2 = TrianguloEquilatero((0.0, -2.0), 3)
    print(t2)
    print(">Perimetro: {}".format(t2.perimetro()))
    print(">Area: {}".format(t2.area()))
    q1 = Quadrado((10.0, 10.0), 4)
    print(q1)
    print(">Perimetro: {}".format(q1.perimetro()))
    print(">Area: {}".format(q1.area()))
    p1 = PoligonoRegular((-10.0, -10.0), (7,7,7,7,7))
    print(p1)
    print(">Perimetro: {}".format(p1.perimetro()))
    print(">Area: {}".format(p1.area()))
    print("Distancia entre o quadrado e o pentagono: {}".format(Poligono.distancia(q1, p1)))
