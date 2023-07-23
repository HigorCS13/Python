perguntas = [
	{
		'Pergunta:' : 'Quanto é 2 + 2?',
		'Opções:' : ['1', '3', '4', '5'],
		'Resposta:' : '4',
	},
	{
		'Pergunta:' : 'Quanto é 5 * 5?',
		'Opções:' : ['25', '55', '10', '51'],
		'Resposta:' : '25',
	},
	{
		'Pergunta:' : 'Quanto é 10 / 2?',
		'Opções:' : ['4', '5', '2', '1'],
		'Resposta:' : '5',
	}
]

qtd_acertos = 0

for pergunta in range(len(perguntas)):# gerar tamanho por range(len())
	print(perguntas[pergunta]['Pergunta:'])

	# opcoes = list(perguntas[pergunta].keys()) # demonstra a chave sem colchetes 
	#print(opcoes[1])
	print()
	global resposta_correta

	for i, opcao in enumerate(perguntas[pergunta]['Opções:']): #enumerate e duas variáveis para listar opções
		print(f'{i})', opcao) #for sempre ira buscar internamente no referido
		if opcao == perguntas[pergunta]['Resposta:']:
			resposta_correta = i
		else:
			continue
	
	try:
		resposta = int(input('Escolha uma opção: '))
		if resposta == resposta_correta:
			qtd_acertos += 1
			print('Resposta correta!')
		else:
			print('Resposta errada!')
		print()
	except ValueError:
		print('Resposta errada!')
		print()

print('Você Acertou', qtd_acertos)
print('de', len(perguntas), 'perguntas.')
