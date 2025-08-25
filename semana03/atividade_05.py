class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

def listarItens(lista):
    elemento = lista
    while elemento is not None:
        print("-> ", elemento.valor)
        elemento = elemento.proximo

def lista_insere_final(lst, valor):
    novo = No(valor)
    if lst is None: 
        return novo
    else:
        elemento = lst
        while elemento.proximo is not None:
            elemento = elemento.proximo
        elemento.proximo = novo
        return lst

def main():
    lista = None
    lista = lista_insere_final(lista, 5)
    lista = lista_insere_final(lista, 23)
    lista = lista_insere_final(lista, 15)
    lista = lista_insere_final(lista, 75)
    lista = lista_insere_final(lista, 9)
    lista = lista_insere_final(lista, 19)
    lista = lista_insere_final(lista, 22)

    print("Lista: ")
    listarItens(lista)

main()
