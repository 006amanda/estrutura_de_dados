class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

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

def listarItens(lista):
    elemento = lista
    while elemento is not None:
        print("-> ", elemento.valor)
        elemento = elemento.proximo

def lista_calcula_media(lst):
    if lst is None:
        return 0
    soma = 0
    cont = 0
    elemento = lst
    while elemento is not None:
        soma += elemento.valor
        cont += 1
        elemento = elemento.proximo
    return soma / cont

def main():
    lista_amanda = None
    lista_amanda = lista_insere_final(lista_amanda, 10)
    lista_amanda = lista_insere_final(lista_amanda, 8)
    lista_amanda = lista_insere_final(lista_amanda, 7)

    print("Média da Amanda: ", lista_calcula_media(lista_amanda))

main()

