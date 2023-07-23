def zipper(lista1, lista2):
	intervalo_maximo = min(len(lista1), len(lista2))
	return [
		(lista1[i], lista2[i]) for i in range(intervalo_maximo)
	]

cidades = ['Salvador', 'Ubatuba', 'Belo Horizonte']
estado = ['BA', 'SP', 'MG', 'RJ']


print(cidades)
print(estado)
print()
print(zipper(cidades, estado))
print()


# zip - função existengte em sistema que executa justamente a função acima, entregando um iterator

print(list(zip(cidades, estado)))
print()

# zip-longest - função importada do módulo itertools, que executa a função contrária de zip, preenchendo com "None" caso não haja valor

from itertools import zip_longest

print(list(zip_longest(cidades, estado, fillvalue = 'SEM CIDADE'))) #fillvalue - preenche espaços vazios com valor determinado
print()

