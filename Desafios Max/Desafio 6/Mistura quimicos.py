import numpy as np

A = np.array([
    [60, 40],
    [50, 30]
])

B = np.array([26, 20])

det = np.linalg.det(A)

if abs(det) < 1e-10:
    print("Erro: matriz não invertível.")

else:
    X = np.linalg.solve(A, B)

    x = X[0]
    y = X[1]

    print("Quantidades do ingrediente X:")
    print(f"x = {x:.2f}")
    print(f"y = {y:.2f}")

    unidades = 70*x + 50*y

    print(f"\nUnidades em 70 litros de A e 50 litros de B: {unidades:.2f}")

    print("\nVerificação:")
    print(f"60x + 40y = {60*x + 40*y:.2f}")
    print(f"50x + 30y = {50*x + 30*y:.2f}")
