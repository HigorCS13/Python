import os #biblioteca de comandos do terminal do sistema operacional

entrada = input('Deseja criar lista? [S][N] ')
lista = []

def imprime_lista():
	for indice, nome in enumerate(lista):
			print(indice + 1, nome)


while entrada:
	
	if entrada == 'S' or entrada == 's':
		os.system('cls') #comando executado da biblioteca
		print('Selecione uma opção:')
		opcao = input('[I]nserir [A]pagar [L]istar ')

		if opcao == 'i' or opcao == 'I':
			imprime_lista()
			incluir = input('Insira um item: ')
			lista.append(incluir)
		elif opcao == 'a' or opcao == 'A':
			imprime_lista()
			n = input('Selecione um item numérico da lista: ')
			try:
				lista.pop(int(n))
			except:
				print('Não é um valor aceitável!')
		elif opcao == 'l' or opcao == 'L':
			if len(lista) == 0:
				print('Nada para listar!')
			else:
				imprime_lista()
		else:
			print('Opção inválida!')	

	elif entrada == 'N' or entrada == 'n':
		os.system('cls')
		print('Fim de lista!')
		imprime_lista()
		break
	else:
		os.system('cls')
		print('Opção inválida!')
	
	entrada = input('Deseja continuar na lista? [S][N] ')
