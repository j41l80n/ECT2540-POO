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
			raise TypeError('Excecao: n precisa ser do tipo str')

if __name__ == "__main__":
	p = Pessoa()
	try:
		n = (1,2,3)
		p.nome = n
	except Exception as err:
		print('Erro: {}'.format(err))
	else:
		print('Nome: {}'.format(p.nome))
	print('Fim do programa')
