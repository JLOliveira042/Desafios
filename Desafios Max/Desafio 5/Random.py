import random

print("=== MATRIZ COM RANDOM ===")

num_linhas = 3
num_colunas = 3

matriz_random = []

for i in range(num_linhas):
    linha = []
    for j in range(num_colunas):
        numero = random.randint(0, 9)
        linha.append(numero)
    matriz_random.append(linha)

for linha in matriz_random:
    print(linha)

import numpy as np

print("\n=== MATRIZ COM NUMPY ===")

matriz_numpy = np.random.randint(0, 10, size=(3, 3))

print(matriz_numpy)
