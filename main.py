from farmacia import Farmacia

def main():
    farmacia = Farmacia()

    while True:
        print("\nSistema de Controle de Farmácia")
        print("1. Cadastrar Medicamento")
        print("2. Vender Medicamento")
        print("3. Consultar Estoque")
        print("4. Gerar Relatório de Vendas")
        print("5. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            id = input("ID do Medicamento: ")
            nome = input("Nome do Medicamento: ")
            quantidade = int(input("Quantidade: "))
            preco = float(input("Preço: "))
            farmacia.cadastrar_medicamento(id, nome, quantidade, preco)
        elif opcao == "2":
            id = input("ID do Medicamento: ")
            quantidade = int(input("Quantidade: "))
            farmacia.vender_medicamento(id, quantidade)
        elif opcao == "3":
            farmacia.consultar_estoque()
        elif opcao == "4":
            farmacia.gerar_relatorio_vendas()
        elif opcao == "5":
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
