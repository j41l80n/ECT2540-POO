class Conta:
    def __init__(self, numero_conta, saldo):
        self.__numero_conta = numero_conta
        self.__saldo = saldo
    
    def saque(self):
        pass

    def deposito(self):
        pass
    
class ContaCorrente(Conta):
    def __init__(self, numero_conta, saldo, plano):
        Conta.__init__(self, numero_conta, saldo)
        self.__plano = plano
    
class ContaPoupanca(Conta):
    def rende(self):
        pass