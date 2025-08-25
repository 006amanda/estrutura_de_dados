class No:
    def __init__(self, item):
        self.item = item
        self.proximo = None

def inserirItem(lista, item):
    novo = No(item)
    if lista is None:
        lista = novo
    else:
        novo.proximo = lista
        lista = novo
    return lista

def listarItens(lista):
    elemento = lista
    while elemento is not None:
        print("-> ", elemento.item)
        elemento = elemento.proximo

def maiores(lst, n):
    contador = 0
    elemento = lst
    while elemento is not None:
        if elemento.item > n:
            contador += 1
        elemento = elemento.proximo
    return contador

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

    n = int(input("Digite um valor: "))
    print("Quantidade de itens maiores que ", n, " = ", maiores(lista, n))

main()
