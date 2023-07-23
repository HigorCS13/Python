'''
class - Classes são moldes para criar novos objetos

As classes geram novos objetos (instâncias) que podem ter seus próprios atributos e métodos.

	atributos - propriedades, dados dentro da classe

	métodos - funções, ações dentro da classe

Os objetos gerados pela classe podem usar seus dados ingternos para realizar várias ações.

Por convenção, usamos PascalCase para nomes de classes

Hard coded - tudo aquilo que é determinado diretamente no código

'''
string = 'Higor' #str
print(string.upper())
print(isinstance(string, str))
print()


class Pessoa: # comando básico de geração de classes
    def __init__(self, nome, sobrenome): #__init__ - inicia o método
        # self - entrega variável na chamada como comando de método
        self.nome = nome
        self.sobrenome = sobrenome

p1 = Pessoa('Higor', 'Cunha')
#p1.nome = 'Higor'
# p1.sobrenome = 'Cunha'

p2 = Pessoa('Talita', 'Ribeiro') # sempre que a classe é chamada, uma nova instância (obejto) é criada
# p2.nome = 'Talita'
# p2.sobrenome = 'Ribeiro'

print(p1) #como padrão, entrega módulo, classe e endereço
print(p2) #como padrão, entrega módulo, classe e endereço
print()

print(p1.nome)
print(p1.sobrenome)
print()

print(p2.nome)
print(p2.sobrenome)
print()

class Carro:
    def __init__(self, nome):
        self.nome = nome
    def acelerar(self):
        print(f'O {self.nome} está acelerando...')


fusca = Carro('Fusca')
print(fusca.nome)

print()

celta = Carro('Celta')
print(celta.nome)
celta.acelerar()

print()
# self - referência a própria instância, sendo a variável, por convenção do python

class Animal:
    def __init__(self, nome):
        self.nome = nome

        variavel = 'valor'
        print(variavel)
    
    def comendo(self, alimento):
        return f'O {self.nome} esta comendo {alimento}'
    
    def executar(self, *args, **kwargs): # pode-se executar funções chamando outras funções dentro das classes
        return self.comendo(*args, **kwargs)

leao = Animal('Leão')

print(leao.nome)
print(leao.executar('Zebra'))
print()

class Camera:
    def __init__(self, nome, filmando = False):
        self.nome = nome
        self.filmando = filmando
    
    def filmar(self):
        if self.filmando:
            print(f'{self.nome} JÁ está filmando!')
            return
        print(f'{self.nome} está filmando...')
        self.filmando = True # variaveis booleanas podem ser mantidas dentro de classes
    
    def parar_filme(self):
        if not self.filmando:
            print(f'{self.nome} NÃO está filmando!')
            return
        print(f'{self.nome} está parando de filmar...')
        self.filmando = False
    
    def fotografar(self):
        if self.filmando:
            print(f'{self.nome} NÃO pode fotografar filmando!')
            return
        print(f'{self.nome} está fotografando...')
        

c1 = Camera('Canon')
c2 = Camera('Sony')

print(c1.filmando)
print(c2.filmando)

print()

c1.filmar()
c1.filmar()

print()

print(c1.filmando)
print(c2.filmando)

print()

c2.filmar()
c2.fotografar()
c2.parar_filme()
c2.parar_filme()
c2.fotografar()

print()


class Pessoa:

    ano_atual = 2023 # Atributos de Classe

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
    
    def get_ano_nascimento(self):
        return Pessoa.ano_atual - self.idade
    
    @classmethod #decorator
    def metodo_de_classe(cls): # métdod de classe
        print('Hey')

# factories method
    @classmethod
    def criar_com_60_anos(cls, nome): # cls se torna um buscador da classe inteira
        return cls(nome, 60)
    
    @classmethod
    def criar_anonimo(cls, idade): # cls se torna um buscador da classe inteira
        return cls('Anônimo', idade)
    
p1 = Pessoa('Higor', 33)
p2 = Pessoa('Talita', 25)

print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())

