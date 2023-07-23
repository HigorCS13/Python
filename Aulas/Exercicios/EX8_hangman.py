
'''
 ______
 |    |
 |    O
 |   /|\
 |	 / \	
 |
_|_

'''

def morto(n):

	if n == 0:
		for i in range(3):
			print(' |')
	elif n == 1:
		print(' |    O')
		for i in range(3):
			print(' |')
	elif n == 2:
		print(' |    O')
		print(' |    |')
		for i in range(2):
			print(' |')
	elif n == 3:
		print(' |    O')
		print(' |   /|')
		for i in range(2):
			print(' |')
	elif n == 4:
		print(' |    O')
		print(' |   /|\\')
		for i in range(2):
			print(' |')
	elif n == 5:
		print(' |    O')
		print(' |   /|\\')
		print(' |   /')
		print(' |')
	elif n > 5:
		print(' |    O')
		print(' |   /|\\')
		print(' |   / \\')
		print(' |')
	print('_|_')

#primeira forca:

def forca(n):
	#superior
	print(' _', end="")
	for i in range(4):
		print('_', end="")
	print('_')

	print(' |', end="")
	for i in range(4):
		print(' ', end="")
	print('|')

	morto(n)

enter = input('Deseja novo jogo? Y/N ')

while True:

	n = 0
	cont = ''

	if (enter == 'Y' or enter =='y'):
		secret = input('Digite a palavra secreta: ')
		print("\033c", end="")
		print('JOGO DA FORCA')
		forca(n)
		print(len(secret)*'*')
		while n < 6:
			word = ''
			letter = input('Digite uma letra: ')
			print("\033c", end="")

			if len(letter) > 1:
				forca(n)
				print('Digite apenas uma letra!')
				continue

			if letter in secret:
				cont += letter
				forca(n)


			else:
				print('Você errou!')
				n += 1
				forca(n)

				if n < 6:
					print(f'Você ainda tem {6-n} tentativas.')
				else:
					print('A palavra era', secret)
					print('Você perdeu!')
			
			for sec_let in secret:
				if sec_let in cont:
					word += sec_let
				else:
					word += '*'
			print(word)
			
			if word == secret:
				print('Você ganhou!')
				break
		
		enter = input('Deseja novo jogo? Y/N ')
	elif (enter == 'N' or enter =='n'):
		print('Fim de jogo.')
		break
	else:
		print('Opção inválida!')
		enter = input('Deseja novo jogo? Y/N ')

