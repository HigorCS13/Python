'''
List comprehension - forma rápida de criar listas a partir de iteráveis
'''
'''
print(list(range(10)))

lista = []

for numero in range(10):
	lista.append(numero)
print(lista)
'''

#exemplos acima possuem o mesmo valor que o de baixo
print()
lista = [numero for numero in range(10)]
print(lista)

print()
lista = [numero*2 for numero in range(10)] #pode-se indicar lógicas
print(lista)
print()



# MAPEAMENTO - transferencia de dados entre listas, execuntado alterações se desejado

produtos = [
	{'nome':'p1', 'preço':20},
	{'nome':'p2', 'preço':30},
	{'nome':'p3', 'preço':50}
]
novos_produtos = [
	#{'nome':produto['nome'], 'preço':produto['preço']} mesmo funcionamento abaixo, porém maior
	{**produto, 'preço':produto['preço'] * 1.05} #pode-se selecionar uma chave específica para alteração
	for produto in produtos
]
# * = desempacotamento lista / ** = desempacotamento dicionário
print(*novos_produtos, sep='\n')
print()

novos_produtos = [
	{**produto, 'preço':produto['preço'] * 1.05}
	if produto['preço'] > 30 else {**produto} # condicional de execução da alteração anterior
	for produto in produtos
]
print(*novos_produtos, sep='\n')
print()



# FILTRO (filter) - executa a transferencia seletiva de dados entre listas

import pprint #pretty print = serve para execução de print mais legíveis, porém não aceita certos parâmetros

def p(v):
	pprint.pprint(v, sort_dicts=False, width=40)


lista_numeros = [
	n for n in range(10)
	if n < 5 #filtro
]
p(lista_numeros)
print()

novos_produtos = [
	{**produto, 'preço':produto['preço'] * 1.05}
	if produto['preço'] > 30 else {**produto}
	for produto in produtos
	if (produto['preço'] > 20) # filtro que capta apenas os valores nessa condição
]
p(novos_produtos)
print()

numeros = [1,2,3,4,5,6,7,8,9,10]
novos_numeros = [numero for numero in numeros if numero > 5]
impares = [numero for numero in numeros if numero % 2 != 0]
pares = [numero for numero in numeros if numero % 2 == 0]
troca_numero = [numero if numero != 6 else 600 for numero in numeros]
quadrado = [[numero, numero ** 2] for numero in range(10)]
flat = [y for x in quadrado for y in x] # achatamento de lista, excluindo as listas internas

p(novos_numeros)
p(impares)
p(pares)
p(troca_numero)
print(quadrado)
print(flat)
print()



# posicionamento em plano
lista = []
for x in range(3):
	for y in range(3):
		lista.append((x,y))
p(lista)
print()

# mesma funcionalidade do código acima
lista = [
	(x,y)
	for x in range(3)
	for y in range(3)
]
p(lista)
print()

# Manipulação de strings
string = 'Higor Cunha'
numeros_letras = 2
nova_string = '|'.join([
	string[letra : letra + 2] 
	for letra in range(0, len(string), numeros_letras)
	])
p(nova_string)
print()

nomes = ['higor', 'talita', 'sabrina', 'filipe']
novos_nomes = [nome.upper() for nome in nomes]
p(novos_nomes)
print()
novos_nomes = [nome.title() for nome in nomes] # função que deixa apenas a primeria letra maiúscula
p(novos_nomes)
print()
novos_nomes = [
	f'{nome[:-1].lower()}{nome[-1].upper()}' 
	for nome in nomes
]
p(novos_nomes)
print()

# Dictionary / Set  Comprehension

produto = {
	'nome':'Caneta Azul',
	'preço': 2.5,
	'categoria':'Escritório'
}

dc = {
	chave : valor
	if isinstance(valor, (int, float)) else valor.upper()
	for chave,valor
	in produto.items()
}

p(dc)
print()

lista = [
	('a', 'valor a'),
	('b', 'valor b'),
	('c', 'valor c')
]

p(dict(lista))
print()

s1 = {i for i in range(10)}

p(s1)
p(set(range(10))) #set - definição rapida para sets - mesma ideia de cima
print()

# isinstance - função condicional que checa tipos

