def zipper (lista1, lista2):
    intervalo = min(len(lista1), len(lista2))
    return [
        lista1[i] + lista2[i] for i in range(intervalo)
	]


lista1 = [1, 2, 3, 4, 5, 6, 7]
lista2 = [1, 2, 3, 4]

print(zipper(lista1, lista2))
print()

lista_soma = [x + y for x, y in zip(lista1, lista2)] #utilizando zip para somar
print(lista_soma)


# utilizando zip-longest

from itertools import zip_longest
 
lista_a = [10, 2, 3, 4, 5]
lista_b = [12, 2, 3, 6, 50, 60, 70]
lista_soma = [x + y for x, y in zip_longest(lista_a, lista_b, fillvalue=0)] # usar "fillvalue" como 0, assim capturando os valores restantes da lista maior, sem obter um erro no programa
print(lista_soma)