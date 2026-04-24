tarefas = []

def mostrar_tarefas():
    print("\nLista de tarefas:")
    if len(tarefas) == 0:
        print("Nenhuma tarefa cadastrada.")
    else:
        for i, tarefa in enumerate(tarefas):
            print(f"{i} - {tarefa}")

def adicionar_tarefa():
    tarefa = input("Digite uma nova tarefa: ")
    tarefas.append(tarefa)
    print("Tarefa adicionada.")

def remover_tarefa():
    mostrar_tarefas()
    try:
        indice = int(input("Digite o índice da tarefa para remover: "))
        removida = tarefas.pop(indice)
        print(f"Tarefa removida: {removida}")
    except:
        print("Índice inválido.")

def modificar_tarefa():
    mostrar_tarefas()
    try:
        indice = int(input("Digite o índice da tarefa para modificar: "))
        nova = input("Digite a nova tarefa: ")
        tarefas[indice] = nova
        print("Tarefa atualizada.")
    except:
        print("Índice inválido.")

def buscar_tarefa():
    termo = input("Digite o nome da tarefa: ")
    if termo in tarefas:
        print("Tarefa encontrada.")
    else:
        print("Tarefa não encontrada.")

def ordenar_tarefas():
    tarefas.sort()
    print("Lista ordenada.")

def inverter_tarefas():
    tarefas.reverse()
    print("Lista invertida.")

def usar_como_pilha():
    print("\nUsando como pilha")
    tarefas.append("Tarefa Pilha 1")
    tarefas.append("Tarefa Pilha 2")
    print("Pilha atual:", tarefas)
    
    removido = tarefas.pop()
    print("Elemento removido:", removido)

while True:
    print("\n===== MENU =====")
    print("1 - Adicionar tarefa")
    print("2 - Remover tarefa")
    print("3 - Modificar tarefa")
    print("4 - Mostrar tarefas")
    print("5 - Buscar tarefa")
    print("6 - Ordenar lista")
    print("7 - Inverter lista")
    print("8 - Usar como pilha")
    print("0 - Sair")

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_tarefa()
    elif opcao == "2":
        remover_tarefa()
    elif opcao == "3":
        modificar_tarefa()
    elif opcao == "4":
        mostrar_tarefas()
    elif opcao == "5":
        buscar_tarefa()
    elif opcao == "6":
        ordenar_tarefas()
    elif opcao == "7":
        inverter_tarefas()
    elif opcao == "8":
        usar_como_pilha()
    elif opcao == "0":
        print("Encerrando programa...")
        break
    else:
        print("Opção inválida.")