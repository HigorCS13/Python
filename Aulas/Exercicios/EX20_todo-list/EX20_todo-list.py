import os
import json

def adiciona_tarefas(tarefa, lista=None):
	lista.append(tarefa)
	return lista 

def exclui_tarefas(numero, lista=None):
	if not lista:
		print('Nenhuma tarefa a excluir')# funcionalidade basica para indicar NA
		return
	else:
		del lista[int(numero) - 1]
		return lista

def imprime_tarefas(tarefas):
	print()
	if not tarefas:
		print('Nenhuma tarefa existente')# também conhecido como Guard Clause
		return
	for indice, nome in enumerate(tarefas):
		print(f'\t{indice + 1} {nome}', sep = ' - ')

def cria_funcao():
	funcao = input('Selecione uma função:\n(A)dicionar\n(E)xcluir\n(C)lear\n(F)inalizar\n')
	return funcao

def salvar(lista, caminho):
	dados = lista
	with open(caminho, 'w', encoding = 'utf-8') as arquivo:
		json.dump(lista, arquivo, ensure_ascii = False, indent = 1) 
	return dados

def ler(tarefas, caminho_arquivo):
    dados = tarefas
    try:
        with open(caminho_arquivo, 'r', encoding='utf8') as arquivo:
            dados = json.load(arquivo)
    except FileNotFoundError:
        salvar(tarefas, caminho_arquivo)
    return dados

CAMINHO = 'C:\\Users\\Higor\\Desktop\\Higor\\Programação\\Python\\Aulas\\Exercicios\\EX20_todo-list\\EX20.json'

tarefas = ler([], CAMINHO)
funcao = ''

while funcao != 'F':

	print()
	print('TO DO LIST')
	imprime_tarefas(tarefas)
	print()
	
	funcao = cria_funcao()

	if funcao == 'A' or funcao == 'a':
		tarefas = adiciona_tarefas(input('Escreva uma tarefa: '), tarefas)
		salvar(tarefas, CAMINHO)

	elif funcao == 'E' or funcao == 'e':
		try:
			indices = exclui_tarefas(int(input('Escolha um indice da tarefa para retirar: ')), tarefas)
			salvar(tarefas, CAMINHO)
		except IndexError:
			print('Índice inválido')

	elif funcao == 'C' or funcao == 'c':
		os.system('cls')
	
	elif funcao == 'F' or funcao == 'f':
		os.system('cls')
		print('Lista finalizada!')
		print()
		print('TO DO LIST')
		imprime_tarefas(tarefas)
		print()
		funcao = 'F'
	else:
		print('Função inválida!')
