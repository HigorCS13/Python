# def criar_tabuada(n):
# 	for i in range(11):
# 		print(f'{n} x {i} = ', n * i)

def criar_tabuada(multiplicador):
	def multiplicar(numero):
		return numero * multiplicador
	return multiplicar

valor = input('Insira numero: ')
valor = int(valor)

for n in range(11):
	multiplo = criar_tabuada(n)
	print(f'{valor} x {n} = ', multiplo(valor))
