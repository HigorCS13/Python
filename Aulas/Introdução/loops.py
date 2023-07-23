#while - em python, pode-se usar combinado a função break de maneira mais simples
#break - função que busca o loop mais próximo e executa o fim dele, de acordo com a sequência

h = True

while h:
	nome = input ('Digite seu nome: ')
	print (f'Seu nome é {nome}')
	if nome == 'sair':
		break
print ('Acabou')

count = 0

while count <= 10:
	print (count)
	count += 1

'''
Operadores de atribuição

=  +=  -=  *=  /=  //=  **=  %=

'''

count = 10
count *= '2'

print (count)

#continue - serve para "pular" um comando dentro de um loop

count = 0

while count < 10:
	count += 1
	if count % 2 == 0:
		continue
	print (count)

#while/else - possível execução de else dentro do loop while, servindo para possível ativação de código caso while se concretize sem break.

str = input('Coloque seu nome: ')
i = 0

while i < len(str):
	l = str[i]
	print(l)
	i += 1
	if l == ' ':
		print('Há espaços em seu nome')
		break
else:
	print('Não há espaços em seu nome')
print('fora do while')

#while é comumente usado para repetições "infinitas", em que seja possível que se permaneça acontecendo até que se faça sair por comando

#for - gera um laço finito, em que, definindo uma variável, ela gera o laço de acordo com a condição sendo True


text = input ('Insira uma palavra: ')
new_txt = ''

for l in text:
	print (l)
	new_txt += l
print(new_txt)

'''
range - tipo iteravel que monta um vetor limitado, determinado dentro de parenteses (start, stop, step)
	caso seu conteudo tenha apenas um item, será determindado como stop, dois itens, start/stop
	padrão de atrt = 0, padrao step = 1, finaliza com um a menos de seu stop
'''

num = range (0, 10, 2)

for n in num:
	print(n)

'''
Iterável -> determinador de valor
Iterador -> aquele que entrega o valor
metodo (.método) -> executor que, após o iterador, determina ações
next -> me entrega o próximo valor
iter -> me entregue seu iterador
'''

text = 'Higor'.__iter__()
print(text)

text = iter('Higor')
print(text)

text = iter('Higor')
print(text.__next__())
print(next(text))

'''
funcionalidade "for"

text = 'Higor"
iterator = iter(text)

while True:
	try:
		letter = next(iterator)
		print (letter)
	except StopIteration:
		break
'''

for i in range(10):
	if i == 2:
		print('pula')
		continue
	if i == 8:
		print('fim')
		break
	for j in range (1,3):
		print(i,j)
else:
	print('For completado!')