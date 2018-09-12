import lista_encadeada

class Pilha():
	def __init__(self):
		self.__quantidade_elementos = 0

	def empilha(self, object):
		lst_encd = lista_encadeada.ListaEncadeada()
		lst_encd.adiciona(object)
		self.__quantidade_elementos += 1

	def desempilha(self):
		lst_encd = lista_encadeada.ListaEncadeada()
		lst_encd.remove(lst_encd.contador-1)
		self.__quantidade_elementos -= 1

	def eh_vazia(self):
		if lst_encd.contador > 0:
			return False
		else:
			return True

	def imprime(self):
		lst_encd = lista_encadeada.ListaEncadeada()
		for i in range(lst_encd.contador):
			print('teste')

if __name__ == "__main__":
	pilha = Pilha()
	pilha.empilha('ufrn')
	pilha.empilha('ect')
	pilha.empilha('poo')
	pilha.imprime()