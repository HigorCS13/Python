import copy
import pprint

def p(v):
	pprint.pprint(v, sort_dicts=False, width=40)

produtos = [
    {'Nome' : 'Produto 5', 'Preço' : 10.00},
    {'Nome' : 'Produto 1', 'Preço' : 22.32},
    {'Nome' : 'Produto 2', 'Preço' : 10.11},
    {'Nome' : 'Produto 3', 'Preço' : 105.87},
    {'Nome' : 'Produto 4', 'Preço' : 69.90}
]

p('Aumentado em 10%')
print()
novos_produtos = [
	{'Nome' : produto['Nome'], 'Preço' : round(produto['Preço'] * 1.1, 2)}
	for produto in copy.deepcopy(produtos)
	]

p(novos_produtos)
print()

p('Ordenador por nome decrescente')
print()
produtos_ordenados_por_nome = sorted(
     copy.deepcopy(novos_produtos),
      key = lambda item : item['Nome'],
       reverse = True
	   )

p(produtos_ordenados_por_nome)
print()

p('Ordenado por preço crescente')
print()
produtos_ordenados_por_preco = sorted(copy.deepcopy(novos_produtos), key = lambda item : item['Preço'])

p(produtos_ordenados_por_preco)
print()

p('Original')
print()
p(produtos)
print()