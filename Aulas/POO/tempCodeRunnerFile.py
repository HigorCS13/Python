from abc import ABC, ABCMeta, abstractmethod

class Log(ABC): #para a criação de classe abstrata, classe criada herda de ABC, pode ser também (metaclass = ABCMeta)
    
    @abstractmethod #abstração de método oficial
    def _log(self, msg):
        ...

    def log_error(self, msg):
        return self._log(f'Error: {msg}')
    
    def log_success(self, msg):
        return self._log(f'Success: {msg}')

class LogPrintMixin(Log):
	
	def _log(self, msg):
		print (f'{msg} ({self.__class__.__name__})')
                
l = LogPrintMixin()

l.log_error('opa')

# É possível criar @property @setter @classmethod @staticmethod e @method como abstratos, para isso use @abstractmethod como decorator mais interno.

# Foo - Bar são palavras usadas como placeholders (pode ser qualquer coisa).

class AbstractFoo(ABC):

    def __init__(self, name):
        self.name = name
    
    @property
    def name(self):
        ...
    
    @name.setter
    def name(self, name):
        ...

class Foo(AbstractFoo):
    def __init__(self, name):
        super().__init__(name)
        print('Inútil')

foo = Foo('Bar')

print(foo.name)