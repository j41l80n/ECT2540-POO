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
		n = (1, 2, 3)
		p.nome = n # ira levantar erro, já que n nao e str
	except: # cláusula de tratamento de erros:
		print('Ocorreu um erro na leitura dos dados') # imprime uma mensagem
		print('Atribuindo nome padrao para pessoa') # atribui um nome padrão para pessoa
		p.nome = 'Erro'
	print('Nome: {}'.format(p.nome))