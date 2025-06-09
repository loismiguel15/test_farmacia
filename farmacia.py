from medicamento import Medicamento

class Farmacia:
    def __init__(self):
        self.medicamentos = []
        self.vendas = []

    def cadastrar_medicamento(self, id, nome, quantidade, preco):
        medicamento = Medicamento(id, nome, quantidade, preco)
        self.medicamentos.append(medicamento)
        print(f"Medicamento {nome} cadastrado com sucesso!")

    def vender_medicamento(self, id, quantidade):
        for medicamento in self.medicamentos:
            if medicamento.id == id:
                if medicamento.quantidade >= quantidade:
                    medicamento.quantidade -= quantidade
                    venda = {
                        'id': id,
                        'nome': medicamento.nome,
                        'quantidade': quantidade,
                        'preco': medicamento.preco,
                        'total': quantidade * medicamento.preco
                    }
                    self.vendas.append(venda)
                    print(f"Venda de {quantidade} unidades de {medicamento.nome} realizada com sucesso!")
                    return
                else:
                    print("Quantidade insuficiente em estoque.")
                    return
        print("Medicamento não encontrado.")

    def consultar_estoque(self):
        print("Estoque de Medicamentos:")
        for medicamento in self.medicamentos:
            print(medicamento)

    def gerar_relatorio_vendas(self):
        if not self.vendas:
            print("Nenhuma venda realizada.")
            return

        print("Relatório de Vendas:")
        for venda in self.vendas:
            print(f"ID: {venda['id']}, Nome: {venda['nome']}, Quantidade: {venda['quantidade']}, Preço: R${venda['preco']:.2f}, Total: R${venda['total']:.2f}")
