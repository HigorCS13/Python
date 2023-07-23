'''Calculadora com while'''

while True:
	num_1 = input('Digite o primeiro número: ')
	num_2 = input('Digite o segundo número: ')
	op = input('Digite o operador (+-*/): ')
	num_val = None

	try:
		num_1 = float(num_1)
		num_2 = float(num_2)
		num_val = True
	except:
		num_val = None

	if num_val == None:
		print('Um ou ambos números digitados são inválidos!')
		continue
	
	op_perm = '+-*/'

	if op not in op_perm:
		print('Operador digitado é inválido!')
		continue
	if len(op) > 1:
		print('Digite apenas um operador!')
		continue

	if op == '+':
		print (f'{num_1} + {num_2} = ', num_1 + num_2)
	elif op == '-':	
		print (f'{num_1} - {num_2} = ', num_1 - num_2)	
	elif op == '*':	
		print (f'{num_1} * {num_2} = ', num_1 * num_2)
	else:
		print (f'{num_1} / {num_2} = ', num_1 / num_2)

	sair = input ('Deseja sair? [s]im [n]ão: ')
	sair = sair.lower().startswith('s') #possibilidade de utilizar múltiplas funções internas
	if sair:
		break
