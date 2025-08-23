class No:
    def __init__(self, item: float):
        self.item = item
        self.proximo = None


def menu():
    print("1 - Inserir")
    print("2 - Listar")
    print("3 - Remover")
    opc = int(input("Digite uma opção: "))
    return opc

def inserirItem(lista, item):
    novoItem = No(item)
    if lista is None:
        lista = novoItem
    else:
        novoItem.proximo = lista
        lista = novoItem
    return lista

def listarItens(lista):
    if lista is None:
        print("Lista vazia")
    else:
        elemento = lista
        while elemento is not None:
            print("-> ", elemento.item)
            elemento = elemento.proximo

def excluirItem(lista, item):
    elemento = lista
    anterior = None

    while elemento is not None:
        if elemento.item == item:
            if anterior is None: 
                print("Primeiro elemento removido")
                return elemento.proximo
            else:
                anterior.proximo = elemento.proximo
                print("Elemento removido")
                return lista
        anterior = elemento
        elemento = elemento.proximo

    print("Item não encontrado")
    return lista  

def main():
    opc = 0
    lista = None

    while opc != 4:
        opc = menu()

        if opc == 1:
            item = float(input("Item para inserir: "))
            lista = inserirItem(lista, item)
        elif opc == 2:
            listarItens(lista)
        elif opc == 3:
            item = float(input("Item para remover: "))
            lista = excluirItem(lista, item)

main()
