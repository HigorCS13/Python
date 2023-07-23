'''
Módulos Padrão

inteiro - import nome_modulo

vantagens - toda a funcionalidade do modulo ativa
desvantagens - por vezes, nomes exagerados
'''

import sys

print(sys.platform)

'''
partes - from nome_modulo import obj1, obj2

vantagens - nomes menores
desvantagens - sem namespace do modulo, podendo gerar sobrinscrição
'''
from sys import exit, platform

print(platform)
'''
alias 1 - import nome_modulo as n_m

vantagens - diminuir nomes extensos
desvantagens - pode gerar falta de padrão na linguagem
'''
import sys as s

print(s.platform)
'''
alias 2 - form nome_modulo import obj1 as n, obj2 as m

vantagens - diminuir nomes extensos
desvantagens - pode gerar falta de padrão na linguagem
'''
from sys import platform as plf

print(plf)
'''
Má pratica - from nome_modulo import * (import all)

vantagens - importa todos os comando de um módulo
desvantagens - importa tudo do módulo
'''

'''
Entendendo módulos prórpios em Python
	o primeiro módulo executado chama-se __main__
    você pode importar outro módulo inteiro ou parte dele
    o Python reconhece o módulo onde o __main__ está e as pastas abaixo dele
    ele não reconhece pastas e módulos acima do __main__ por padrão
    o Python conhece todos os módulos e pacotes presentes nos caminhos sys.path 
'''
print('Módulo:', __name__)

#para arquivos de mesma pasta, é possível a importação

import teste_import # pode-se criar apenas funções e gerar módulos personalizados para cada serviço

print(teste_import.__name__)

try:
    sys.path.append('Users\Higor\Desktop\Higor\Programação\Python\Aulas\Introdução')
except:
    print('Não deu certo')

print(*sys.path, sep = '\n') # é uma lista

# Singleton - o Python, por padrão, não refaz a importação de um módulo, mesmo se citado novamente

import importlib #biblioteca que serve para recarregar a chamada de outra biblioteca em chamada

for i in range(10):
    print(i)
    importlib.reload(teste_import)

#pode-se criar uma importação de package, isto é, uma pasta com outros arqivos incluidos, e desde que respeite as regars de importação, poderão ser utilizadas dentro de outro programa

# __all__ - função criada dentro do módulo, em que se gera uma lista de seleções do que vai ser importado, por meio de strings

#todo direcionamento do package deve ser bem escrito para o funcionamento do import

import import_package.modulo_test

print(import_package.modulo_test.soma(1,2)) #pode executar resumos de importação tal qual exemplos acima

# __init__ - criando um arquivo com esse nome na pasta importada, se cria automáticamente um "módulo", pois executando o mesmo, pode-se acessar outras funções internas

import import_package

print(import_package.dobra(2))

# para acesso a outros arquivos em módulo, deve-se manter a importação direcionada vista acima

print(import_package.soma(3, 6))

# para adicionar funções de outros arquivos internos, pode-se adicionar primeitramente em __init__, gegrando um acesso interno

