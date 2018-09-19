import carro

class Patio:
	def __init__(self, nome='', capacidade=0):
		self.__nome = nome
		# basta aumentar a capacidade > 0 para poder estacionar carros
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



patio = Patio()
patio.nome = 'ect'
patio.entrada_carro(carro.carro)
patio.entrada_carro(carro.carro2)

print(f'quantidade de carros estacionados {patio.quantidade_estacionados}.')
print(patio.nome)
print(patio.capacidade)