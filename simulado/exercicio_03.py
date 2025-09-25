class No:
    def __init__(self, nome, altitude, combustivel):
        self.nome = nome
        self.altitude = altitude
        self.combustivel = combustivel
        self.ativo = True
        self.proximo = None
        self.anterior = None

class Orbita:
    def __init__(self):
        self.inicio = None

    def adicionar_satelite(self, nome, altitude, combustivel):
        if altitude < 300:
            print("Altura mínima é 300 km")
            return
        if combustivel < 0:
            print("Combustível inválido")
            return
        novo = No(nome, altitude, combustivel)
        if self.inicio is None:
            novo.proximo = novo.anterior = novo
            self.inicio = novo
        else:
            ultimo = self.inicio.anterior
            ultimo.proximo = novo
            novo.anterior = ultimo
            novo.proximo = self.inicio
            self.inicio.anterior = novo

    def remover_satelite(self, nome):
        if self.inicio is None:
            return
        atual = self.inicio
        while True:
            if atual.nome == nome:
                if atual.proximo == atual:
                    self.inicio = None
                else:
                    atual.anterior.proximo = atual.proximo
                    atual.proximo.anterior = atual.anterior
                    if atual == self.inicio:
                        self.inicio = atual.proximo
                break
            atual = atual.proximo
            if atual == self.inicio:
                break

    def simular_orbita(self, consumo=10):
        if self.inicio is None:
            return
        atual = self.inicio
        while True:
            if atual.ativo:
                atual.combustivel -= consumo
                if atual.combustivel <= 0:
                    atual.combustivel = 0
                    atual.ativo = False
            atual = atual.proximo
            if atual == self.inicio:
                break

    def percorrer_horario(self):
        if self.inicio is None:
            print("Nenhum satélite em órbita")
            return
        atual = self.inicio
        while True:
            if atual.ativo:
                print(atual.nome)
                print(atual.altitude, "km")
                print("Combustível: ", atual.combustivel, "%")
                print("Status: Ativo")
            else:
                print(atual.nome)
                print(atual.altitude, "km")
                print("Combustível: ", atual.combustivel, "%")
                print("Status: Desativado")
            atual = atual.proximo
            if atual == self.inicio:
                break

    def percorrer_antihorario(self):
        if self.inicio is None:
            print("Nenhum satélite em órbita")
            return
        atual = self.inicio.anterior
        while True:
            if atual.ativo:
                print(atual.nome)
                print(atual.altitude, "km")
                print("Combustível: ", atual.combustivel, "%")
                print("Status: Ativo")
            else:
                print(atual.nome)
                print(atual.altitude, "km")
                print("Combustível: ", atual.combustivel, "%")
                print("Status: Desativado")
            atual = atual.anterior
            if atual.proximo == self.inicio.anterior:
                break

    def reposicionar(self, nome, nova_altitude):
        if nova_altitude < 300:
            print("Altitude inválida")
            return
        atual = self.inicio
        while True:
            if atual.nome == nome:
                atual.altitude = nova_altitude
                break
            atual = atual.proximo
            if atual == self.inicio:
                break

    def mostrar_ativos(self):
        if self.inicio is None:
            print("Nenhum satélite em órbita")
            return
        atual = self.inicio
        while True:
            if atual.ativo:
                print(atual.nome)
                print(atual.altitude, "km")
                print("Combustível: ", atual.combustivel, "%")
            atual = atual.proximo
            if atual == self.inicio:
                break

    def mostrar_desativados(self):
        if self.inicio is None:
            print("Nenhum satélite em órbita")
            return
        atual = self.inicio
        while True:
            if not atual.ativo:
                print(atual.nome)
                print(atual.altitude, "km")
                print("Combustível: ", atual.combustivel, "%")
            atual = atual.proximo
            if atual == self.inicio:
                break

def main():
    orbita = Orbita()
    orbita.adicionar_satelite("Hubble", 550, 100)
    orbita.adicionar_satelite("James Webb", 1500, 100)
    orbita.adicionar_satelite("Amazônia-1", 780, 50)

    print("Percorrendo órbita horário: ")
    orbita.percorrer_horario()

    orbita.simular_orbita(consumo=30)
    print("Após simulação de órbita: ")
    orbita.percorrer_horario()

    print("Satélites ativos: ")
    orbita.mostrar_ativos()

    print("Satélites desativados: ")
    orbita.mostrar_desativados()

    orbita.reposicionar("Amazônia-1", 900)
    orbita.percorrer_horario()

main()
