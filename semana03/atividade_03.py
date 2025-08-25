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

def ultimo(lista):
    if lista is None:
        return None 
    elemento = lista
    while elemento.proximo is not None:
        elemento = elemento.proximo
    return elemento

def main():
    lista = None
    lista = inserirItem(lista, 10)
    lista = inserirItem(lista, 5)
    lista = inserirItem(lista, 20)
    lista = inserirItem(lista, 15)
    lista = inserirItem(lista, 88)
    lista = inserirItem(lista, 95)
    lista = inserirItem(lista, 2)
    lista = inserirItem(lista, 19)
    lista = inserirItem(lista, 22)

    listarItens(lista)

    noFinal = ultimo(lista)
    if noFinal is not None:
        print("Último nó da lista: ", noFinal.valor)
    else:
        print("A lista está vazia")
main()
