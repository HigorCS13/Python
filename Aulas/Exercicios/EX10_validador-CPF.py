#VALIDADOR DE CPF

def regiao_emissora(x):

	if x[8] == '1':
		print('CPF emitido nas regiões DF/GO/MS/MT/TO')
	elif x[8] == '2':
		print('CPF emitido nas regiões AC/AM/AP/PA/RO/RR')
	elif x[8] == '3':
		print('CPF emitido nas regiões CE/MA/PI')
	elif x[8] == '4':
		print('CPF emitido nas regiões AL/PB/PE/RN')
	elif x[8] == '5':
		print('CPF emitido nas regiões BA/SE')
	elif x[8] == '6':
		print('CPF emitido nas regiões MG')
	elif x[8] == '7':
		print('CPF emitido nas regiões ES/RJ')
	elif x[8] == '8':
		print('CPF emitido nas regiões SP')
	elif x[8] == '9':
		print('CPF emitido nas regiões PR/SC')
	elif x[8] == '0':
		print('CPF emitido nas regiões RS')

	return 

def primeiro_digito(x):
	n = 10
	total = 0
	validacao = x[:9] #fatiamento para busca

	for i in validacao:
		total += int(i) * n
		n -= 1

	digito_1 = (total * 10) % 11
	digito_1 = digito_1 if digito_1 <= 9 else 0
	return str(digito_1)

def segundo_digito(y):
	n = 11
	total = 0
	validacao = y[:10] #fatiamento para busca

	for i in validacao:
		total += int(i) * n
		n -= 1

	digito_2 = (total * 10) % 11
	digito_2 = digito_2 if digito_2 <= 9 else 0
	return str(digito_2)

cpf = ' '

#import sys --> biblioteca de sistemas
		#sys.exit() --> função de finalização do sistema

while cpf:
	cpf = input('Insira seu CPF: ')

	if (len(cpf) != 11 and len(cpf) != 14):
		
		print('CPF inexistente!')
	else:
		'''
		metodo de expressões regulares

		import re --> biblioteca de expressões regulares

		cpf_num = re.sub(r'[^0-9]', '', cpf)
			--> lê-se funçaõ de experessões regulares de substituição, para todos caracteres que não(^) forem números, substituir por nada em cpf
		'''
		try:
			cpf_num = cpf.replace('.', '').replace('-', '') #caso seja utilizado esses caracteres, serão retirados
			
			if (primeiro_digito(cpf_num) == cpf_num[9] and segundo_digito(cpf_num) == cpf_num[10]):
				regiao_emissora(cpf)
				print(f'CPF {cpf} é válido!')
				break
			else:
				print(f'CPF {cpf} é inválido!')
				break
		except:
			print('CPF inexistente!')
