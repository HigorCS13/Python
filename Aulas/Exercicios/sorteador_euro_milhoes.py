import random

# Listas com as sequências numéricas
primeira_sequencia = list(range(1, 61))
segunda_sequencia = list(range(1, 13))

# Dicionários para armazenar a contagem dos números sorteados
primeira_contagem = {num: 0 for num in primeira_sequencia}
segunda_contagem = {num: 0 for num in segunda_sequencia}

# Número de sorteios a ser realizado
num_sorteios = 1246

# Loop para realizar os sorteios
for i in range(num_sorteios):
    # Sorteio dos números da primeira sequência
    sorteio_primeira = random.sample(primeira_sequencia, 5)
    # Atualização da contagem dos números sorteados na primeira sequência
    for num in sorteio_primeira:
        primeira_contagem[num] += 1
    
    # Sorteio dos números da segunda sequência
    sorteio_segunda = random.sample(segunda_sequencia, 2)
    # Atualização da contagem dos números sorteados na segunda sequência
    for num in sorteio_segunda:
        segunda_contagem[num] += 1

# Lista com os 5 números mais sorteados na primeira sequência
primeira_mais_sorteados = sorted(primeira_contagem, key=primeira_contagem.get, reverse=True)[:5]

# Lista com os 2 números mais sorteados na segunda sequência
segunda_mais_sorteados = sorted(segunda_contagem, key=segunda_contagem.get, reverse=True)[:2]

# Exibição dos resultados
print(f"5 números mais sorteados na primeira sequência: {primeira_mais_sorteados}")
print(f"2 números mais sorteados na segunda sequência: {segunda_mais_sorteados}")
