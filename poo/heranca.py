# -*- coding: utf-8 -*-

class Pessoa:
    instancias = []

    def __init__(self, nome, cpf):
        self._nome = nome
        self._cpf = cpf
        Pessoa.instancias.append(self)

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, n):
        self._nome = n

    @property
    def cpf(self):
        return self._cpf

    @cpf.setter
    def cpf(self, c):
        self._cpf = c

    @staticmethod
    def num_instancias():
        return len(Pessoa.instancias)

    def se_apresenta(self):
        print('Ola, meu nome e {}, meu CPF e {}'.format(self._nome, self._cpf))

    def __repr__(self):
        return 'Nome: {}, CPF: {}'.format(self._nome, self._cpf)

class Funcionario(Pessoa):
    pass

class Gerente(Funcionario):
    pass

if __name__ == "__main__":
    p1 = Pessoa('joao', 111222)
    print(p1)