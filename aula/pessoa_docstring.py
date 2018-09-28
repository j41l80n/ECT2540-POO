# -*- coding: utf-8 -*-

""" Módulo contém classe para representar uma pessoa. """

class Pessoa:
	"""
	Classe pessoa: armazena o nome de uma pessoa.
	Também armazena a quantidade de instâncias criadas
	e cada uma delas em atributos de classe.
	"""
	_quant = 0
	_pessoas = []

	def __init__(self, nome=''):
		"""Inicializa pessoa com nome informado (padrão: string vazia)"""
		self._nome = nome
		Pessoa._quant += 1
		Pessoa._pessoas.append(self)

	@property
	def nome(self):
		"""Nome da pessoa"""
		return self._nome

	@nome.setter
	def nome(self, n):
		self._nome = n

	def __repr__(self):
		"""Pessoa como string no formato '>>> self.nome'"""
		s = '>>> {}'.format(self._nome)
		return s

	def __lt__(self, outro):
		"""Retorna verdadeiro se self.nome < outro.nome"""
		if self._nome < outro.nome:
			return True
		else:
			return False

	@staticmethod
	def num_pessoas():
		"""Método de classe: obtém total de instâncias criadas"""
		return Pessoa._quant

	@staticmethod
	def imprime_pessoas():
		"""Método de classe: imprime cada uma das pessoas criadas"""
		i = 0
		for p in Pessoa._pessoas:
			print("[{}]: {}".format(i, p.nome))
			i += 1

	@staticmethod
	def ordena_por_nome():
		"""Método de classe: ordena a lista contendo as instâncias da classe
		   por ordem alfabética do nome"""
		Pessoa._pessoas = sorted(Pessoa._pessoas)

if __name__ == "__main__":
	print("Pessoas (antes): {}".format(Pessoa.num_pessoas())) # chamado a partir da classe
	p1 = Pessoa('Joao')
	p2 = Pessoa('Jose')
	p3 = Pessoa('Amanda')
	p4 = Pessoa('Renata')
	print("Pessoas (depois): {}".format(p1.num_pessoas())) # chamado a partir da instancia
	Pessoa.ordena_por_nome()
	for p in Pessoa._pessoas:
		print(p)


