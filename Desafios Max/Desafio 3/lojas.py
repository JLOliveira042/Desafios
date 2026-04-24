produtos = []
vendas = []

def cadastrar_produto():
    nome = input("Nome do produto: ").strip()

    if nome == "":
        print("Nome não pode ser vazio.")
        return

    for p in produtos:
        if p["nome"].lower() == nome.lower():
            print("Produto já cadastrado.")
            return

    try:
        preco = float(input("Preço: "))
        if preco <= 0:
            print("Preço deve ser maior que zero.")
            return

        estoque = int(input("Estoque inicial: "))
        if estoque < 0:
            print("Estoque não pode ser negativo.")
            return

    except:
        print("Entrada inválida.")
        return

    produtos.append({
        "nome": nome,
        "preco": preco,
        "estoque": estoque
    })

    print("Produto cadastrado com sucesso.")

def listar_produtos():
    if len(produtos) == 0:
        print("Nenhum produto cadastrado.")
        return False

    print("\nLista de produtos:")
    for i, p in enumerate(produtos):
        print(f"{i} - {p['nome']} - R$ {p['preco']:.2f} - Estoque: {p['estoque']}")
    
    return True

def calcular_venda(produto, quantidade):
    valor_bruto = produto["preco"] * quantidade

    desconto = 0
    if quantidade > 10:
        desconto = valor_bruto * 0.05

    valor_final = valor_bruto - desconto

    produto["estoque"] -= quantidade

    return valor_bruto, desconto, valor_final

def realizar_venda():
    if not listar_produtos():
        return

    cliente = input("Nome do cliente: ").strip()
    if cliente == "":
        print("Nome inválido.")
        return

    try:
        indice = int(input("Selecione o produto pelo índice: "))
        produto = produtos[indice]
    except:
        print("Produto inválido.")
        return

    try:
        quantidade = int(input("Quantidade: "))
        if quantidade <= 0:
            print("Quantidade inválida.")
            return

        if quantidade > produto["estoque"]:
            print("Estoque insuficiente.")
            return

    except:
        print("Entrada inválida.")
        return

    valor_bruto, desconto, valor_final = calcular_venda(produto, quantidade)

    venda = {
        "cliente": cliente,
        "produto": produto["nome"],
        "quantidade": quantidade,
        "valor_bruto": valor_bruto,
        "desconto": desconto,
        "valor_final": valor_final
    }

    vendas.append(venda)

    print("Venda realizada com sucesso.")

def gerar_relatorio():
    if len(vendas) == 0:
        print("Nenhuma venda realizada.")
        return

    print("\n=== Relatório de Vendas ===")

    total = 0

    for v in vendas:
        print(f"\nCliente: {v['cliente']}")
        print(f"Produto: {v['produto']}")
        print(f"Quantidade: {v['quantidade']}")
        print(f"Valor Bruto: R$ {v['valor_bruto']:.2f}")
        print(f"Desconto: R$ {v['desconto']:.2f}")
        print(f"Valor Final: R$ {v['valor_final']:.2f}")

        total += v["valor_final"]

    print(f"\nTotal arrecadado pela loja: R$ {total:.2f}")

def salvar_relatorio():
    try:
        with open("relatorio_vendas.txt", "w", encoding="utf-8") as arquivo:
            arquivo.write("=== Relatório de Vendas ===\n")

            total = 0

            for v in vendas:
                arquivo.write(f"\nCliente: {v['cliente']}\n")
                arquivo.write(f"Produto: {v['produto']}\n")
                arquivo.write(f"Quantidade: {v['quantidade']}\n")
                arquivo.write(f"Valor Bruto: R$ {v['valor_bruto']:.2f}\n")
                arquivo.write(f"Desconto: R$ {v['desconto']:.2f}\n")
                arquivo.write(f"Valor Final: R$ {v['valor_final']:.2f}\n")

                total += v["valor_final"]

            arquivo.write(f"\nTotal arrecadado: R$ {total:.2f}\n")

        print("Relatório salvo com sucesso.")

    except:
        print("Erro ao salvar o arquivo.")

def main():
    while True:
        print("\n===== MENU =====")
        print("1 - Cadastrar produto")
        print("2 - Realizar venda")
        print("3 - Gerar relatório")
        print("4 - Salvar relatório")
        print("5 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            cadastrar_produto()
        elif opcao == "2":
            realizar_venda()
        elif opcao == "3":
            gerar_relatorio()
        elif opcao == "4":
            salvar_relatorio()
        elif opcao == "5":
            print("Encerrando...")
            break
        else:
            print("Opção inválida.")

main()