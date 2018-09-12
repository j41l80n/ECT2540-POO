# from celula import *
import celula

class ListaEncadeada():
	def __init__(self, head=None, tail=None):
		self.__contador = 0
		self.__head = head
		self.__tail = tail

	def get_contador(self):
		return self.__contador

	def get_head(self):
		return self.__head

	def get_tail(self):
		return self.__tail

	def adiciona(self, dado):
		cel = celula.Celula(dado)

		if self.__head == None:
			self.__head = cel
			self.__tail = cel
			self.__contador += 1
		else:
			self.__tail.set_proximo(cel)
			self.__tail = cel
			self.__contador += 1

	def remove(self, indice):
		if self.__contador > 0:
			for i in range(indice-1):
				print('remove: ', i)
			self.__contador -= 1
		else:
			print('erro ao remover')


	contador = property(get_contador)
	head = property(get_head)
	tail = property(get_tail)

#realizando testes
if __name__ == "__main__":
	listaEncadeada = ListaEncadeada()
	listaEncadeada.adiciona('teste1')
	listaEncadeada.adiciona('teste1')

	print('contador: ', listaEncadeada.contador)
	listaEncadeada.remove(2)
	print('contador: ', listaEncadeada.contador)