# __dict__ e vars para atrinutos e instâncias

print()

print(vars(p1)) # vars - mostra o dicionário (__dict__) existente do objeto selecionado

print()

p1.__dict__['Altura'] = 1.85 # __dict__ pode ser alterado
print(p1.__dict__)
print()

del p1.__dict__['Altura']
print(p1.__dict__)
print()

dados = {'nome': 'Bagheera', 'idade': 3} # para que seja possivel executar as chaves deves ser iguais aos métodos

p3 = Pessoa(**dados)
print(vars(p3))
print()

# Métodos de calsse + factories (fábricas)
# são métodos onde "self" será "cls", ou seja, ao invés de receber a instância no primeiro parâmetro, recebemos a própria classe
#

print(Pessoa.ano_atual)

Pessoa.metodo_de_classe()
p4 = Pessoa.criar_com_60_anos('Jether')
print(vars(p4))

p5 = Pessoa.criar_anonimo(50)
print(vars(p5))
print()
# Métodos estáticos, segundo professor, são inúteis em python
# @staticmethod - são métodos que estão dentro da classe, mas não tem acesso nem ao self, nem cls, sendo apenas funções internas

class Teste:
    @staticmethod
    def funcao_static(*args, **kwargs):
        print('Oi', args, kwargs)

teste1 = Teste()
teste1.funcao_static(1,2,3,nome=4) #percebe-se na execução que não nomeados entram em lista, e nomeados entram em dicionário

# method - self, método de instância
# @classmethod - cls, método de classe
# @staticmethod - método estatico (função simples)

class Connection:
    def __init__(self, host = 'localhost'):
        self.host = host
        self.user = None
        self.password = None

        # method
    def set_user(self,user):
        # setter
        self.user = user
    
    def set_password(self,password):
        self.password = password
    
    @classmethod
    def create_with_auth(cls, user, password):
        connection = cls()
        connection.user = user
        connection.password = password
        return connection
    
    @staticmethod
    def log(msg):
        print('LOG:', msg)



print(Connection.log('Mensagem de início'))

c1 = Connection()
c1.set_user('Higor')
c1.set_password('123')
print(vars(c1))

c2 = Connection.create_with_auth('Talita', '1234')
print(vars(c2))
print()

# @property - um getter no modo Pythônico

# getter - um método para obter um valor

# cor -> get_cor()

# modo pythônico - modo do Python de fazer coisas


class Caneta:
    def __init__(self, cor):
        self.cor_tinta = cor
        self._cor = self.cor_tinta # ajuste para simbolizar atributo inalterável
        self._cor_tampa = None # atributo sem declaração

# POR CONVENÇÃO, CASO VEJA UNDERLINE NO INICIO DO ATRIBUTO, NÃO DEVE SER MODIFICADO

    def get_cor(self):
        print('GET COR')
        return self.cor_tinta
    
    @property # método apenas executa ações, não sendo possível mudar os atributos
    def cor(self): #método utilizado para adaptação em código
        print('PROPERTY')
        return self.cor_tinta

    @cor.setter # utilizado para alterar valores dentro de property
    def cor(self, cor):
        print('Nova cor:', cor)
        self.cor_tinta = cor

    @property
    def cor_tampa(self):
        return self._cor_tampa
    
    @cor_tampa.setter
    def cor_tampa(self, cor):
        self._cor_tampa = cor

caneta = Caneta('Azul')
print(caneta.get_cor()) #método getter padrão
print()

# @property é uma propriedade do objeto, ela é um método que se comporta como um atributo, então não salva valor

# Geralmente é usada nas seguintes situações:
# - como getter
# - p/ evitar quebrar código cliente
# - p/ habilitar setter
# - p/ executar ações ao obter um atributo
# Código cliente - é o código que usa seu código

# @property + @setter = getter e setter em Python

print(caneta.cor) #método property
print()
caneta.cor = 'Vermelho'
print()
print(caneta.cor)
print()

print(caneta.cor_tampa)
caneta.cor_tampa = "Preto"
print(caneta.cor_tampa)
print()
# Encapsulamento (modificadores de acesso: public, protected, private)

