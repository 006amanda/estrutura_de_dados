class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

def inserirItem(lista, valor):
    novo = No(valor)
    if lista is None:
        lista = novo
    else:
        novo.proximo = lista
        lista = novo
    return lista

def listarItens(lista):
    elemento = lista
    while elemento is not None:
        print("-> ", elemento.valor)
        elemento = elemento.proximo

def concatena(l1, l2):
    if l1 is None: 
        return l2
    elemento = l1
    while elemento.proximo is not None:
        elemento = elemento.proximo
    elemento.proximo = l2
    return l1

def main():
    l1 = None
    l2 = None

    l1 = inserirItem(l1, 30)
    l1 = inserirItem(l1, 20)
    l1 = inserirItem(l1, 10)

    l2 = inserirItem(l2, 50)
    l2 = inserirItem(l2, 40)

    print("Lista 1: ")
    listarItens(l1)
    print("Lista 2: ")
    listarItens(l2)

    print("Lista concatenada: ")
    l3 = concatena(l1, l2)
    listarItens(l3)

main()
