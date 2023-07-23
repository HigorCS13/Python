# Exercício com classes
# 1 - Crie uma classe Carro (Nome)
# 2 - Crie uma classe Motor (Nome)
# 3 - Crie uma classe Fabricante (Nome)
# 4 - Faça a ligação entre Carro tem um Motor
# Obs.: Um motor pode ser de vários carros
# 5 - Faça a ligação entre Carro e um Fabricante
# Obs.: Um fabricante pode fabricar vários carros
# Exiba o nome do carro, motor e fabricante na tela

class Marca:
    def __init__(self,nome):
        self.nome = nome
        self._motor = None
        self._carro = None
    
    @property
    def motor(self):
        return self._motor
    
    @motor.setter
    def motor(self, motor):
        self._motor = motor
        
    @property
    def carro(self):
        return self._carro
    
    @carro.setter
    def carro(self, marca):
        self._carro = marca

class Carro:
    def __init__(self, nome):
        self.nome = nome

class Motor:
    def __init__(self,nome):
        self.nome = nome

v6 = Motor('V6')
v8 = Motor('V8')
v12 = Motor('V12')

lamborghini = Marca('Lamborghini')

aventador = Carro('Aventador')
lamborghini.motor = v12.nome
lamborghini.carro = aventador.nome

print(lamborghini.nome, lamborghini.carro, lamborghini.motor)