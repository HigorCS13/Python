# Ambientes virtuais em Python (venv)
# Um ambiente virtual carrega toda a sua instalação
# do Python para uma pasta no caminho escolhido.
# Ao ativar um ambiente virtual, a instalação do
# ambiente virtual será usada.
# venv é o módulo que vamos usar para
# criar ambientes virtuais.
# Você pode dar o nome que preferir para um
# ambiente virtual, mas os mais comuns são:
# venv / env / .venv / .env

# O ambiente virtual serve para se adaptar a cada trabalho, cada um com sua caracteristica

'''
python -m venv venv(sendo esse último o nome da pasta) 
	-> para cria um ambiente virtual 

gmc python -Syntax 
	-> indica o caminho da pasta python

.\venv\Scripts\activate
	-> ativa ambiente virtual

(python -m) pip install/uninstall
	-> instalador/desinstalador de frameworks

pip freeze
	-> exibe frameworks instalados

pip index versions N==0.0
	-> seleciona versão especifica para instalar

pip index versions N --upgrade
	-> atualiza biblioteca especificada

pip freeze > requirements.txt
	-> gera arquivo .txt padrão indicando quais os libs atuais na venv em ação

pip install -r requirements.txt
	-> instala os arquivos listados em requirements

'''

'''-------------------------------------------------------------------'''

# Criando arquivos com Python + Context Manager with
# Usamos a função open para abrir
# um arquivo em Python (ele pode ou não existir)
# Modos:
# r (leitura), w (escrita), x (para criação)
# a (escreve ao final), b (binário)
# t (modo texto), + (leitura e escrita)
# Context manager - with (abre e fecha)
# Métodos úteis
# write, read (escrever e ler)
# writelines (escrever várias linhas)
# seek (move o cursor)
# readline (ler linha)
# readlines (ler linhas)

caminho = 'C:\\Users\\Higor\\Desktop\\Higor\\Programação\\Python\\Aulas\\Intermediário\\teste_file.txt'
# sempre que for utilizar o caminho completo, em windows, deve-se usar duas barras no lugar de uma

# METODO PADRÃO
# arquivo = open(caminho, 'w') # w (escrita)
# arquivo.close()
# # sempre fechar o arquivo após utilização para evitar corrupção do mesmo

# com a função with, o fechamento do arquivo se torna automático, evitando erros, e podendo também executar funções internas
with open(caminho, 'w+', encoding = 'utf-8') as arquivo:
	print('Olá mundo\n')
	arquivo.write('Linha 1\n') # escreve o texto desejado, em relação a posição do cursor
	arquivo.write('Linha 2\n')
	arquivo.writelines(
		('Linha 3\n', 'Linha 4\n', 'Atenção') # executa varias escritas
	) # 'Atenção', na escrita acima, sai de maneira diferente no arquivo, por causa do Encoding

	arquivo.seek(0,0) # move o cursor para a posição inicial, habilitando a leitura, por estar dentro da mesma função
	print(arquivo.read())
	print('Lendo por etapas:')
	arquivo.seek(0,0)
	print(arquivo.readline()) # executa algo parecido com a função next, lendo apenas a linha seguinte, de acordo com a posição do cursor

	print('READLINES como função:')
	for linha in arquivo.readlines():
		print(linha.strip()) # evita a sobrecarga de quebras de linha, podendo ser também end = ''

	print('função para abertura e fechamento automático do arquivo')

print()
# w - quando executado, ele faz a limpeza do arquivo selecionado e inclui o lhe foi solicitado em código.
# a - quando executado, escreve sempre ao fim do arquivo, não apagando suas informações anteriores

# para a inclusão de caractéres diferenciados, como acentuações, deve-se ter atenção ao padrão de Encode utilizado

# Vamos falar mais sobre o módulo os, mas:
# os.remove ou unlink - apaga o arquivo
# os.rename - troca o nome ou move o arquivo
# Vamos falar mais sobre o módulo json, mas:
# json.dump = Gera um arquivo json
# json.load

# para a utilização de json em Python, se utiliza import para importar como módulo
import json
import os

caminho = 'C:\\Users\\Higor\\Desktop\\Higor\\Programação\\Python\\Aulas\\Intermediário\\teste_file.json'

pessoa = {
	'nome' : 'Higor',
	'sobrenome' : 'Cunha Silva',
	'idade' : 33,
	'altura' : 1.85,
	'endereço' : [
		{'rua' : 'lugar1', 'numero:' : 123},
		{'rua' : 'lugar2', 'numero:' : 456}
	],
	'altura': 1.85,
	'números preferidos': (0,5,7,13),
	'Dev': True,
	'nada': None
}

with open(caminho, 'w', encoding = 'utf-8') as arquivo:
	json.dump(pessoa, arquivo, ensure_ascii = False, indent = 1) 

# ensure_ascii = False - codifica o arquivo json de maneira igual a escrita no código enviado
# indent = 1 - torna o json demonstrado mais legível

with open(caminho, 'r', encoding= 'utf-8') as arquivo:
	sujeito = json.load(arquivo)
	print(sujeito)
	print(type(sujeito))

print()
# json salva apenas dados, sendo poucos suportados

def adiciona_clientes(nome, lista=[]):
#em casos mutaveis, como a lista, caso não exista  e seja citada na criação da função, o Python entende a lista interna como a padrão
	lista.append(nome)
	return lista

cliente1 = adiciona_clientes('Higor')
adiciona_clientes('Talita', cliente1)
print(cliente1)

print()

cliente2 = adiciona_clientes('Filipe')
adiciona_clientes('Sabrina', cliente2)
print(cliente2)
# executando um segundo cliente na função, o mesmo se adiciona para dentro da lista interna da função
print()
#a resolução para esses casos é a criação de um mutável extreno, e a citação do mesmo como parametro, evitando o acumulo de dados

lista = []

cliente3 = adiciona_clientes('Bagheera', lista)
adiciona_clientes('Estrela', cliente3)
print(lista)

print()
# outro modo de resolver seria tornando a variavel em um imutavel None, e incluindo uma nova lista toda vez que ela permanecer assim

def adiciona_clientes2(nome, lista=None):
	if lista == None:
		lista = [] # gera uma nova lista a cada chamada
	lista.append(nome)
	return lista

cliente4 = adiciona_clientes2('Nome1')
adiciona_clientes2('Nome2', cliente4)
print(cliente4)

print()

cliente5 = adiciona_clientes2('Nome3')
adiciona_clientes2('Nome4', cliente5)
print(cliente5)


