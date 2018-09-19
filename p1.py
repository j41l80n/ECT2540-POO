# # from celula import *
# import celula
import random

class Carro:
	def __init__(self, modelo='', placa=''):
		self.__modelo = modelo
		self.__placa = placa

		if self.__placa == '':
			self.__placa = self.__gerar_placa()

	def get_placa(self):
		return self.__placa

	def set_placa(self, placa):
		self.__placa = placa

	def get_modelo(self):
		return self.__modelo

	def set_modelo(self, modelo):
		self.__modelo = modelo

	def __gerar_placa(self):
		placa = []
		for i in range(4):
			placa.append(random.randint(0, 9))
		return placa

	modelo = property(get_modelo, set_modelo)
	placa = property(get_placa, set_placa)


class Patio:
	def __init__(self, nome='', capacidade=0):
		self.__nome = nome
		self.__capacidade = capacidade
		self.__quantidade_estacionado = 0
		self.__estacionados = []

		if self.__nome == '':
			self.__nome = 'patio'

	def get_nome(self):
			return self.__nome

	def set_nome(self, nome):
		self.__nome = nome

	def get_capacidade(self):
			return self.__capacidade

	def entrada_carro(self, Carro):
		if self.__quantidade_estacionado >= self.__capacidade:
			print('não pode estacionar')
		else:
			print('pode estacionar')
			self.__estacionados.append(Carro)
			self.__quantidade_estacionado+=1

	def saida_carro(self, placa):
		if c in self.__estacionados:
			self.__estacionados.remove(c)
			self.__quantidade_estacionado -= 1
		else:
			print('carro não encontrado')
	def carros_estacionados(self):
		pass

	def quantidade_estacionados(self):
		return self.__quantidade_estacionado 

	nome = property(get_nome, set_nome)
	capacidade = property(get_capacidade, None)
	quantidade_estacionados = property(quantidade_estacionados, None)

class Estacionamento:
	def __init__(self, patio=5):
		self.__patio = patio
		total_carros = 0

	def get_quantidade_carros(self):
		return total_carros

class TesteEstacionamento:
	def __init__(self):
		pass


#testes
if __name__ == "__main__":
	carro = Carro()
	carro2 = Carro()
	print(f'a placa do carro é {carro.placa}')

	patio = Patio()
	
	patio.nome = 'ect'
	patio.entrada_carro(carro)
	patio.entrada_carro(carro2)

	print(f'quantidade de carros estacionados {patio.quantidade_estacionados}.')
	print(patio.nome)
	print(patio.capacidade)