# Python NÃO TEM modificadores de acesso, tudo é feito por convenção (PEP8)

# Mas podemos seguir as seguintes convenções
#   (sem underline) = public
#       pode ser usado em qualquer lugar

# _ (um underline) = protected
#       não DEVE ser usado fora da classe ou suas subclasses.

# __ (dois underlines) = private
#       "name mangling" (desfiguração de nomes) em Python
#       _NomeClasse__nome_attr_ou_method
#       só DEVE ser usado na classe em que foi declarado.

from functools import partial # ctrl + clicar = acessar o código da função

class Foo:
    def __init__(self):
        self.public = 'isso é público'
        self._protected = 'isso é protegido'
        self.__private = 'isso é private'

    def metodo_publico(self):
        print(self.__private)
        print(self.__metodo_private())
        return 'método_público'
    
    def _metodo_protected(self):
        return '_método_protected'
    
    def __metodo_private(self):
        return '__método_private'

f = Foo()
print(f.public)
print(f.metodo_publico())
print()

# PROTECTED E PRIVATE NÂO DEVEM SER USADOS DESSA FORMA!!!!

print(f._protected) # não deveria ser acessado dessa forma
print(f._metodo_protected()) # não deveria ser acessado dessa forma
print()
print(f._Foo__private) # acesso a um método private por name mangling
print(f._Foo__metodo_private()) # acesso a um método private por name mangling
print()


# RELAÇÕES ENTRE CLASSES: ASSOCIAÇÃO, AGREGAÇÃO E COMPOSIÇÃO (lembrando que "Associação C Agregação C composição")

# Associação é um tipo de relação onde os objetos estão ligados dentro do sistema.

# Essa é a relação mais comum entre objetos e tem subconjuntos como agregação e composição (que veremos depois).

# Geralmente, temos uma associação quando um objeto tem um atributo que referencia outro objeto.

# A associação não especifica como um objeto controla o ciclo de vida de outro objeto.

class Escritor:
    def __init__(self, nome):
        self.nome = nome
        self._ferramneta = None

    @property
    def ferramenta(self):
        return self._ferramneta
    
    @ferramenta.setter
    def ferramenta(self, ferramenta):
        self._ferramneta = ferramenta
  
class Ferramenta:
    def __init__(self,ferramenta):
        self.ferramenta = ferramenta

    def escrever(self):
        return f'{self.ferramenta} esta escrevendo'
    
escritor = Escritor('Higor')
caneta = Ferramenta('Caneta Azul')
maquina = Ferramenta('Máquina de escrever')

escritor.ferramenta = caneta # Associação
print(caneta.escrever())

escritor.ferramenta = maquina # Associação
print(escritor.ferramenta.escrever())

print()

# Agregação é uma forma mais especializada de associação entre dois ou mais objetos. Cada objeto terá seu ciclo de vida independente.

# Geralmente é uma relação de um para muitos, onde um objeto tem um ou muitos objetos.

# Os objetos podem viver separadamente, mas pode se tratar de uma relação onde um objeto precisa de outro para fazer determinada tarefa.

# EXISTEM controvérsias sobre as definições de agregação.

class Carrinho:
    def __init__(self):
        self._carrinho = []
    
    def total(self):
        return sum([p.preco for p in self._carrinho])
    
    def inserir_produto(self, *produtos):
        #self._carrinho.extend(produtos) - extend = funciona como um adicionador de listas
        #self._carrinho += produtos
        for produto in produtos:
            self._carrinho.append(produto)

    def listar_produtos(self):
        for produto in self._carrinho:
            print(produto.nome, produto.preco)

class Produto:
    def __init__(self, nome, preco):
        self.nome = nome
        self.preco = preco

carrinho = Carrinho()
p1, p2 = Produto('Camisa', 10), Produto('Calça', 15) # Agregação
carrinho.inserir_produto(p1, p2)
carrinho.listar_produtos()
print(carrinho.total())
print()

