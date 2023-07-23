'''
 LAMBDA

 Função anônima, de uma linha, ou seja tudo deve ser escrito em uma única expressão
'''
lista_numeros = [4,32,59,87,2546,634,132,5,6,791]

lista_numeros.sort() #executa a ordenação interna da lista
print(lista_numeros)

lista_numeros.sort(reverse=True) #executa a ordenação reversa interna da lista
print(lista_numeros)

print()

lista_nomes = [
    {'Nome':'Higor', 'Sobrenome': 'Silva'},
    {'Nome':'Talita', 'Sobrenome': 'Riberio'},
    {'Nome':'Jether', 'Sobrenome': 'Oliveira'},
    {'Nome':'Beatriz', 'Sobrenome': 'Cunha'},
    {'Nome':'Antônio', 'Sobrenome': 'Nunes'},
]

def ordenar_nome(item):
    return item['Nome']

lista_nomes.sort(key=ordenar_nome)
for item in lista_nomes:
	print(item)

print()

def ordenar_sobrenome(item):
	return item['Sobrenome']

lista_nomes.sort(key=ordenar_sobrenome)
for item in lista_nomes:
	print(item)

print()
# .sort ordena de acordo com a tabela Unicode

def exibir(lista):
	for item in lista:
		print(item)

l1 = sorted(lista_nomes, key=lambda item:item['Nome'])
l2 = sorted(lista_nomes, key=lambda item:item['Sobrenome'])
# lambda tem seu funcionamento sem definição de nomeclatura
#utilizando sorted para criação de nova lista

exibir(l1)
print()
exibir(l2)

# OUTROS EXEMPLOS

def executa(funcao, *args):
	return(funcao(*args))

print(executa(lambda x, y : x + y, 2,3)) # função de soma, em que demonstram-se os argumentos, gera o cálculo e por fim se dá os valores

duplica = executa(lambda m: lambda n: n*m, 2)
print(duplica(2)) #função de multiplicador, em que utiliza-se lambda dentro de lambda, para gerar função recursiva

# é possível executar entrada de valores em lambda, mesmo não sendo o aconselhado

double = lambda: 2* int(input('Digite um número:'))
result = double()
print(result)
print()

