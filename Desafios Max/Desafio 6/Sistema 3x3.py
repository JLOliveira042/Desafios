import numpy as np

A = []
B = []

print("Digite os coeficientes da matriz A (3x3):")

for i in range(3):
    linha = []

    for j in range(3):
        valor = float(input(f"A[{i}][{j}]: "))
        linha.append(valor)

    A.append(linha)

print("\nDigite os termos independentes:")

for i in range(3):
    valor = float(input(f"B[{i}]: "))
    B.append(valor)

A = np.array(A)
B = np.array(B)

print("\nMatriz A:")
print(A)

print("\nVetor B:")
print(B)

try:
    det = np.linalg.det(A)

    print(f"\nDeterminante: {det:.2f}")

    if abs(det) < 1e-10:
        print("Erro: matriz não invertível.")

    else:
        X = np.linalg.solve(A, B)

        print("\nSolução:")
        print(f"x = {X[0]:.2f}")
        print(f"y = {X[1]:.2f}")
        print(f"z = {X[2]:.2f}")

except np.linalg.LinAlgError:
    print("Erro ao resolver o sistema.")
