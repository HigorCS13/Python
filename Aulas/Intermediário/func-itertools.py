# citações e funcionalidades do itertools

from itertools import zip_longest

list1 = [1, 2, 3, 4, 5, 6, 7]
list2 = ['a', 'b', 'c', 'd']

print(list(zip_longest(list1, list2, fillvalue='N/A')))

from itertools import count
#count() funciona junto a função next(), adicionando sempre mais um por conveção, quando chamado

c1 = count(10, 3) # iteravel de contador infinito, em que seu primeiro parametro determina seu ponto de início, e seu segundo determina seus passos
r1 = range(10, 100, 3) # contador finito, em que seu primeiro parâmetro é o início, segundo é o fim e o terceiro seu passo

print ('count')
for i in c1:
	if i >=100:
		break	
	print(i)
print()

print ('range')
for i in r1:
    print(i)
print()

from itertools import combinations, permutations, product

# combinations - executa combinações de iteráveis baseado no tamanho do grupo escolhido (ordem não importante)
# permutations - executa combinações de iteráveis baseado no tamanho do grupo escolhido (ordem importante)
# product - executa combinações de iteráveis baseado no tamanho do grupo escolhido, em relação a quantidade de grupos existentes no mesmo grupo principal (ordem sequencial)

def print_iter(iterator):
	print(*list(iterator), sep = '\n')
	print()

pessoas = ['Higor', 'Talita', 'Filipe', 'Sabrina']

camisetas =[
	['preta', 'branca'],
	['S', 'M', 'L'],
	['Masculino', 'Feminino']
	]

print_iter(combinations(pessoas, 2))
#para a execução da função, se indica o grupo e em qual quantidade será dividida as possibilidades

print_iter(permutations(pessoas, 2))
#para a execução da função, se indica o grupo e em qual quantidade será dividida as possibilidades

print_iter(product(*camisetas))
#para a execução da função, se faz o desempacotamento do grupo selecionado


from itertools import groupby
# groupby - executa a ordenação de acordo com algum dado em igualdade


alunos = [
	{'Nome':'Higor', 'Nota': 'A'},
	{'Nome':'Filipe', 'Nota': 'B'},
	{'Nome':'Talita', 'Nota': 'A'},
	{'Nome':'Sabrina', 'Nota': 'C'},
	{'Nome':'Brendon', 'Nota': 'C'},
	{'Nome':'Nicolle', 'Nota': 'B'},
	{'Nome':'Teko', 'Nota': 'C'},
	{'Nome':'Ana', 'Nota': 'C'},
	{'Nome':'Feio', 'Nota': 'B'}
	]

def ordena(aluno):
	return aluno['Nota']

alunos_agrupados = sorted(alunos, key = ordena) #organizar por meio de sorted, usando uma função criada para ser um lambda

grupos = groupby(alunos_agrupados, key = ordena)

for grupo in grupos:
	for aluno in grupo:
		print_iter(list(aluno))


from functools import partial #biblioteca de ferramentas para funções

produtos = [
    {'Nome' : 'Produto 5', 'Preço' : 10.00},
    {'Nome' : 'Produto 1', 'Preço' : 22.32},
    {'Nome' : 'Produto 2', 'Preço' : 10.11},
    {'Nome' : 'Produto 3', 'Preço' : 105.87},
    {'Nome' : 'Produto 4', 'Preço' : 69.90}
]

def aumenta_porcento(valor, porcentagem):
	return round(valor * porcentagem, 2)

print_iter(produtos)


novos_produtos10 = [
	{**p, 'Preço' : aumenta_porcento(p['Preço'], 1.1)} for p in produtos
]

print_iter(novos_produtos10)


aumenta_20p = partial(
	aumenta_porcento,
	porcentagem = 1.2
)
# partial - um closure padrão que executa a função incluida de acordo com o solicitado

novos_produtos20 = [
	{**p, 'Preço' : aumenta_20p(p['Preço'])} for p in produtos
]

print_iter(novos_produtos20)

def muda_preco(produto):
	return {**produto, 'Preço' : aumenta_porcento(produto['Preço'], 1.3)}

novos_produtos30 = map(muda_preco, produtos)
# map - função que cria um iterador novo, baseado em uma função e outro iterável


print_iter(novos_produtos30)

from types import GeneratorType # módulo de trabalho com tipos

print(isinstance(novos_produtos30, GeneratorType))
print()
# GeneratorType - booleano que determina se o iterável é um generator

print(list(map(lambda x : x + 3, [1, 2, 3, 4, 5])))
print()

print_iter(filter(lambda p : p['Preço'] > 20, produtos))
print()
# filter - de modo parecido ao map, cria um filtro condicional utilizando uam função e um vetor como referência

from functools import reduce
# reduce - função de functools, utiliza uma função como regra e um vetor de atuação, sendo necessário indicar valor inicial, e gera um valor "único"

total = reduce(lambda ac, p : ac + p['Preço'], produtos, 0)

print(round(total, 2))
print()

'''
Recursividade - funções que se chamam de volta, sendo úteis para dividir problemas grandes em partes menores

Toda recursiva deve ter:
	- um problema que possa ser dividido em partes menores
	- um caso recursivo que resolve o pequeno problema
	- um caso base que para a recursão
'''
#caso a recursiva não tenha uma saída fim, isso ira gerar um stack overflow, que é o limite de segurança de execução do código

# from sys import setrecursionlimit
# função de sistema que modifica o controle de memória para uso em recursões
# USAR COM CUIDADO

def recursiva(inicio = 0, fim = 10):
	if inicio >= fim:
		return fim
	
	inicio += 1
	return recursiva(inicio, fim)

print(recursiva())
print()


#setrecursionlimit(1004)
# print(recursiva(0, 1004))
# print()

def factorial(n):
	if n <= 1:
		return 1
	return n * factorial(n-1)

print(factorial(10))
print()

