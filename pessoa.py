class Pessoa:
	def __init__(self, nome=''):
		self.__nome = nome
		self.__atividades = []

	def get_nome(self):
		return self.__nome

	def set_nome(self, nome):
		if type(nome) == str:
			self.__nome = nome
		else:
			print('nome precisa ser do tipo string')

	def get_atividades(self):
		return self.__atividades

	nome = property(get_nome, set_nome)
	atividades = property(get_atividades, None)




