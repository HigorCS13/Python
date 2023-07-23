from log import LogPrintMixin

class Eletronico:

	def __init__(self, nome):
		self._nome = nome
		self._ligado = False

	@property
	def nome(self):
		return self._nome
	
	@nome.setter
	def nome(self, nome):
		self._nome = nome

	def ligar(self):
		if not self._ligado:
			self._ligado = True
			print(f'{self.nome} foi ligado')
		else:
			print(f'{self.nome} já está ligado')

	def desligar(self):
		if self._ligado:
			self._ligado = False
			print(f'{self.nome} foi desligado')
		else:
			print(f'{self.nome} já está desligado')

class Smartphone(Eletronico, LogPrintMixin):
	
	def ligar(self):
		super().ligar()

		if self._ligado:
			msg = 'Login'
			self.log_success(msg)

	def desligar(self):
		super().desligar()
		
		if self._ligado:
			msg = 'Logout'
			self.log_error(msg)