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

    def altura(self, no):
        if no is None:
            return 0
        alt_esquerda = self.altura(no.esquerda)
        alt_direita = self.altura(no.direita)
        return 1 + max(alt_esquerda, alt_direita)
    
    def buscar(self, valor):
        atual = self.raiz
        while atual is not None:
            if valor == atual.dado:
                return True
            if valor < atual.dado:
                atual = atual.esquerda
            else:
                atual = atual.direita
        return False

    def contar_nos(self, no):
        if no is None:
            return 0
        return 1 + self.contar_nos(no.esquerda) + self.contar_nos(no.direita)

    def contar_folhas(self, no):
        if no is None:
            return 0
        if no.esquerda is None and no.direita is None:
            return 1
        return self.contar_folhas(no.esquerda) + self.contar_folhas(no.direita)
    
    def minimo(self, no):
        if no is None:
            return None
        while no.esquerda is not None:
            no = no.esquerda
        return no.dado
    
    def maximo(self, no):
        if no is None:
            return None
        while no.direita is not None:
            no = no.direita
        return no.dado

    def media(self, no):
        def soma(no):
            if no is None:
                return 0
            return no.dado + soma(no.esquerda) + soma(no.direita)

        total_nos = self.contar_nos(no)
        if total_nos == 0:
            return 0
        return soma(no) / total_nos

    def contar_maiores(self, no, limite):
        if no is None:
            return 0
        contador = 1 if no.dado > limite else 0
        return contador + self.contar_maiores(no.esquerda, limite) + self.contar_maiores(no.direita, limite)

def main():
    opc = 0 
    arv = Arvore()

    while opc != 13:
        print("1 - Inserir")
        print("2 - Mostrar pré-ordem")
        print("3 - Mostrar em ordem")
        print("4 - Mostrar pós-ordem")
        print("5 - Mostrar altura")
        print("6 - Contagem dos nós")
        print("7 - Contagem de folhas")
        print("8 - Buscar valor")
        print("9 - Mostrar menor valor")
        print("10 - Mostrar maior valor")
        print("11 - Mostrar média")
        print("12 - Contar valores maiores que...")
        print("13 - Sair")
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
            altura = arv.altura(arv.raiz)
            print("Altura da árvore: ", altura)
            print()
        elif opc == 6:
            total_nos = arv.contar_nos(arv.raiz)
            print("Total de nós: ", total_nos)
            print()
        elif opc == 7:
            total_folhas = arv.contar_folhas(arv.raiz)
            print("Total de folhas: ", total_folhas)
            print()
        elif opc == 8:
            valor = int(input("Buscar: "))
            encontrado = arv.buscar(valor)
            print(encontrado)
            print()
            print()
        elif opc == 9:
            print("Menor valor: ", arv.minimo(arv.raiz))
            print()
        elif opc == 10:
            print("Maior valor: ", arv.maximo(arv.raiz))
            print()
        elif opc == 11:
            print("Média dos valores: ", arv.media(arv.raiz))
            print()
        elif opc == 12:
            limite = int(input("Informe o valor limite: "))
            maiores = arv.contar_maiores(arv.raiz, limite)
            print("Quantidade de nós com valor maior: ", maiores)
            print()
        elif opc == 13:
            print("Encerrando o programa...")
main()
