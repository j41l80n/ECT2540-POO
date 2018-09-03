class Lista:
	def __init__(self, capacidade=1):
		self.__dados = []
		self.__capacidade = capacidade
		self.__quantidade = 0

		# inicializa os dados como None
		self.__inicializa()

	def __inicializa(self):
		self.__dados = [None] * self.__capacidade
		
	def adiciona(self, object):
		if self.__capacidade == self.__quantidade:
			print('teste')
		else:
			self.__dados[self.__quantidade] = object
			self.__quantidade += 1

	def eh_vazio(self):
		if self.__quantidade != 0:
			return False
		else:
			return True

	def get_objeto(self, posicao):
		if self.eh_vazio():
			return 'sem objetos'
		else:
			return self.__dados[posicao]

	def remove(self, posicao):
		for i in range(posicao, self.__quantidade-1):
			self.__dados[i] = self.__dados[i+1]

		self.__dados[self.__quantidade-1] = None
		self.__quantidade -= 1

	def imprime(self):
		# for dado in self.__dados:
		for i in range(0, self.__quantidade):
			print(self.__dados[i])

	def tamanho(self):
		i = 0
		for dado in self.__dados:
			i += 1
		return i

lista = Lista(3)

lista.adiciona('ufrn')
lista.adiciona('ect')
lista.adiciona('POO')
# print(lista.eh_vazio())

# print(lista.get_objeto(0))

lista.remove(1)
# print(lista.get_objeto(0))
# print(lista.get_objeto(1))

lista.imprime()
print(lista.tamanho())