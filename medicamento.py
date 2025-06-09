class Medicamento:
    def __init__(self, id, nome, quantidade, preco):
        self.id = id
        self.nome = nome
        self.quantidade = quantidade
        self.preco = preco

    def __str__(self):
        return f"ID: {self.id}, Nome: {self.nome}, Quantidade: {self.quantidade}, Preço: R${self.preco:.2f}"