# Herança = Associação + Agregação
# Composição = Composição

# Composição é uma especialização da agregação.

# Mas nela, quando o objeto "pai" for apagado, todas as referências dos objetos filhos também são apagadas.

class Cliente:
    def __init__(self, nome):
        self.nome = nome
        self.enderecos = []
    
    def inserir_endereco(self, rua, numero):
        self.enderecos.append(Endereco(rua, numero)) # Composição

    def listar_enderecos(self):
        for endereco in self.enderecos:
            print(endereco.rua, endereco.numero)

    def inserir_endereco_externo(self, endereco):
        self.enderecos.append(endereco)

    def __del__(self):
        print('Apagando', self.nome)


class Endereco:
    def __init__(self, rua, numero):
        self.rua = rua
        self.numero = numero

cliente1 = Cliente('Higor')
cliente1.inserir_endereco('Porto', 89)
print(cliente1.nome)
cliente1.listar_enderecos()
print()

cliente1 = Cliente('Talita') # Quando Classe "mãe" é deletada suas composições são tambem deletadas
print(cliente1.nome)
cliente1.listar_enderecos()
print()

# cliente2 = Cliente('Bagheera')
endereco_externo = Endereco('Rua Esmeralda', 57)
# cliente2.inserir_endereco_externo(endereco_externo)
# print(cliente2.nome)
# cliente2.listar_enderecos()
print()

del cliente1

print ('Fim dos endereços?')

print(endereco_externo.rua, endereco_externo.numero) # quando criado externamente, permanece acessivel
print()
'''
Herança simples - Relação entre classses

Associçaõ - Usa
Agregação - Tem
Composição - É dono
Herança - É um

    Herança ou Composição

Classe principal (Pessoa)
    -> super class, base class, parent class

Classe filhas (Cliente)
    -> sub class, child class, derived class

'''

class Obj:
    ...
help(Obj)
print()

class Pessoa_base: #super class
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome
    
    def falar_classe(self):
        print('Classe Pessoa')
        print(self.nome, self.sobrenome, self.__class__.__name__)

class Cliente_base(Pessoa_base): #sub class (herança)
    def falar_classe(self):
        print('Classe Cliente')
        print(self.nome, self.sobrenome, self.__class__.__name__)

class Aluno_base(Pessoa_base): #sub class
    ...

c1 = Cliente_base('Higor', 'Cunha')
a1 = Aluno_base('Talita', 'Riberio')

c1.falar_classe() # chamada possui função
print()
a1.falar_classe() # chamada chama função de Pessoa

print()

#   method resolution order - sequência de busca de resolução da classe

# help(Pessoa_base)
# print()
# help(Cliente_base)

# UTILIZAR CADEIAS DE HERANÇA DE NO MÁXIMO 3 A 4 NÍVEIS

# super() é a super classe na sub classe

class Minha_Str(str): # herança da classe str
    def upper(self):  # sobreposição de clases
        print('Chamou .upper()') # deve-se ter atenção a alteração de funções existentes, pois a primeira busca é interna
        return super().upper() # chama a função da super classe

nome = Minha_Str('Higor')

print(nome.upper()) # utiliza todas as funções existentes na classe herdada
print()

class A:
    atributo_a = 'valor a'
    
    def __init__(self, atributo): # utilizar init na classe principal exige a inclusão dos valores
        self.atributo = atributo

    def metodo(self):
        print('A')

class B(A):
    atributo_b = 'valor b'
    
    def __init__(self, atributo, outra_coisa): # utilizando init na sub classe, deve-se alimentar a classe principal, mas pode-se também incluir novos valores
        super().__init__(atributo)
        self.outra_coisa = outra_coisa

    def metodo(self):
        print('B')

class C(B):
    atributo_c = 'valor c'
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        print('SISTEMA BURLADO') # prática de chamada completa para evitar erros 

    def metodo(self):
        super(B, self).metodo() # utilizando definições internas em super, pode-se buscar a função diretamente na classe mais elevada
        super().metodo()
        print('C')

