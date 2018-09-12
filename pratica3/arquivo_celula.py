class Celula():
	def __init__(self, dado, proximo=None):
		self.__dado = dado
		self.__proximo = proximo

	def get_dado(self):
		return self.__dado

	def set_dado(self, object):
		self.__dado = object

	def get_proximo(self):
		return self.__proximo

	def set_proximo(self, proximo):
		self.__proximo = proximo

	dado = property(get_dado, set_dado)
	proximo = property(get_proximo, get_proximo)