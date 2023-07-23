def multiplicacao(*args):
	total = 1
	for numero in args:
		numero = int(numero)
		total *= numero
	return total

def par_ou_impar(x):
	if (x % 2 == 0):
		print('Número par!')
	else:
		print('Número ímpar!')

argumentos = input('Insira os valores numéricos desejados: ')
argumentos = argumentos.split()

total = multiplicacao(*argumentos) #LEMBRAR SEMPRE DE GERAR O DESEMPACOTAMENTO!!!!

print('A multiplicação desses números é', total)

par_ou_impar(total)
