frutas = ["maçã", "banana", "laranja"]
numeros = [1, 2, 3, 4, 5]
misturado = [1, "texto", 3.14, True]

print("Lista de frutas:", frutas)
print("Lista de números:", numeros)
print("Lista misturada:", misturado)

print("\nAcessando elementos:")
print("Primeira fruta:", frutas[0])
print("Última fruta:", frutas[-1])
print("Sublista de números:", numeros[1:4])

print("\nIterando com for:")
for fruta in frutas:
    print("Fruta:", fruta)

print("\nIterando com while:")
indice = 0
while indice < len(frutas):
    print(f"Fruta no índice {indice}: {frutas[indice]}")
    indice += 1

print("\nOperações com listas:")

frutas.append("morango")
print("Após append:", frutas)

frutas.remove("banana")
print("Após remove:", frutas)

frutas[1] = "kiwi"
print("Após modificação:", frutas)

nova_lista = frutas + ["uva", "manga"]
print("Após concatenação:", nova_lista)

print("\nExemplo de pilha:")
pilha = []

pilha.append(1)
pilha.append(2)
pilha.append(3)
print("Pilha:", pilha)

ultimo = pilha.pop()
print("Elemento removido:", ultimo)
print("Pilha após pop:", pilha)

print("\nOutras operações:")
numeros = [5, 2, 8, 1, 9]

print("Tamanho:", len(numeros))
print("Tem 8?", 8 in numeros)

numeros.sort()
print("Ordenado:", numeros)

numeros.reverse()
print("Invertido:", numeros)

print("\nLista aninhada:")
matriz = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

print("Matriz:", matriz)
print("Elemento [1][2]:", matriz[1][2])

print("\nList comprehension:")
quadrados = [x**2 for x in range(1, 6)]
print("Quadrados:", quadrados)