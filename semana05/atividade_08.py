class No:
    class NoDuplo:
        def __init__(self, dado):
            self.dado = dado
            self.anterior = None
            self.proximo = None

class ListaDuplamenteEncadeada:
    def __init__(self):
        self.inicio = None

    def adicionar_inicio(self, dado):
        novo = No.NoDuplo(dado)
        if self.inicio is None:
            self.inicio = novo
        else:
            novo.proximo = self.inicio
            self.inicio.anterior = novo
            self.inicio = novo

    def percorrer_frente(self):
        atual = self.inicio
        while atual is not None:
            print(atual.dado)
            atual = atual.proximo

    def percorrer_tras(self):
        atual = self.inicio
        if atual is None:
            return
        while atual.proximo is not None:
            atual = atual.proximo
        while atual is not None:
            print(atual.dado)
            atual = atual.anterior

lista = ListaDuplamenteEncadeada()
lista.adicionar_inicio(12)
lista.adicionar_inicio(45)
lista.adicionar_inicio(5)
lista.adicionar_inicio(11)
lista.adicionar_inicio(9)
lista.adicionar_inicio(3)
lista.adicionar_inicio(21)
lista.adicionar_inicio(18)
lista.adicionar_inicio(19)

print("Percorrendo da frente para trás: ")
lista.percorrer_frente()

print()

print("Percorrendo de trás para frente: ")
lista.percorrer_tras()
