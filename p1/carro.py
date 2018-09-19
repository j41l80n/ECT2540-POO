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

carro = Carro()
carro2 = Carro()