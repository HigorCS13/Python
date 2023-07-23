print (1+1)

#comentário em linha singular

"""
"comentário" 
em 
múltiplas 
linhas
(DocString)(também podem ser ''' x ''')
"""
print (123)
print(12,34)
print(56,78)
print(12,34, end="##")#end - serve para alterar o final da exibição dos dados (por padrão '\n')
print(56,78, sep='|')#sep - serve para alterar o separador (indicado pela vírgula) de dados
#\r \n -> CRLF
#\n -> LF

#strings (str) = textos (dentro de aspas)

#aspas simples
print('Higor')
print("'Higor'")

#aspas duplas
print("Higor")
print('"Higor"')

#escape - serve para excluir a interpretação funcional de algum símbolo
print("Higor \" Cunha")

#r - revela escapes
print(r"Higor \" Cunha\"")

#int - números inteiros, positivos e negativos (sem sinal é considerado positivo)
print(11)
print(-11)
print(0)

#float - números decimais, positivos e negativos, separados por ponto (sem sinal é considerado positivo)
print(1.1)
print(0.0, 10.5)
print(-9.1, -1.5)

#type - indica classe do que foi selecionado
print(type('Higor'))
print(type(1))
print(type(1.9))

#bool - questionador lógico (True, False)
#== - operador lógico
print(10==10)
print(10==11)
print(type(10==11))

#polimorfismo - capacidade dinâmica da linguagem de executar múltiplas funções com o mesmo simbolizador de execução
#tipagem forte - a linguagem não permite execução de funções em tipos diferentes
print(1 + 1)


#conversão de tipos - executa a mudança para melhor adequação em função
print('1', type('1'))
print(int('1'), type(int('1')))

#booleano - em python, sem caractere é considerado False, com é considerado True
print(bool(''))
print(bool(' '))

#variáveis - podem ser criadas apenas escrevendo as mesmas e dando seu valor determinado
nome_completo = 'Higor Cunha Silva'
print(nome_completo)

adicao = 10 + 10
print('Adição:', adicao)

subtracao = 5 - 10
print('Subtrção:', subtracao)

multiplicacao = 10 * 10
print('Multiplicação:', multiplicacao)

divisao = 10 / 2  #sempre float
print('Divisão:', divisao)

divisao_int = 10 // 2 #divisão inteira
print('Divisão:', divisao_int)

exponenciacao = 2 ** 10
print('Exponenciação:', exponenciacao)

modulo = 55 % 2  #resto da divisão
print('Módulo:', modulo)

#a partir de certas comparações, booleano se ativa automaticamente, e atua no comparativo
print(modulo == 0)

#por ter tipagem forte, é possível executar concatenação e repetição com strings e sinais operacionais de soma e multiplicação
print('a' + 'b')
print( 'A' * 10)
print('Luiz' * 3)

#precedencia de operadores - os cálculos funcionam igual matemática básica

#f-string - permite a formatação de strings, sendo utilizado {} para definir as variáveis.
#para arredondamento de números float, utiliza-se a terminação :.nf, sendo 'n' o número de casas desejadas para exibição
nome = 'Higor'
altura = 1.85
peso = 100
imc = peso/(altura**2)
linha = f'{nome}, você tem {altura}m de altura, pesa {peso}kg, e seu IMC é {imc:.2f}'
print(linha)

#.format -  Função/método utilizada dentro de uma string, que serve para manipulação interna de vetores
a = 'A'
b = 'BB'
c = 1.1

formato = 'a = {0} b = {1} c {2:.2f}'.format(a,b,c)
print(formato)

#input - função de captação de dados do tipo string
nome = input ('Qual seu nome? ')
print(f'Seu nome é {nome}')

num_1 = input ('Digite um número: ')
num_2 = input ('Digite outro número: ')

int_num_1 = int(num_1)
int_num_2 = int(num_2)

print (f'A soma dos números é: {int_num_1 + int_num_2}')

