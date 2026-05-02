import random

matriz = []

for i in range(3):
    linha = []
    for j in range(3):
        linha.append(random.randint(0, 10))
    matriz.append(linha)

print("Matriz 3x3 aleatória:")
for linha in matriz:
    print(linha)

A = [[10, 20, 30],
     [15, 25, 35]]

B = [[5, 10, 15],
     [10, 5, 10]]

soma = []

for i in range(len(A)):
    linha = []
    for j in range(len(A[0])):
        linha.append(A[i][j] + B[i][j])
    soma.append(linha)

print("\nSoma das matrizes (vendas):")
for linha in soma:
    print(linha)

total_vendas = sum(sum(linha) for linha in soma)
print("Total de vendas:", total_vendas)

import numpy as np

alunos = np.array([
    [8.5, 7.0, 9.0],
    [6.0, 5.5, 7.0],
    [9.0, 8.5, 10.0]
])

medias = alunos.mean(axis=1)

print("\nMédias dos alunos:")
print(medias)

matriz_det = np.array([
    [2, 1, 3],
    [1, 0, 2],
    [4, 1, 8]
])

det = np.linalg.det(matriz_det)

print("\nDeterminante:", det)

if det != 0:
    print("Sistema resolvível (matriz invertível)")
else:
    print("Sistema NÃO resolvível (matriz singular)")

estoque = np.array([
    [10, 20],
    [30, 40],
    [50, 60]
])

precos = np.array([
    [2, 3, 4]
])

estoque_T = estoque.T

total = np.dot(precos, estoque_T)

print("\nEstoque transposto:")
print(estoque_T)

print("\nTotal calculado:")
print(total)
