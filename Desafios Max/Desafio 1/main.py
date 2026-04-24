def calcular_salario_estagiario(salario):
    return salario, 0, 0, salario

def calcular_salario_clt(salario):
    inss = salario * 0.08
    irrf = salario * 0.10 if salario > 2000 else 0
    liquido = salario - inss - irrf
    return salario, inss, irrf, liquido

def calcular_salario_freelancer(horas, valor_hora):
    bruto = horas * valor_hora
    desconto = bruto * 0.05
    liquido = bruto - desconto
    return bruto, desconto, 0, liquido

def cadastrar_funcionario():
    while True:
        nome = input("Nome: ").strip()
        if nome:
            break
        print("Nome inválido.")

    while True:
        tipo = input("Tipo (estagiario, clt, freelancer): ")
        if tipo in ["estagiario", "clt", "freelancer"]:
            break
        print("Tipo inválido.")

    try:
        if tipo in ["estagiario", "clt"]:
            salario = float(input("Salário: "))
            if salario <= 0:
                raise ValueError
            return {"nome": nome, "tipo": tipo, "salario": salario}
        else:
            horas = float(input("Horas trabalhadas: "))
            valor_hora = float(input("Valor por hora: "))
            if horas <= 0 or valor_hora <= 0:
                raise ValueError
            return {"nome": nome, "tipo": tipo, "horas": horas, "valor_hora": valor_hora}
    except:
        print("Erro na entrada.")
        return None

def processar_salario(funcionario):
    tipo = funcionario["tipo"]

    if tipo == "estagiario":
        bruto, inss, irrf, liquido = calcular_salario_estagiario(funcionario["salario"])
    elif tipo == "clt":
        bruto, inss, irrf, liquido = calcular_salario_clt(funcionario["salario"])
    else:
        bruto, inss, irrf, liquido = calcular_salario_freelancer(
            funcionario["horas"], funcionario["valor_hora"]
        )

    return {
        "nome": funcionario["nome"],
        "tipo": tipo,
        "bruto": bruto,
        "inss": inss,
        "irrf": irrf,
        "liquido": liquido
    }

def gerar_relatorio(lista):
    total = 0
    print("\n=== Relatório de Folha de Pagamento ===\n")

    for f in lista:
        print(f"Nome: {f['nome']}")
        print(f"Tipo: {f['tipo'].capitalize()}")
        print(f"Salário Bruto: R$ {f['bruto']:.2f}")
        print(f"Desconto INSS: R$ {f['inss']:.2f}")
        print(f"Desconto IRRF: R$ {f['irrf']:.2f}")
        print(f"Salário Líquido: R$ {f['liquido']:.2f}")
        print("-" * 30)
        total += f["liquido"]

    print(f"Total pago pela empresa: R$ {total:.2f}")

def salvar_relatorio(lista):
    try:
        with open("relatorio_folha.txt", "w") as f:
            total = 0
            f.write("=== Relatório de Folha de Pagamento ===\n\n")

            for func in lista:
                f.write(f"Nome: {func['nome']}\n")
                f.write(f"Tipo: {func['tipo'].capitalize()}\n")
                f.write(f"Salário Bruto: R$ {func['bruto']:.2f}\n")
                f.write(f"Desconto INSS: R$ {func['inss']:.2f}\n")
                f.write(f"Desconto IRRF: R$ {func['irrf']:.2f}\n")
                f.write(f"Salário Líquido: R$ {func['liquido']:.2f}\n")
                f.write("-" * 30 + "\n")
                total += func["liquido"]

            f.write(f"Total pago pela empresa: R$ {total:.2f}")
        print("Relatório salvo com sucesso.")
    except:
        print("Erro ao salvar o arquivo.")

def main():
    funcionarios = []

    while True:
        print("\n1 - Cadastrar funcionário")
        print("2 - Gerar relatório")
        print("3 - Salvar relatório")
        print("4 - Sair")

        opcao = input("Escolha: ")

        if opcao == "1":
            f = cadastrar_funcionario()
            if f:
                funcionarios.append(processar_salario(f))
        elif opcao == "2":
            gerar_relatorio(funcionarios)
        elif opcao == "3":
            salvar_relatorio(funcionarios)
        elif opcao == "4":
            break
        else:
            print("Opção inválida.")

main()
