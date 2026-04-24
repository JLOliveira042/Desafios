def exibir_menu():
    print("\n--- SISTEMA DE LOJA SIMPLES ---")
    print("1. Cadastrar Produto")
    print("2. Realizar Venda")
    print("3. Relatório de Vendas")
    print("4. Sair")
    return input("Escolha uma opção: ")

def sistema_loja():
    produtos = []  # Lista de dicionários para produtos
    vendas = []    # Lista de dicionários para histórico de vendas

    while True:
        opcao = exibir_menu()

        if opcao == '1':
            nome = input("Nome do produto: ").strip()
            preco = float(input("Preço: R$ "))
            estoque = int(input("Quantidade em estoque: "))
            produtos.append({"nome": nome, "preco": preco, "estoque": estoque})
            print(f"Produto '{nome}' cadastrado com sucesso!")

        elif opcao == '2':
            if not produtos:
                print("Nenhum produto cadastrado.")
                continue
            
            print("\nProdutos Disponíveis:")
            for i, p in enumerate(produtos):
                print(f"{i+1}. {p['nome']} - R$ {p['preco']:.2f} (Estoque: {p['estoque']})")
            
            idx = int(input("Selecione o número do produto: ")) - 1
            qtd = int(input("Quantidade desejada: "))
            
            if qtd <= produtos[idx]['estoque']:
                cliente = input("Nome do cliente: ")
                valor_total = qtd * produtos[idx]['preco']
                
                # Regra de Desconto (5% se > 10 unidades)
                if qtd > 10:
                    valor_total *= 0.95
                    print("Desconto de 5% aplicado!")
                
                # Atualiza estoque
                produtos[idx]['estoque'] -= qtd
                
                # Registra venda
                venda = {
                    "cliente": cliente,
                    "produto": produtos[idx]['nome'],
                    "quantidade": qtd,
                    "total": valor_total
                }
                vendas.append(venda)
                print(f"Venda realizada! Total: R$ {valor_total:.2f}")
            else:
                print("Erro: Estoque insuficiente.")

        elif opcao == '3':
            print("\n--- RELATÓRIO DE VENDAS ---")
            total_loja = 0
            for v in vendas:
                print(f"Cliente: {v['cliente']} | {v['produto']} (x{v['quantidade']}) - R$ {v['total']:.2f}")
                total_loja += v['total']
            print(f"TOTAL ARRECADADO: R$ {total_loja:.2f}")

        elif opcao == '4':
            print("Encerrando sistema...")
            break
        else:
            print("Opção inválida!")

if __name__ == "__main__":
    sistema_loja()