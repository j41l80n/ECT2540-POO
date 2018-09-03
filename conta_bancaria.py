class ContaBancaria:
	def __init__(self, num=0, tit='', saldo=0.0, lim=1000.0):
		self._numero = num
		self._titular = tit
		self._saldo = saldo
		self._limite = lim

	def imprime_info(self):
		print('Titular: {}'.format(self._titular))
		print('Conta: {}'.format(self._numero))

	def imprime_saldo(self):
		print('Titular: {}'.format(self._titular))
		print('Conta: {}'.format(self._numero))
		print('Saldo: R${:.2f}'.format(self._saldo))

	def deposita(self, valor):
		if type(valor) != float:
			print('valor deve ser float')
		elif valor <= 0:
			print('valor deve ser maior que 0.0')
		else:
			self._saldo += valor
			print('Deposito de R${:.2f} realizado'.format(valor))

	def saca(self, valor):
		if type(valor) != float:
			print('valor deve ser float')
		elif self.__checa_transacao(valor):
			self._saldo -= valor
			print('Saque de R${:.2f} realizado'.format(valor))

	def transfere(self, outra, valor):
		if type(outra) != ContaBancaria:
			print('outra deve ser ContaBancaria')
		elif type(valor) != float:
			print('valor deve ser float')
		elif self.__checa_transacao(valor):
			self._saldo -= valor
			outra._saldo += valor
			print('Transferencia de R${:.2f} realizada'.format(valor))
			print('Dados da transferencia:')
			outra.imprime_info()

	def __checa_transacao(self, valor):
		if valor <= 0:
			print('valor deve ser maior que 0.0')
			return False
		elif valor > self._limite:
			print('Valor requisitado e superior ao limite. Operacao nao realizada.')
			return False
		elif valor > self._saldo:
			print('Saldo insuficiente. Operacao nao realizada.')
			return False
		return True


c1 = ContaBancaria(11, 'Joao', 500.0)
c1.imprime_saldo()
print('----------')

c1.deposita(100.0)
c1.imprime_saldo()
print('----------')

c1.saca(50.0)
c1.imprime_saldo()
print('----------')

c2 = ContaBancaria(33, 'Maria', 300.0)
c1.transfere(c2, 300.0)
c1.imprime_saldo()
c2.imprime_saldo()
print('----------')

