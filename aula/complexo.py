# -*- coding: utf-8 -*-

""" Módulo contém classe para representar um número complexo. """

class Complexo:
	"""
	Classe Complexo: complexo.
	"""

	def __init__(self, re=0.0, im=0.0):
		"""Inicializa um número complexo"""
		self._re = re
		self._im = im

	@property
	def real(self):
		"""Retorna a parte real do número"""
		return self._re

	@real.setter
	def real(self, re):
		"""Insere a parte real do número"""
		if type(re) == int or type(re) == float:
			self._re = re
		else:
			print('re precisa ser int ou float')

	@property
	def imaginario(self):
		"""Retorna a parte imaginária do número"""
		return self._im

	@imaginario.setter
	def imaginario(self, im):
		"""Insere a parte imaginária do número"""
		if type(im) == int or type(im) == float:
			self._im = im
		else:
			print('im precisa ser int ou float')

	def imprime(self):
		"""imprime o número complexo"""
		if self._im >= 0:
			print('{} + {}j'.format(self._re, self._im))
		else:
			print('{} - {}j'.format(self._re, -self._im))

	def zera(self):
		"""Zera o número complexo"""
		self._re = 0.0
		self._im = 0.0

	def modulo(self):
		"""teste"""
		return (self._re**2 + self._im**2)**0.5

	def conjugado(self):
		"""conjulgado"""
		res = Complexo()
		res.re = self._re
		res.im = -self._im
		return res

	def soma(self, outro):
		"""Soma dois números complexos"""
		res = Complexo()
		res.real = self._re + outro.real
		res.imaginario = self._im + outro.imaginario
		return res

	def igual(self, outro):
		"""Verifica igualdade entre dois números complexos"""
		return self._re == outro.real and self._im == outro.imaginario

	def __repr__(self):
		return 'nuemro complexo'

if __name__ == "__main__":
	c1 = Complexo(0.5, 0.3)
	c2 = Complexo()
	c2.real = 0.5
	c2.imaginario = 0.3
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