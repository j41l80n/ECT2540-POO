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
		p.nome = 'roberto'
		print('Nome: {}, sobrenome: {}'.format(p.nome, p.sobrenome)) # outro erro: atributo inexistente
	except Exception:
		print('Erro qualquer')
	except AttributeError:
		print('Erro acessando atributo inexistente')