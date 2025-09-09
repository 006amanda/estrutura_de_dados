class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    def apresentar(self):
        print("Olá, me chamo " + self.nome + " e tenho " + str(self.idade) + " anos")

ana = Pessoa("Ana", 19)
joao = Pessoa("João", 21)

def main():
    ana.apresentar()
    joao.apresentar()

main()
