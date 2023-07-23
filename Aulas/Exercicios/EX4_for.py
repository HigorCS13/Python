name = input('Escreva seu nome: ')
age = input('Escreva sua idade: ')

if (name and age):
	print(f'Seu nome é {name}')
	print(f'Seu nome invertido é {name[::-1]}')
	print(f'Sua idade é {age}')
	if ' ' in name:
		print('Seu nome contém espaços')
		for x in name:
			i = 0
			if x == ' ':
				i = i + 1
				print(f'Seu nome tem {(len(name)) - i} letras')
	else:
		print('Seu nome não contém espaços')
		print(f'Seu nome tem {len(name)} letras')
	print(f'A primeira letra do seu nome é {name[0]}')
	print(f'A última letra do seu nome é {name[-1]}')
else:
	print('Desculpe, você deixou campos vazios.')
