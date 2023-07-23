# if / elif / else - condicionais se / se não se / se não, finalizada com ':'
# A separação de pertencentes de cada função, em Python, se da por TAB

entrada = input ('[E]ntrar ou [S]air? ')
senha_digitada = input('Senha: ')
senha = '123456'

if (entrada == 'E' or entrada == 'e') and (senha_digitada == senha):
	print('Você entrou no Sistema.')
elif (entrada == 'S' or entrada == 's'):
	print('Você saiu do Sistema.')
else:
	print('N/A')


# debuguer - serve para observar passo a passo o código debugado.

# python -i xxx.py - inicia o arquivo em shell para atuação

# and - função de adição as condicionais, e todas necessitam ser verdadeiras

# or - função de adição as condicionais, e a primeira a  ser verdadeira é considerada

# not - função de inversão de valores booleanos

# in - função contém, usada para citação em, valores iteráveis (vetores)

# not in - função não contém

# utilizar valores negativos dentro de uma chamada de vetores indica a movimentação reversa de busca

nome = 'Higor'
print(nome[2])
print(nome[-3])

print ('g' in nome)
print ('g' not in nome)

# Interpolação - Função de direcionamento de variáveis dentro de uma string
'''
s - string
d, i - int
f - float
x, X - hexadecimal (ABCDEF0123456789)
>, < - preenchimento de caracteres para as laterais
^ - preenchimento lateral de caracteres por igual, centralizando a string na maior possibilidade
= - força a inserção de caracteres no inicio da string
pode-se utilizar, após os dois pontos divisores, o caractere que deseja inserir
Sinais - utiliza-se + ou - para demonstração inicial de positivo ou negativo, para o mesmo, deve-se definir após os dois pontos em um número inteiro
'''

valor = 1000.89765
texto = '%s, o preço é R$ %.2f' %(nome, valor)

print(texto)

var = 'ABC'
print(f'{var}')
print(f'{var: >10}.') #preenche a esquerda
print(f'{var: <10}.') #preenche a direita
print(f'{var:-^9}.') #preenche ao centro
print(f'{1000.48997855332:+,.2f}') #insere "+" para indicação de positivo e "," para divisão de milhar, além de arredondar para duas casas
print(f'{1000.48997855332:0=+5,.2f}') #insere "+" para indicação de positivo, "0" cinco vezes (utilizando o sinal de igual), "," para divisão de milhar, além de arredondar para duas casas

''' Fatiamento de string

Utilizado para busca interna de uma determinada string

positivos -  (012345678)
negativos - -(987654321)

variável[início:fim]

len - função de contagem de caracteres

passo - terceiro argumento indicado dentro de uma busca, indica a frequencia de busca
variável[início:fim:passo]

toda abstenção de informação é caracterizada como máximo ou mínimo de busca possível
'''

var = 'Olá Mundo'

print(var)
print(var[1]) #busca padrão
print(var[-8]) #busca negativa
print(var[4:]) #início
print(var[:4]) #fim
print(var[1:7]) #início:fim
print(var[-8:-2]) #início:fim (negativo)
print(len(var)) #contador
print(var[::2]) #passo
print(var[::-2]) #passo negativo

'''
 Introdução try/except
try - tenta executar código
except - executa, caso try possua erro
'''

num_str = input('Digite um número: ')

try:
	print('STR: ', num_str)
	num_float = float(num_str)
	print('FLOAT: ', num_float)
	print(f'O dobro de {num_str} é {num_float * 2:.2f}')
except:
	print('Isso não é um número!')
