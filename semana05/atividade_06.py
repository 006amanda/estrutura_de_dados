class No:
    def __init__(self, dado):
        self.dado = dado
        self.proximo = None

class ListaEncadeada:
    def __init__(self):
        self.inicio = None
        self.final = None

    def inserirInicio(self, dado):
        novo = No(dado)
        if self.inicio is None:
            self.inicio = novo
            self.final = novo
        else:
            novo.proximo = self.inicio
            self.inicio = novo

    def inserirFinal(self, dado):
        novo = No(dado)
        if self.inicio is None:
            self.inicio = novo
            self.final = novo
        else:
            self.final.proximo = novo
            self.final = novo

    def media(self):
        if self.inicio is None:
            return
        soma = 0
        contador = 0
        atual = self.inicio
        while atual is not None:
            soma += atual.dado
            contador += 1
            atual = atual.proximo
        soma = soma / contador
        print(soma)
        return soma

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
    print("2 - Inserir no final")
    print("3 - Percorrer a lista")
    print("4 - Média dos dados")
    print("5 - Sair")
    return int(input("Opção: "))

def main():
    lista = ListaEncadeada()
    opc = 0

    while opc != 5:
        opc = menu()
        if opc == 1:
            dado = int(input("Digite um valor: "))
            lista.inserirInicio(dado)
        elif opc == 2:
            dado = int(input("Digite um valor: "))
            lista.inserirFinal(dado)
        elif opc == 3:
            print("Lista atualizada: ")
            lista.percorrer()
        elif opc == 4:
            print("Média dos dados informados: ")
            lista.media()
        elif opc == 5:
            print("Saindo do sistema...")

main()
