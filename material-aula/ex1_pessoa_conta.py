class Pessoa:
	def __init__(self, nome, cpf):
		self._nome = nome
		self._cpf = cpf
		self._contas = []

	# gets/sets etc.

	def imprime_contas(self):
		for c in self._contas:
			c.imprime_informacao()

class Conta:
	def __init__(self, tit=None, num=0, saldo=0.0):
		self._numero = num
		self._saldo = saldo
		self._titular = tit

	def imprime_informacao(self):
		print('titular: {}'.format(self._titular._nome))
		print('conta: {}, saldo: {}'.format(self._numero, self._saldo))

p = Pessoa('Joao', '000.111.222-34')
c1 = Conta(p, 131, 200.00)
c2 = Conta(p, 231, 100.00)
c3 = Conta(p, 531, 1000.00)
p._contas.append(c1)
p._contas.append(c2)
p._contas.append(c3)
p.imprime_contas()


