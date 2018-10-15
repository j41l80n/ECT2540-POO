# -*- coding: utf-8 -*-
from abc import ABC, abstractmethod

class Usuario:
    def __init__(self, nome='', local_trabalho=''):
        """inicializa o usuario"""
        self.__nome = nome
        self.__local_trabalho = local_trabalho

    @property
    def nome(self):
        """retorna nome do usuario"""
        return self.__nome

    @nome.setter
    def nome(self, nome):
        """seta nome do usuario"""
        self.__nome = nome

    @property
    def local_trabalho(self):
        """retorna local de trabalho do usuario"""
        return self.__local_trabalho

    @local_trabalho.setter
    def local_trabalho(self, local_trabalho):
        """seta local de trabalho do usuario"""
        self.__local_trabalho = local_trabalho


    def __repr__(self):
        """representação do usuario"""
        r = f'{self.__nome} esta em: {self.__local_trabalho}'
        return r
        
class Recurso(ABC):
    @abstractmethod
    # def __init__(self, nome, numero_tarefas, esta_ocupado, usuario):
    def __init__(self, nome):
        self.__nome = nome
        self.__numero_tarefas = 0
        self.__esta_ocupado = False
        self.__usuario = None

    @property
    def nome(self):
        """retorna nome do recurso"""
        return self.__nome

    @nome.setter
    def nome(self, nome):
        """seta nome do recurso"""
        self.__nome = nome

    # @property
    # def numero_tarefas(self):
    #     """retorna numero de tarefas"""
    #     return self.__numero_tarefas

    # @numero_tarefas.setter
    # def numero_tarefas(self, numero_tarefas):
    #     """seta numero de tarefas"""
    #     self.__numero_tarefas = numero_tarefas


    @property
    def esta_ocupado(self):
        """retorna se esta ocupado"""
        return self.__esta_ocupado

    @esta_ocupado.setter
    def esta_ocupado(self, esta_ocupado):
        """seta se esta ocupado"""
        self.__esta_ocupado = esta_ocupado


    @property
    def usuario(self):
        """retorna usuario do recurso"""
        return self.__usuario

    @usuario.setter
    def usuario(self, usuario):
        """seta usuario do recurso"""
        self.__usuario = usuario

    def reserva(self, usuario, numero_tarefas):
        self.__usuario = usuario
        self.__numero_tarefas = numero_tarefas

        if self.__esta_ocupado:
            print('recurso não disponível')
        else:
            print(f'Recurso {self.__nome} solicitado por {self.__usuario.nome} para {self.__numero_tarefas} tarefas.')
            print(f'> Recurso reservado')
            self.__esta_ocupado = True
        

    @abstractmethod
    def processa(self):
        print(f'{self.__nome} está sendo utilizado por {self.__usuario.nome} por {self.__numero_tarefas} vezes.')
        self.__numero_tarefas -= 1

    def libera(self):
        self.__numero_tarefas = 0
        
    @abstractmethod
    def __repr__(self):
        r = f'Recurso: {self.__nome}, Tarefas: {self.__numero_tarefas}, Ocupado: {self.__esta_ocupado}, Tipo: '
        return r

class Impressora(Recurso):
    def __init__(self, nome):
        Recurso.__init__(self, nome)
        self.__nome = nome    

    def processa(self):
        print(f'{self.__nome} está sendo utilizado por {self.__usuario.nome} por {self.__numero_tarefas} vezes.')
        print(f'> tarefa processada')
        self.__numero_tarefas -= 1

    def __repr__(self):
        r = Recurso.__repr__(self)
        r += 'impressora'
        return r   
        
class Cafeteira(Recurso):
    def __init__(self, nome):
        Recurso.__init__(self, nome)
        # self.__nome = nome
        
    def processa(self):
        print('teste')
        print(f'{self.__nome} está sendo utilizado por {self.__usuario.nome} por {self.__numero_tarefas} vezes.')
        print('>Fazendo cafe')
        self.__numero_tarefas -= 1

    def __repr__(self):
        r = Recurso.__repr__(self)
        r += 'cafefeira'
        return r

if __name__ == '__main__':
    usuario1 = Usuario('alice', 'cozinha')
    usuario2 = Usuario('bernardo', 'sala')
    impressora = Impressora('impressora-escritorio')
    cafeteira = Cafeteira('cafeteira-copa')
    print(usuario1)
    print(usuario2)
    # impressora.numero_tarefas = 2
    # impressora.reserva(usuario1, impressora.numero_tarefas)
    # impressora.processa()
    # impressora.processa()
    print(cafeteira)
    print('==============================================')
    print(impressora)
    print('==============================================')
    cafeteira.reserva(usuario1, 3)
    print(cafeteira)
    print('==============================================')
    cafeteira.processa()
    # cafeteira.reserva(usuario2, 3)