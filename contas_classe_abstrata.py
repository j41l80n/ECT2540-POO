# -*- encoding: utf-8 -*-
from abc import ABC, abstractmethod
import math

class Conta(ABC):
    @abstractmethod
    def __init__(self, ag, num, titular):
        ABC.__init__(self)
        self._ag = ag
        self._num = num
        self._titular = titular
        self._saldo = 0.0

    def __repr__(self):
        s = 'Titular: {}\n'.format(self._titular)
        s += 'Ag: {}, Num: {}\n'.format(self._ag, self._num)
        s += 'Saldo: R${}'.format(self._saldo)
        return s

    def saque(self, valor):
        self._saldo -= valor
        print('Saque de R${} realizado com sucesso'.format(valor))
        if self._saldo < 0:
            print('Conta com saldo negativo')

    def deposito(self, valor):
        self._saldo += valor
        print('Deposito de R${} realizado com sucesso'.format(valor))

class ContaCorrente(Conta):
    def __init__(self, ag, num, titular):
        Conta.__init__(self, ag, num, titular)

    def __repr__(self):
        s = 'Conta Corrente\n'
        s += Conta.__repr__(self)
        return s

class ContaPoupanca(Conta):
    def __init__(self, ag, num, titular):
        Conta.__init__(self, ag, num, titular)

    def __repr__(self):
        s = 'Conta Poupanca\n'
        s += Conta.__repr__(self)
        return s

    def saque(self, valor):
        if self._saldo >= valor + 2.0:
            self._saldo -= (valor + 2.0)
            print('Saque de R${} realizado com sucesso'.format(valor))
            print('Cobrada taxa de R$2')
        else:
            print('Saldo insuficiente')

    def rende(self):
        self._saldo = math.ceil(self._saldo*1.0095)

if __name__ == "__main__":
    c2 = ContaCorrente(1, 11, 'jose')
    print(c2)

    c3 = ContaPoupanca(2, 11, 'maria')
    print(c3)