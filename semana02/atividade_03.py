class Produto:
    def __init__(self, nome, preco, estoque):
        self.nome = nome
        self.preco = preco
        self.estoque = estoque

    def atualizar_estoque(self, qtd):
        self.estoque += qtd
        return self.estoque

arroz = Produto("Arroz", 14.99, 16)
batata = Produto("Batata", 5.99, 60)

print("Nome do Produto: ", arroz.nome,
      "Preço: R$", arroz.preco,
      "Estoque anterior: ", 16,
      "Estoque atual: ", arroz.atualizar_estoque(10))
print("Nome do Produto: ", batata.nome,
      "Preço: R$", batata.preco,
      "Estoque anterior: ", 60,
      "Estoque atual: ", batata.atualizar_estoque(20))
