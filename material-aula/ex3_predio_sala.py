class Sala:
	def __init__(self, numero=0, empresa=''):
		self._numero = numero
		self._empresa = empresa

class Predio:
	def __init__(self, numero=0, endereco=''):
		self._numero = numero
		self._endereco = endereco
		self._salas = []
		# predio tem 10 salas
		for i in range(10):
			s = Sala(i, 'empresa' + str(i))
			self._salas.append(s)

	def imprime_salas(self):
		for s in self._salas:
			print('Nr.: {}, empresa: {}'.format(s._numero, s._empresa))

p = Predio(600, 'Edificio Empresarial')
p.imprime_salas()