class No:
    def __init__(self, idd, bastao=False):
        self.idd = idd
        self.bastao = bastao
        self.proximo = None
        self.anterior = None

def adicionar(lista, idd, bastao=False):
    novoAtleta = No(idd, bastao)
    if lista is None:
        novoAtleta.proximo = novoAtleta
        novoAtleta.anterior = novoAtleta
        return novoAtleta
    else:
        ultimo = lista.anterior
        novoAtleta.proximo = lista
        novoAtleta.anterior = ultimo
        ultimo.proximo = novoAtleta
        lista.anterior = novoAtleta
        return lista

def remover(lista, idd):
    if lista is None:
        print("Lista vazia.")
        return None
    aux = lista
    while True:
        if aux.idd == idd:
            if aux.proximo == aux:
                return None
            else:
                aux.anterior.proximo = aux.proximo
                aux.proximo.anterior = aux.anterior
                if aux == lista:
                    return aux.proximo
                else:
                    return lista
        aux = aux.proximo
        if aux == lista:
            print("Atleta não encontrado.")
            return lista

def simularBastao(lista, voltas=5):
    if lista is None:
        print("Lista vazia.")
        return
    atual = lista
    encontrou = False
    aux = lista
    while True:
        if aux.bastao:
            atual = aux
            encontrou = True
            break
        aux = aux.proximo
        if aux == lista:
            break
    if not encontrou:
        lista.bastao = True
        atual = lista
    qtd = 1
    aux = lista.proximo
    while aux != lista:
        qtd += 1
        aux = aux.proximo
    passos = qtd * voltas
    for p in range(passos):
        print("Atleta: ", atual.idd, "(Volta", (p // qtd) + 1, ") -> Bastão: ", atual.bastao)
        atual.bastao = False
        atual = atual.proximo
        atual.bastao = True

def main():
    lista = None
    lista = adicionar(lista, 1, True)
    lista = adicionar(lista, 2)
    lista = adicionar(lista, 3)
    lista = adicionar(lista, 4)

    print("Simulação da passagem do bastão: ")
    simularBastao(lista, voltas=5)

main()