c = C('Atributo', 'Qualquer')

print(c.atributo_a)
print(c.atributo_b)
print(c.atributo_c)
c.metodo()
print()

print(C.mro()) # função base de method resolution order, para observar a sequência de chamadas
print()

print(c.atributo, c.outra_coisa)
print()

# Herança Múltipla - Python Orientado a Objetos

# Quer dizer que no Python, uma classe pode estender várias outras classes.

# Herança simples:
    # Animal -> Mamifero -> Humano -> Pessoa -> Cliente

# Herança múltipla e mixins
    # Log -> FileLog
    # Animal -> Mamifero -> Humano -> Pessoa -> Cliente
    # Cliente(Pessoa, FileLog)


    # Problema do Diamante
# A, B, C, D
# D(B, C) - C(A) - B(A) - A

# método -> falar
#           A
#         /   \
#        B     C
#         \   /
#           D

# Python 3 usa C3 superclass linearization para gerar o mro.
# Você não precisa estudar isso (é complexo)
# https://en.wikipedia.org/wiki/C3_linearization

# Para saber a ordem de chamada dos métodos
# Use o método de classe Classe.mro()
# Ou o atributo __mro__ (Dunder - Double Underscore)

class K:
    ...
    def quem_sou(self):
        print('K')

class X(K):
    ...
    # def quem_sou(self):
    #     print('X')

class Y(K):
    ...
    def quem_sou(self):
        print('Y')

class Z(X, Y):
    ...
    # def quem_sou(self):
    #     print('Z')

z = Z() # vai buscar sempre em sequencia, segundo mro()
z.quem_sou()

# Classes abstratas - Abstract Base Class (abc)

# ABCs são usadas como contratos para a definição de novas classes. Elas podem forçar outras classes a criarem métodos concretos. Também podem ter métodos concretos por elas mesmas.

# @abstractmethods são métodos que não têm corpo.

# As regras para classes abstratas com métodos abstratos é que elas NÃO PODEM ser instânciadas diretamente.

# Métodos abstratos DEVEM ser implementados nas subclasses (@abstractmethod).

# Uma classe abstrata em Python tem sua metaclasse sendo ABCMeta.

from abc import ABC, ABCMeta, abstractmethod

class Log(ABC): #para a criação de classe abstrata, classe criada herda de ABC, pode ser também (metaclass = ABCMeta)
    
    @abstractmethod #abstração de método oficial
    def _log(self, msg):
        ...

    def log_error(self, msg):
        return self._log(f'Error: {msg}')
    
    def log_success(self, msg):
        return self._log(f'Success: {msg}')

class LogPrintMixin(Log):
	
	def _log(self, msg):
		print (f'{msg} ({self.__class__.__name__})')
                
l = LogPrintMixin()

l.log_error('opa')

# É possível criar @property @setter @classmethod @staticmethod e @method como abstratos, para isso use @abstractmethod como decorator mais interno.
print('\n')
# Foo - Bar são palavras usadas como placeholders (pode ser qualquer coisa).

class AbstractFoo(ABC):

    def __init__(self, name):
        self._name = None
        self.name = name
    
    @property
    @abstractmethod # criando property abstrato (sempre mais interno)
    def name(self):
        ...
    

class Foo(AbstractFoo):

    # name = '' # serviria ao inves da criação dos property / setters abaixo, porém trava a criação de logicas
    
    def __init__(self, name):
        super().__init__(name)

    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, name):
        self._name = name

foo = Foo('Bar')

print(foo.name)

# Utilizando @abstractmethod em setter

class AbstractFoo2(ABC):

    def __init__(self, name):
        self._name = None
        self.name = name
   
    @property
    def name(self):
        return self._name
    
    @name.setter
    @abstractmethod
    def name(self, name):
        ...

class Foo(AbstractFoo2):

    def __init__(self, name):
        super().__init__(name)

    @AbstractFoo2.name.setter #defini-se o setter com referencia a classe super
    def name(self, name):
        self._name = name

foo = Foo('Foo')

print(foo.name)