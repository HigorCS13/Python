from log import LogFileMixin, LogPrintMixin

lp = LogPrintMixin()
lp.log_error('qualquer coisa')
lp.log_success('coisa qualquer')

print()

lf = LogFileMixin()
lf.log_error('qualquer coisa')
lf.log_success('coisa qualquer')

from eletronico import Smartphone

galaxy_s = Smartphone('Galaxy S')
iphone = Smartphone('Iphone')

galaxy_s.ligar()
iphone.desligar()
print()

# Classes abstratas - Abstract Base Class (abc)
# ABCs são usadas como contratos para a definição
# de novas classes. Elas podem forçar outras classes
# a criarem métodos concretos. Também podem ter
# métodos concretos por elas mesmas.
# @abstractmethods são métodos que não têm corpo.
# As regras para classes abstratas com métodos
# abstratos é que elas NÃO PODEM ser instânciadas
# diretamente.
# Métodos abstratos DEVEM ser implementados
# nas subclasses (@abstractmethod).
# Uma classe abstrata em Python tem sua metaclasse
# sendo ABCMeta.
# É possível criar @property @setter @classmethod
# @staticmethod e @method como abstratos, para isso
# use @abstractmethod como decorator mais interno.

from abc import ABC, abstractmethod

class Log1(ABC): # pode-se tambem 'metaclass = ABCMeta'
    
	@abstractmethod
	def _log(self, msg): #assinatura do método
		...

	def log_error(self, msg):
		return self._log(f'Error: {msg}')

	def log_success(self, msg):
		return self._log(f'Success: {msg}')

class LogPrintMixin1(Log1):
	
	def _log(self, msg):
		print (f'{msg} ({self.__class__.__name__})')

log1 = LogPrintMixin1()

log1.log_error('oi')