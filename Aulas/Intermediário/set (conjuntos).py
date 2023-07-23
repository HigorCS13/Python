# set -  conjunto em python
# set - são mutáveis, porém só aceitam tipos imutáveis com valor interno

s1 = set('Higor')
print(s1, type(s1))

#criação de set
#set(iterável) ou {1,2,3} #não é um dicionário

s1 = {'Higor'}
print(s1)
s1 = {'Higor', 1,2,3}
print(s1)
# set ocasionalmente entregam valores desordenados

s1 = { 1, 2, 3, 3, 3, 3, 3, 1}
print(s1)
# set eleimina valores duplicados na sua representação

l1 = [1, 2, 3, 3, 3, 3, 3, 1]
s1 = set(l1)
l2 = list(s1)
print(l1)
print(s1)
print(l2)
# set entrega sempre valores sem duplicação

# - seus valores sempre serão únicos
# - não aceitam valores mutáveis
# - não garatem ordem
# - são iteráveis (for, in, not in)
# - não tem índicies

'''
Metodos úteis
 - add
 - update
 - clear
 - discard
'''
s1.clear() #limpa o conjunto
print(s1)
print()
s1.add('Higor') #adiciona valor, um por vez
print(s1)
print()
s1.update('olá mundo!') # adiciona de modo iterável, para evitar separações, adicione em tuples
print(s1)
print()
s1.discard('o') #descarta o elemento mencionado
print(s1)
print()

'''
Operadores úteis
 - | : union
 - & : intersection
 - - : difference (presentes apenas no da esquerda)
 - ^ : symetric_difference(não intercedem)
'''

s1 = {1,2,3,4}
s2 = {3,4,5,6}

s3 = s1 | s2 #s1.union(s2)
print(s3)
print()
s3 = s1 & s2 #s1.intersection(s2)
print(s3)
print()
s3 = s1 - s2 #s1.difference(s2)
print(s3)
print()
s3 = s1 ^ s2 #s1.symmetric_difference(s2)
print(s3)
print()

