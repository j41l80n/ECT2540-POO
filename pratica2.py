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
			print('erro')
		else:
			self.__dados[self.__quantidade] = object
			self.__quantidade += 1

	def get_objeto(self, posicao):
		if self.eh_vazio():
			return 'sem objetos'
		else:
			return self.__dados[posicao]

	def eh_vazio(self):
		if self.__quantidade != 0:
			return False
		else:
			return True

	def remove(self, posicao):
		for i in range(posicao, self.__quantidade-1):
			self.__dados[i] = self.__dados[i+1]

		self.__dados[self.__quantidade-1] = None
		self.__quantidade -= 1

	def imprime(self):
		if self.__dados[0] != None:
		# for dado in self.__dados:
			for i in range(0, self.__quantidade):
				print(self.__dados[i])
		else:
			print('sem dados a imprimir')

	def reseta(self):
		self.__inicializa()

	def copia(self):
		return self

	def inverte(self):
		listaInvertida = Lista(self.__quantidade)
		for i in range(self.__quantidade-1, -1, -1):
			listaInvertida.adiciona(self.__dados[i])
		return listaInvertida.imprime()

	def concatena(self, lista):
		listaConcatenada = Lista(self.__quantidade)
		for i in range(self.__quantidade-1):
			listaConcatenada.adiciona(lista.get_objeto())

	def tamanho(self):
		i = 0
		for dado in self.__dados:
			i += 1
		return i

lista1 = Lista(3)
lista2 = Lista()

lista1.adiciona('ufrn')
lista1.adiciona('ect')
lista1.adiciona('POO')
# print(lista1.eh_vazio())
# print(lista1.get_objeto(0))
# lista1.remove(1)
# print(lista.get_objeto(0))
# print(lista.get_objeto(1))
# lista1.reseta()
# lista1.imprime()
# print('tamanho da lista1: ', lista1.tamanho())

lista2 = lista1.copia()
# print(lista2.eh_vazio())
lista2.eh_vazio()
lista1.inverte()