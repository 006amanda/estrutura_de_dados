class No:
    def __init__(self, valor):
        self.valor = valor
        self.proximo = None

def lista_insere_final(lst, valor):
    novo = No(valor)
    if not lst:
        return novo
    elemento = lst


    while elemento.proximo:
        elemento = elemento.proximo
    elemento.proximo = novo
    return lst

def listarItens(lst):
    e = lst
    while e:
        print("-> ", e.valor)
        e = e.proximo

def lista_altera(lst):
    e = lst
    while e:
        e.valor = -e.valor
        e = e.proximo
    return lst

outra_lista = None
for v in [10, -8, 5, -1, 22, 18, -18, -22, 15]:
    outra_lista = lista_insere_final(outra_lista, v)

outra_lista = lista_altera(outra_lista)
print("Alterada: ")
listarItens(outra_lista)
