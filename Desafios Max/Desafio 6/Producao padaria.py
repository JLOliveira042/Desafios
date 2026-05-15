import numpy as np

A = np.array([
    [50, 20],
    [30, 30]
])

B = np.array([30, 12])

det = np.linalg.det(A)

if abs(det) < 1e-10:
    print("Erro: matriz não invertível.")

else:
    X = np.linalg.solve(A, B)

    x = X[0]
    y = X[1]

    print("Quantidades por unidade:")
    print(f"x = {x:.2f} kg de farinha por pão")
    print(f"y = {y:.2f} kg de açúcar por bolo")

    consumo = 40*x + 25*y

    print(f"\nConsumo para 40 pães e 25 bolos: {consumo:.2f} kg")

    print("\nVerificação:")
    print(f"50x + 20y = {50*x + 20*y:.2f}")
    print(f"30x + 30y = {30*x + 30*y:.2f}")
