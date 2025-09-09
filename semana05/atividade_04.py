class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

class ListaEncadeada:
    def __init__(self):
        self.inicio = None

    def inserirInicio(self, dado):
        novo = No(dado)
        novo.proximo = self.inicio
        self.inicio = novo

    def percorrer(self):
        if self.inicio is None:
            print("Lista vazia")
            return

        atual = self.inicio
        while atual is not None:
            if atual.proximo is not None:
                print(atual.dado, "-> ", atual.proximo.dado)
            else:
                print(atual.dado, "-> None")
            atual = atual.proximo

def menu():
    print("MENU")
    print("1 - Inserir no início")
    print("2 - Percorrer a lista")
    print("3 - Sair")
    opc = int(input("Opção: "))
    return opc

def main():
    lista = ListaEncadeada()
    opc = 0

    while opc != 3:
        opc = menu()
        if opc == 1:
            dado = int(input("Digite um valor: "))
            lista.inserirInicio(dado)
        elif opc == 2:
            print("Lista atualizada: ")
            lista.percorrer()
        elif opc == 3:
            print("Saindo do sistema...")

main()
