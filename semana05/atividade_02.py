class Retangulo:
    def __init__(self, largura, altura):
        self.largura = largura
        self.altura = altura

    def calcular_area(self):
            return self.largura * self.altura

    def calcular_perimetro(self):
            return 2 * (self.largura + self.altura)

retangulo = Retangulo(12, 6)

def main():
    print("Temos um retângulo com base 12 e altura 6")
    print("---")
    print("Sua área é igual a " + str(retangulo.calcular_area()))
    print("---")
    print("E seu perímetro é igual a " + str(retangulo.calcular_perimetro()))

main()
