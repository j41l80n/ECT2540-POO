class Lista:
	def __init__(self, capacidade=1):
		self.__dados = []
		self.__capacidade = capacidade
		self.__quantidade = 0

		# inicializa os dados como None
		self.__inicializa()

	def __inicializa(self):
		dados = [None] * capacidade
		
	def adiciona(self, object):
		if self.__capacidade == self.__quantidade:
			print('teste')
		else:
			dados[self.__capacidade-self.__quantidade] += object
			self.__quantidade += 1
		pass

	def get_objeto(self):
		return object
		# pass

	def eh_vazio(self):
		pass

	def remove(self):
		pass


	def imprime(self):
		pass

lista = Lista()
lista.adiciona(2)
print('fim do codigo')