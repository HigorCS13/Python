# Abstração

from pathlib import Path

LOG_FILE = Path(__file__).parent / 'log.txt' #função para endereçamento direto de pasta, sem ter que escrever na mão, com nome do arquivo definido

class Log:
    
	# é uma classe abstrata feita a mão
	def _log(self, msg): #assinatura do método
		raise NotImplementedError('Implemente o método Log')

	def log_error(self, msg):
		return self._log(f'Error: {msg}')

	def log_success(self, msg):
		return self._log(f'Success: {msg}')

class LogFileMixin(Log):
	
	def _log(self, msg):
		msg_formatada = f'{msg} ({self.__class__.__name__})'
		with open(LOG_FILE, 'a') as arquivo: #criação do arquivo .txt
			arquivo.write(msg_formatada)
			arquivo.write('\n')

class LogPrintMixin(Log):
	
	def _log(self, msg):
		print (f'{msg} ({self.__class__.__name__})')

if __name__ == '__main__': #serve para indicar funcionalidade apenas no local citado

	lp = LogPrintMixin()
	lp.log_error('qualquer coisa')
	lp.log_success('coisa qualquer')

	print()
	print(LOG_FILE) #caminho arquivo impresso
	print()

	lf = LogFileMixin()
	lf.log_error('qualquer coisa')
	lf.log_success('coisa qualquer')

