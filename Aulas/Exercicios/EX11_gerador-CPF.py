#GERADOR DE CPF

import random #biblioteca de randomização

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

cpf = ''

for i in range(9):
	cpf += str(random.randint(0, 9)) #função para randomizar númemros

cpf += primeiro_digito(cpf) + segundo_digito(cpf)
cpf = list(cpf)
cpf.insert(3, '.')
cpf.insert(7, '.')
cpf.insert(11, '-')
cpf = ''.join(cpf)

print(cpf)
