class Motor:
	def __init__(self, pot=0, cil=0):
		self._pot = pot
		self._cil = cil

	def liga(self):
		print("Ligando motor de {} cilindros e {} de potencia".format(self._pot, self._cil))

class Roda:
	def __init__(self, aro=0, perfil=0):
		self._aro = aro
		self._perfil = perfil

	def gira(self):
		print("Girando roda")

class Carro:
	def __init__(self, marca='', modelo='', motor=None, rodas=None):
		self._marca = marca
		self._modelo = modelo
		self._motor = motor
		self._rodas = rodas

	def liga(self):
		if self._motor and len(self._rodas) == 4:
			print('Ligando carro {} {}'.format(self._marca, self._modelo))
			self._motor.liga()
			for r in self._rodas:
				r.gira()
		else:
			print('Carro incompleto')

m = Motor(200, 4)
m.liga()

r1 = Roda(16, 60)
r2 = Roda(16, 60)
r3 = Roda(16, 60)
r4 = Roda(16, 60)
r1.gira()
rodas = [r1, r2, r3, r4]

c = Carro('Honda', 'Civic', m, rodas)
c.liga()