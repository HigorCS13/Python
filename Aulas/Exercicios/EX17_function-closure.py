
#Adiamento de função

def soma(x, y):
    return x + y

def multiplica(x, y):
    return x * y

def executar(funcao, *args):
    def calcula(*numeros):
        return funcao(*args, *numeros)
    return calcula

soma_com_cinco = executar(soma, 5)
multiplica_por_dez = executar(multiplica, 10)

numeros = input('Insira números: ')
numeros = numeros.split()

for numero in numeros:
    print(soma_com_cinco(int(numero)))
    print(multiplica_por_dez(int(numero)))
	