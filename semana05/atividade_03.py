class Carro:
    def __init__(self, marca, modelo, ano):
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.ligado = False

    def ligar(self):
        self.ligado = True

    def desligar(self):
        self.ligado = False

    def estado(self):
        if self.ligado:
            print("O carro está ligado.")
        else:
            print("O carro está desligado.")


dodge = Carro("Dodge", "Challenger SRT Demon 170", 2023)

def main():
    print("Parabéns!")
    print("Você acaba de adquirir um " + (dodge.marca) + " " + (dodge.modelo))
    print("Ano: ", (dodge.ano))
    print()
    print("Preparando o seu carro...")
    dodge.ligar()
    dodge.estado()
    dodge.desligar()
    dodge.estado()
    print()
    print("Testes concluídos com sucesso!")
    print("O carro está pronto para ir para casa.")

main()
