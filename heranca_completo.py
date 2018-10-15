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
    def __init__(self, nome, cpf, salario):
        Pessoa.__init__(self, nome, cpf)
        self._salario = salario

    @property
    def salario(self):
        return self._salario
    
    @salario.setter
    def salario(self, m):
        self._salario = m

    def __repr__(self):
        s = Pessoa.__repr__(self)
        return s + ', salario: {}'.format(self.salario)

class Gerente(Funcionario):
    def __init__(self, nome, cpf, salario, bonus):
        Funcionario.__init__(self, nome, cpf, salario)
        self._bonus = bonus

    @property
    def bonus(self):
        return self._bonus
    
    @bonus.setter
    def bonus(self, b):
        self._bonus = b

    def __repr__(self):
        s = Pessoa.__repr__(self)
        return s + ', salario: {}'.format(self.salario*(1.0 + self.bonus))

if __name__ == "__main__":
    p1 = Pessoa('joao', 111222)
    print(p1)
    f1 = Funcionario('joaquim', 123456, 1000)
    print(f1)
    g1 = Gerente('amanda', 543210, 2000, 0.2)
    print(g1)
    print('Instancias da classe base: {}'.format(Pessoa.num_instancias()))
    print(isinstance(g1, Pessoa))
    print(isinstance(g1, Funcionario))
    print(isinstance(g1, Gerente))
    print(isinstance(p1, Gerente))