# -*- coding: utf-8 -*-

class Matriz:
    """
    Modela uma matriz de tamanho nl x nc
    de números reais.
    """
    def __init__(self, nl, nc):
        self._nl = nl
        self._nc = nc
        self._dados = []
        self._inicializa()

    @property
    def nl(self):
        return self._nl
    
    @property
    def nc(self):
        return self._nc

    def _inicializa(self):
        for i in range(self._nl):
            self._dados.append([])
            for j in range(self._nc):
                self._dados[i].append(0.0)

    def __getitem__(self, pos):
        """
        Obtém o elemento na linha l e coluna c
        da matriz da forma A[l,c]
        (ou seja, pos é uma tupla: pos = (i,j)).
        """
        if type(pos) != tuple:
            print('pos deve ser do tipo tuple')
        else:
            l, c = pos
            if l >= self._nl or c >= self._nc:
                print('indice fora da matriz')
            else:
                return self._dados[l][c]

    def __setitem__(self, pos, v):
        """
        Atribui o elemento na linha l e coluna c
        da matriz da forma A[l,c] = v
        (ou seja, pos é uma tupla: pos = (i,j)).
        """
        if type(pos) != tuple:
            print('pos deve ser do tipo tuple')
        else:
            l, c = pos
            if l >= self._nl or c >= self._nc:
                print('indice fora da matriz')
            else:
                self._dados[l][c] = v

    def __repr__(self):
        """
        Escreve a matriz na tela em formato de String.
        """
        res = ''
        for i in range(a.nl):
            for j in range(a.nc):
                res += f'{self._dados[i][j]} '
            res += '\n'
        return res

    def _checa_dimensoes(self, matriz_b):
        """
        Checa se as dimensões das matrizes são iguais.
        """
        if self._nl != matriz_b._nl or self._nc != matriz_b._nc:
            return False
        else:
            return True

    def __add__(self, matriz):
        """
        Soma duas matrizes.
        """
        if type(matriz) != Matriz:
            res = 'tipo de dados incompatível. Insira uma Matriz'
        elif self._checa_dimensoes(matriz):
            res = ''
            for i in range(a.nl):
                for j in range(a.nc):
                   res += f'{self._dados[i][j] + matriz._dados[i][j]} '
                res += '\n'
        else:
            res = 'O tamanho das matrizes são incompatíveis.'
        return res

    def __iadd__(self, matriz):
        """
        Adição de Matrizes.
        """
        if type(matriz) != Matriz:
            res = 'tipo de dados incompatível. Insira uma Matriz'
        elif self._checa_dimensoes(matriz):
            for i in range(a.nl):
                for j in range(a.nc):
                   self._dados[i][j] += self._dados[i][j] + matriz._dados[i][j]
        else:
            res = 'O tamanho das matrizes são incompatíveis.'
        return self

    def __sub__(self, matriz):
        """
        Subtração de duas matrizes.
        """
        if type(matriz) != Matriz:
            res = 'tipo de dados incompatível. Insira uma Matriz'
        elif self._checa_dimensoes(matriz):
            res = ''
            for i in range(a.nl):
                for j in range(a.nc):
                   res += f'{self._dados[i][j] - matriz._dados[i][j]} '
                res += '\n'
        else:
            res = 'O tamanho das matrizes são incompatíveis.'
        return res

    def __isub__(self, matriz):
        """
        Subtração de duas matrizes.
        """
        if type(matriz) != Matriz:
            res = 'tipo de dados incompatível. Insira uma Matriz'
        elif self._checa_dimensoes(matriz):
            for i in range(a.nl):
                for j in range(a.nc):
                   self._dados[i][j] -= self._dados[i][j] - matriz._dados[i][j]
        else:
            res = 'O tamanho das matrizes são incompatíveis.'
        return self

    def __eq__(self, matriz):
        """
        Verifica Igualdade da Matriz.
        """
        if type(matriz) != Matriz:
            res = 'tipo de dados incompatível. Insira uma Matriz'
        elif self._checa_dimensoes(matriz):
            for i in range(a.nl):
                for j in range(a.nc):
                   if self._dados[i][j] != matriz._dados[i][j]:
                       return False 
            return True

if __name__ == "__main__":
    a = Matriz(3,3)
    a[1,1] = 50
    for i in range(a.nl):
        for j in range(a.nc):
            print("{} ".format(a[i,j]), end='')
        print('')

    b = Matriz(3,3)
    b[1,1] = 50

    print('\nOperador __repr__')
    print(a)

    print('\nOperador __add__')
    print(a+b)

    print('\nOperador __iadd__')
    a += a
    print(a)

    print('\nOperador __sub__')
    print(a-b)

    print('\nOperador __isub__')
    a-=b
    print(a)

    print('\nOperador __eq__')
    print(a==b)