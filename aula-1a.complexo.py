class Complexo:
	def __init__(self, re=0.0, im=0.0):
		self._re = re
		self._im = im

	def get_real(self):
		return self._re

	def set_real(self, re):
		if type(re) == int or type(re) == float:
			self._re = re
		else:
			print('re precisa ser int ou float')

	def get_imag(self):
		return self._im

	def set_imag(self, im):
		if type(im) == int or type(im) == float:
			self._im = im
		else:
			print('im precisa ser int ou float')

	def imprime(self):
		if self._im >= 0:
			print('{} + {}j'.format(self._re, self._im))
		else:
			print('{} - {}j'.format(self._re, -self._im))

	def zera(self):
		self._re = 0.0
		self._im = 0.0

	def modulo(self):
		return (self._re**2 + self._im**2)**0.5

	def conjugado(self):
		res = Complexo()
		res.re = self._re
		res.im = -self._im
		return res

	def soma(self, outro):
		res = Complexo()
		res.re = self._re + outro.re
		res.im = self._im + outro.im
		return res

	def igual(self, outro):
		return self._re == outro.re and self._im == outro.im

	re = property(get_real, set_real)
	im = property(get_imag, set_imag)

c1 = Complexo(0.5, 0.3)
c2 = Complexo()
c2.re = 0.5
c2.im = 0.3
print('C1:')
c1.imprime()
print('Modulo: {}'.format(c1.modulo()))
print('Conj. de C1:')
c1c = c1.conjugado()
c1c.imprime()
print('C2:')
c2.imprime()
print('Modulo: {}'.format(c2.modulo()))
if c1.igual(c2):
	print('Os dois numeros sao iguais')
else:
	print('Os dois numeros sao diferentes')
c3 = c1.soma(c2)
print('C3:')
c3.imprime()