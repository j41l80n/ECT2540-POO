class Pessoa:
	def __init__(self):
		self.nome = '' # tipo str
		self.idade = 0 # tipo int
		self.atividades = [] # tipo list
	def se_apresenta(self):
		print('Ola, meu nome e {} e tenho {} \
anos de idade'.format(self.nome, self.idade))

	def cumprimenta(self, outro):
		print("{}: Ola {}, \
tudo bem?".format(self.nome, outro.nome))

	def lista_atividades(self):
		print("Gosto de: ", end='')
		msg = ''
		for i in range(len(self.atividades)):
			msg += self.atividades[i]
			if i != len(self.atividades) - 1:
				msg += ', '
		print(msg)

	def compara_atividades(self, outro):
		cont = 0
		for a in outro.atividades:
			if a in self.atividades:
				cont += 1

		if cont == 0:
			print("{} nao tem atividade em comum com {}".format(self.nome, outro.nome))
		elif cont == 1:
			print("{} tem uma atividade em comum com {}".format(self.nome, outro.nome))
		elif cont/len(self.atividades) >= 0.8:
			print("{} tem muitas atividades em comum com {}".format(self.nome, outro.nome))
		else:
			print("{} tem algumas atividades em comum com {}".format(self.nome, outro.nome))


p1 = Pessoa()
p1.nome = 'Ana'
p1.idade = 20
p1.atividades += ['futebol', 'danca', 'instagram', 'fotografia', 'musica']
p2 = Pessoa()
p2.nome = 'Julia'
p2.idade = 25
p2.atividades += ['futebol', 'danca', 'instagram', 'xadrez', 'ioga']
p1.compara_atividades(p2)