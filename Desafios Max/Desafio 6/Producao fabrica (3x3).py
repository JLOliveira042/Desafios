import numpy as np

A = np.array([
    [4, 2, 3],
    [3, 3, 2],
    [5, 1, 4]
])
B = np.array([150, 140, 160])

try:
    det = np.linalg.det(A)

    print(f"Determinante: {det:.2f}")

    if abs(det) < 1e-10:
        print("Erro: matriz não invertível.")

    else:
        X = np.linalg.solve(A, B)

        x = X[0]
        y = X[1]
        z = X[2]

        print("\nTaxas de produção:")
        print(f"x = {x:.2f}")
        print(f"y = {y:.2f}")
        print(f"z = {z:.2f}")

        producao = 6*x + 3*y + 5*z

        print(f"\nProdução com 6 trabalhadores, 3 máquinas e 5 horas: {producao:.2f}")

        print("\nVerificação:")
        print(f"4x + 2y + 3z = {4*x + 2*y + 3*z:.2f}")
        print(f"3x + 3y + 2z = {3*x + 3*y + 2*z:.2f}")
        print(f"5x + y + 4z = {5*x + y + 4*z:.2f}")

except np.linalg.LinAlgError:
    print("Erro ao resolver o sistema.")