lista = [
	'a', 1, 1.5, True, [0,1,2], (1,2), {0,1}, {'nome': 'Higor'}
]

for item in lista:
	if isinstance(item, set):
		print('SET')
		item.add(5)
		print(item)
	
	elif isinstance(item, str):
		print('STR')
		item.upper()
		print(item)
	
	elif isinstance(item, (int, float)):
		if type(item) == bool:
			print('BOOL')
			print(item)
		else:
			print('NUM')
			print(item, item *2)
	
	else:
		print('OUTROS')
		print(item, type(item))
print()	
# Valores Truthy e Falsy

lista = []
dicionario = {}
tupla = ()
conjunto = set()
string = ''
inteiro = 0
flutuante = 0.0
nada = None
falso = False
intervalo = range(0)

def valores(valor):
	return 'Falsy' if not valor else 'Truthy'

print(f'Teste', valores('Teste'))
print(f'{lista = }', valores(lista))
print(f'{dicionario = }', valores(dicionario))
print(f'{tupla = }', valores(tupla))
print(f'{conjunto = }', valores(conjunto))
print(f'{string = }', valores(string))
print(f'{inteiro = }', valores(inteiro))
print(f'{flutuante = }', valores(flutuante))
print(f'{nada = }', valores(nada))
print(f'{falso = }', valores(falso))
print(f'{intervalo = }', valores(intervalo))
print()

#dir, hasattr e getattr
# Utilizando dir() no debug console, em um debug, pode-se observar todas as funções possiveis de acordo com o tipo do item inserido

string = 'Higor'
metodo = 'upper'
if hasattr(string, metodo): # hasattr - checa se existe a possibilidade da função mencionada em string
	print(f'Existe {metodo}')
	print(getattr(string, metodo)()) # getattr - executa a função mencionada em string
else:
	print(f'Método {metodo} não existe')
print()

#Generator expression, Iterables e Iterator

import sys #módulo padrão em python, utilizado para sistema

iterable = ['Eu', 'tenho', '__iter__']
iterator = iter(iterable) # podendo ser .__iter__()
#iter - gera um ponteiro de iteração, entregando um valor por vez

print(next(iterator)) # podendo ser .__next__()
#next - funçaõ de entrega de valor dentro do iterador
# o funcionamento acima se assimila com a função for

lista_gen = [n for n in range(10000)]
gen = (n for n in range(10000)) #generator expression - um comprehension dentro de parênteses, que gera um iterador sequêncial

print(gen, type(gen))
print()
# getsizeof - demonstra o tamanho em bytes do item mencionado
print(sys.getsizeof(lista_gen))
print(sys.getsizeof(gen))
print()
# diferente da lista, a generator expression gera um ponteiro iterador lógico, onde ele salva apenas o primeiro parâmetro, sendo sequencial a medida que for solicitado
# generator não possui indice

#Generator functions

def generator(n = 0):
	yield 1 # yield - executa a pausa da leitura da função em generators
	print('Continuando...')
	yield 2
	print('Mais uma vez...')
	yield 3
	print('Terminando...')
	return 'ACABOU!' # O return somente é atingido, nesse caso, se houver a insistência da chamada da função

gen = generator(0)
print(next(gen)) # para chamada manual, necessário a utilização de next
for n in gen:
	print(n)

print()

# com a função de pausa e proteção do yield, while loop pode ser executado sem quebra de código
def generator_loop(n = 0, maxim = 10):
	while True:
		yield n
		n += 1
		if n > maxim:
			return

gen = generator_loop(n = 85, maxim = 100)
for n in gen:
	print(n)

print()

# yield from - chamada de função generator, podendo ser posicionada dentro de outra função

def gen1():
	print('começou gen1')
	yield 1
	yield 2
	yield 3
	print('acabou gen1')

def gen2():
	print('começou gen2')
	yield 4
	yield 5
	yield 6
	print('acabou gen2')

def gen3(gen):
	print('COMEÇOU GEN3')
	yield from gen()
	yield 70
	yield 80
	yield 90
	print('ACABOU GEN3')

g1 = gen3(gen1)
g2 = gen3(gen2)
for n in g1:
	print(n)

print()

for n in g2:
	print(n)

print()

