try:
    a = 10
    b = 0
    print('linha 1')
    c = a / b
    print(b[0])
    print('linha 2')

except ZeroDivisionError:
    print('Não é possível dividir por zero.')

except NameError:
    print('B não está definido.')

except (TypeError, IndexError) as error: # podem ser adicionados mais de um tipo de erro por exceção
    print('Erro de tipagem / index.')
    print('MSG:', error) # colocando "as" para receber o erro ocorrido, pode-se demonstra-lo em execução
    print('Nome:', error.__class__.__name__) # demosntra o nome do erro

except Exception: # exceção majoritária, capta qualquer erro
    print('Erro desconhecido.')

else: #executa apenas caso o código try não possua erros
    print('Não teve erro')
    
finally: # garante a execução do código independente de tudo que ocorrer antes
    print('Fecha Arquivo')
    
print('FIM!')

print()

# raise - lança erros definidos

def non_zero(d):
    if d == 0:
        raise ZeroDivisionError('Você está tentyando dividir por zero.')
    return True

def deve_ser_int_ou_float(n):
    tipo_n = type(n)
    if not isinstance(n, (float, int)):
        raise TypeError(
            f'"{n}" deve ser int ou float.'
            f'"{tipo_n.__name__}" enviado.'
		)
    return True

def divide(n,d):
    deve_ser_int_ou_float(n)
    deve_ser_int_ou_float(d)
    non_zero(d)
    return n / d

print(divide(8, 0))
print()

