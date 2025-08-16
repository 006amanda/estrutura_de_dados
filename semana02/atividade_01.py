class Produto:

    def __init__(self, produto, estoque, preco):
        self.produto = produto
        self.estoque = estoque
        self.preco = preco

    def calcular_total(self):
        return (self.estoque) * (self.preco)

batata = Produto("Batata", 5, 5.99)
maca = Produto("Maçã", 3, 3.95)

print("Nome do Produto: ", batata.produto, "---> Total do produto: ", batata.calcular_total())
print("Nome do Produto: ", maca.produto, "---> Total do produto: ", maca.calcular_total())
