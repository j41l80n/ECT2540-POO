class NumerosComplexos:
	# construtor
	def __init__(self, parte_real=0, parte_imaginaria=0):
		# membros
		self.__parte_real = parte_real
		self.__parte_imaginaria = parte_imaginaria
		
	# parte real
	def get_parte_real(self):
		return self.__parte_real
    
	def set_parte_real(self, parte_real):
		self.__parte_real = parte_real

	# parte imaginaria
	def get_parte_imaginaria(self):
		return self.__parte_imaginaria
    
	def set_parte_imaginaria(self, parte_imaginaria):
		self.__parte_imaginaria = parte_imaginaria
    
    # funcoes property
	re = property(get_parte_real, set_parte_real)
	im = property(get_parte_imaginaria, set_parte_imaginaria)

	
	def imprime_numero_complexo(self, numero):	
		if numero > 0:
			print('teste {} teste {}' .format(0, 1))
		else:
			print(numero)
		
	def zerar_numero_real(self, numero):	
		self.__parte_real = numero
		self.__parte_imaginaria = numero
		
	def calcula_modulo(self):
		pass
	
	def calcula_conjulgado(self):
		pass
		
	def soma_complexos(self):
		pass
		
	def comapra_complexos(self):
		pass
			
numero = NumerosComplexos();
numero.imprime_numero_complexo(3)
