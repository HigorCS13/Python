'''
Listas em Python

list - mutável
suporta vários valores de qualquer tipo
suporta indice e fatiamento
métodos úteis: 
	append - adiciona ao fim da lista
	insert - adiciona ao endereço
	pop - remove o solicitado
	del - apaga o solicitado
	clear - limpeza
	extend - extenção
	+ - concatenação

CRUD - Create, Read, Update, Delete

'''

lista = [] #create
print(lista) #read
print(type(lista))
print(bool(lista))

lista = [123, True, 'Higor', 1.2, []]
print(lista)
print(lista[2].upper(), type(lista[2]))

lista[-3]='Talita' #update
print(lista)
print(lista[2].upper(), type(lista[2]))

del lista[3] #delete
print(lista)

#sempre evitar reescrever dados, apenas retirar e adicionar
#sempre buscar trabalhar com o final da lista

lista.append(50) # adiciona ao fim da lista
print(lista)
lista.pop() # remove o ultimo valor, caso indique, remove no endereço indicado
print(lista)

lista.append(10)
add = lista.pop()
del lista [-1] #deletar o ultimo sem saber o fim
print(lista)

lista.clear() #limpa toda a lista
print(lista)

lista.insert(0, 5) # adiciona em determinado espaço
print(lista)

#caso seja inserido em local alem do fim, é automaticamente colocado no espaço após o ultimo

list_a = [1,2,3]
list_b = [4,5,6]
list_c = list_a + list_b
print(list_c)
list_a.extend(list_b)
print(list_a)

'''
= em imutaveis - copia dados para variável
= em mutáveis - aponta para mesmo endereço de memória
'''

lista_a = ['Higor', 'Talita']
lista_b = lista_a
lista_a[0] = 'Nada'

print(lista_b)

lista_a = ['Higor', 'Talita']
lista_b = lista_a.copy() #copia valores da lista
lista_a[0] = 'Nada'

print(lista_b)

#for consegue atuar dentro de listas

for nome in lista_a:
	print(nome)

lista = ['Higor', 'Talita', 'Bagheera']
indices = range(len(lista))

for i in indices:
	print(i, lista[i])

#empacotamento - função utilizada para remanejo de listas
a, b, c  = lista
print(b)
nome1, *resto = lista
print(nome1)
# * - indicador de empacotamento, caso não selecione valores, gera uma lista vazia (ponteiro)
# _ - utilizar o underline em código indica por convenção que a variável não será utilizada

# Tuples - tipo de conjunto imutável, indicado por parênteses 

nomes = ('Higor', 'Talita', 'Bagheera')
print(nomes, type(nomes))
print(nomes[1])

#enumerate - função de enumeração de iteráveis

lista.append('Portugal')

print(enumerate(lista)) #é um iterador

for item in enumerate(lista):
	print(item)

# é possível o desempacotamento em enumrados utilizando for
for indice, nome in enumerate(lista):
	print(indice, nome)

# \t - executa o TAB em impressão

#round - função que executa o arredondamento de floats
import decimal #biblioteca de funções de cálculo de precisão

num_1 = 0.1
num_2 = 0.5
num_3 = num_1 + num_2

print(num_3) #aparentemente na versão 3.11.1 nã gera imprecisão
print(f'{num_3:.2f}')
print(round(num_3, 3)) # sempre irá cortar o zero na leitura

num_1 = decimal.Decimal(0.1)
num_2 = decimal.Decimal(0.5)
num_3 = num_1 + num_2

print(num_3) # gera imprecisão se não utilizadas strings

num_1 = decimal.Decimal('0.1')
num_2 = decimal.Decimal('0.5')
num_3 = num_1 + num_2

print(num_3) # gera imprecisão se não utilizadas strings
print(f'{num_3:.2f}')
print(round(num_3, 2)) # utilizando função Decimal, gera efeito esperado

#split - divide uma string em uma lista(sem determinação, separa a string nos caractéres invisiveis)

frase_1 = 'Vou conseguir fazer dar certo!'
print(frase_1.split())
frase_2 = 'E, não conseguir, não é uma opção.'
print(frase_2.split(',')) #utiliza o caractére selecionado para executar a separação, e exclui o mesmo

for i, frase in enumerate(frase_2.split(',')):
	print(frase_2.split(',')[i])

for i, frase in enumerate(frase_2.split(',')):
	print(frase_2.split(',')[i].strip())#strip - executa a retirada de espaços iniciais e finais de uma string
#strip pode ser definido como rstrip ou lstrip, definindo de qual lado se cortara os espaços

#join - une uma lista de strings, utilizando o valor determinado

frase_3 = frase_1 + ' ' + frase_2
print(frase_3)

frase_3 = frase_3.split('!')
print(frase_3)

frase_fim = '!'.join(frase_3)
print(frase_fim)

# listas dentro de listas

dados = [
	[1, 5, 4],
	[2,3],
	[7,9,6,(0,8)]
]

print(dados)
print(dados[0])
print(dados[0][2])
print(dados[2][3][1])


for dado in dados:
	print(f'dados{dado}')
	for item in dado:
		print (item)

#desempacotadmento seletivo - pode-se selecionar com o * a quantidade de itens a isolar, dependendo de quantos itens selecionar após
lista = ['Maria', 'Helena', 1, 2, 3, 'Eduarda']
a, b, *_, c = lista 
print(a, c)
print(_)


for i in lista:
	print(i, end = ' ')
print(end = '\n')

# * - nesse caso, imprime a lista de acordo com seu conteudo e separando cada item por espaços, igual for acima
print(*lista) 

# nesse caso, é considerado cada item da string um vetor em separado, atuando a regra e gerando espaços entre eles
string  = 'ABCD'
print(*string) 

#nesse caso, demosntra funcioanlidade também com tuples
tuplas = 'Higor', 'S2', 'Talita'
print(*tuplas)

print(*dados, sep = '\n') #demonstração em matrizes

#operação ternária - condicional em linha (<valor1> if <condição>/ else <valor2>)
print('Valor' if True else 'Outro Valor')
#podem ser gerados outros valores em linha para execução de multiplas condicionais
#print('Valor1' if True else 'Valor2' if True else 'Fim')

