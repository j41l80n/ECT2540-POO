class NumerosComplexos:
	#construtor
	def __init__(self, parte_real=0, parte_imaginaria=0):
		#membros
		self.__parte_real = parte_real
		self.__parte_imaginaria = parte_imaginaria
        
        
	def get_parte_real(self):
		return self.__parte_real
    
	def set_parte_real(self, parte_real):
		#if type(parte_real) == float:
		self.__parte_real = parte_real
		#else:
		#	print('erro')

	def get_parte_imaginaria(self):
		return self.__parte_imaginaria
    
	def set_parte_imaginaria(self, parte_imaginaria):
		self.__parte_imaginaria = parte_imaginaria
        
	def imprime_numero_complexo(self, numero):	
		if:
			print(numero)
		else:
			print(numero)
    
	re = property(get_parte_real, set_parte_real)
	im = property(get_parte_imaginaria, set_parte_imaginaria)

numero = NumerosComplexos();
#numero.re(1)
#numero.im(2)
numero.imprime_numero_complexo(3)
