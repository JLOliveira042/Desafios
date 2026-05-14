import numpy as np

A = np.array([
    [5, 3],
    [8, 2]
])

B = np.array([110, 100])

X = np.linalg.solve(A, B)

x = X[0]
y = X[1]

print("Taxas de produção:")
print(f"x = {x:.2f} itens por trabalhador")
print(f"y = {y:.2f} itens por máquina")

producao = 10*x + 4*y

print(f"\nProdução com 10 trabalhadores e 4 máquinas: {producao:.2f}")

print("\nVerificação:")
print(f"5x + 3y = {5*x + 3*y:.2f}")
print(f"8x + 2y = {8*x + 2*y:.2f}")
