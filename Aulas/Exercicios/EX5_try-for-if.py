"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este número é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
num = input('Digite um número inteiro: ')

try:
	num = int(num)
	if num % 2 == 0:
		print('O número é par!')
	else:
		print('O número é ímpar!')

except:
	print ('Não é um número inteiro.')

"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""
h = input('Digite a Hora atual: ')
h = int(h)
min = input('Digite os minutos: ')

if (00 <= h <= 11) and ('00' <= min <= '59'):
	print(f'Bom dia, são {h}:{min.zfill(2)}.')
elif (12 <= h <= 17) and ('00' <= min <= '59'):
	print(f'Boa tarde, são {h}:{min.zfill(2)}.')
elif (18 <= h <= 23) and ('00' <= min <= '59'):
	print(f'Boa noite, são {h}:{min.zfill(2)}.')
else:
	print('Essa não é uma hora válida.')

"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""
name = input('Digite seu nome: ')
name = len(name)
if (name > 1):
	if (1 < name <= 4):
		print("Seu nome é curto.")
	elif (5 <= name <= 6):
		print("Seu nome é normal.")
	else:
		print("Seu nome é muito grande.")
else:
	print("Um nome tem que ter mais de uma letra.")
