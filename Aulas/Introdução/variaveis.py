'''
CONSTANTE (em maiúsculo) = "Variáveis que não vão mudar"
Muitas condições do tipo if(ruim)
	<- Contagem de complexidade (ruim)
SEMPRE TENTE SIMPLIFICAR, E ABUSE DE VARIÁVEIS!
'''
vel = 61 #velocidade do carro
loc_car = 90 #local onde esta

RADAR_1 = 60 #velocidade máxima radar 1
LOCAL_1 = 100 #local radar 1
RADAR_RANGE = 1 #distancia radar

if vel > RADAR_1:
	print('Carro ultrapassou a velocidade!')
if (LOCAL_1 >= loc_car >= RADAR_RANGE):
	print('Carro multado!')

'''
Flag - Marca um local
id = identidade
'''

v1 = 'a'
v2 = 'a'
#v2 = 'b'
print(id(v1))
print(id(v2))

'''
None = Não valor
is e is not = é ou não é (tipo, valor, id)
'''

c = False
if_true = None

if c:
	if_true = True
	print('faça algo')
else:
	print(if_true, if_true is None)
	print(if_true, if_true is not None)


#Valores imutáveis: são valores que não são possiveis de modificar internamente
str ='Higor'
print (str[3])

n_str = f'{str[:3]}ABC{str[4:]}'
print (n_str)

#utilizar . após a variável demonstra as várias funções possíveis de personalização dos objetos criados
