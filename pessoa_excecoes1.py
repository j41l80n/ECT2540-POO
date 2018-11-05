class Pessoa:
	def __init__(self, nome=''):
		self._nome = nome

	@property
	def nome(self):
		return self._nome
	
	@nome.setter
	def nome(self, n):
		if type(n) == str:
			self._nome = n
		else:
			raise Exception('n precisa ser do tipo str')

if __name__ == "__main__":
	p = Pessoa() # inicializa objeto com nome igual a ''
	print('Nome (antes): {}'.format(p.nome))
	p.nome = 7 # tenta atribuir nr. ao nome
	print('Nome (depois): {}'.format(p.nome)) # o que sera impresso?




