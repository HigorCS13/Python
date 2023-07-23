# Exercicio - Salve sua classe em JSON
# Salve os dados da sua classe em JSON e depois crie novamente as intâncias
# Faça arquivos separados

import json

CAMINHO_ARQUIVO = 'C:\\Users\\Higor\\Desktop\\Higor\\Programação\\Python\\Aulas\\Exercicios\\EX21_class-json\\EX21.json'

class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        
p1 = Pessoa('Higor', 33)
p2 = Pessoa('Talita', 25)
p3 = Pessoa('Bagheera', 3)

bd = [vars(p1), p2.__dict__, vars(p3)]

def fazer_dump(): #envolver em uma função para adiar execução
    print('FAZENDO DUMP')
    with open(CAMINHO_ARQUIVO, 'w') as arquivo:
	    json.dump(bd, arquivo, ensure_ascii=False, indent=2)

# método em que se faz um limitador de execução da função, somente ativando se a mesma for o 'main'
if __name__ == '__main__':
     print ('Ele é o __main__')
     fazer_dump()
