class Node:
    def __init__ (self, dado):
        self.dado = dado
        self.esquerda = None
        self.direita = None

class Arvore:
    def __init__(self):
        self.raiz = None

    def inserir(self, dado):
        novo = Node(dado)

        if self.raiz is None:
            self.raiz = novo
            return
            
        atual = self.raiz
        while True:
            if atual.dado > dado:
                if atual.esquerda is None:
                    atual.esquerda = novo
                    return
                atual = atual.esquerda
            else:
                if atual.direita is None:
                    atual.direita = novo
                    return
                atual = atual.direita

    def pre_ordem(self, no):
        if no is not None:
            print(no.dado)
            self.pre_ordem(no.esquerda)
            self.pre_ordem(no.direita)

    def em_ordem(self, no):
        if no is not None:
            self.em_ordem(no.esquerda)
            print(no.dado)
            self.em_ordem(no.direita)

    def pos_ordem(self, no):
        if no is not None:
            self.pos_ordem(no.esquerda)
            self.pos_ordem(no.direita)
            print(no.dado)

def main():
    opc = 0 
    arv = Arvore()

    while opc != 5:
        print("1 - Inserir")
        print("2 - Mostrar pré-ordem")
        print("3 - Mostrar em ordem")
        print("4 - Mostrar pós-ordem")
        print("5 - Sair")
        opc = int(input("Escolha a opção: "))

        if opc == 1:
            dado = int(input("Valor para inserir: "))
            arv.inserir(dado)
            print()
        elif opc == 2:
            arv.pre_ordem(arv.raiz)
            print()
        elif opc == 3:
            arv.em_ordem(arv.raiz)
            print()
        elif opc == 4:
            arv.pos_ordem(arv.raiz)
            print()
        elif opc == 5:
            print("Encerrando o programa...")
main()
