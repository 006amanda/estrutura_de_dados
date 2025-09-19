class No:
    def __init__(self, nome):
        self.nome = nome
        self.proximo = None
        self.anterior = None

def adicionar(lista, nome):
    novo = No(nome)

    if lista is None:
        lista = novo
        lista.proximo = novo
        lista.anterior = novo
        return lista
    else:
        ultimo = lista.anterior
        novo.proximo = lista
        novo.anterior = ultimo
        ultimo.proximo = novo
        lista.anterior = novo
        return lista

def remover(lista, cliente):
    aux = lista
    if lista is None:
        print("Pizzaria vazia")
        return None

    while True:
        if aux.nome == cliente:
            if aux.proximo == aux:
                return None
            else:
                aux.proximo.anterior = aux.anterior
                aux.anterior.proximo = aux.proximo
                if aux == lista:
                    return aux.proximo
                else:
                    return lista
        aux = aux.proximo

        if aux == lista:
            print(cliente, " não encontrado")
            return lista

def simularPizza(lista, voltas):
    if lista is None:
        print("Pizzaria vazia")
        return

    atual = lista
    for i in range(voltas):
        print("A pizza foi para", atual.nome)
        atual = atual.proximo

def main():
    lista = None
    lista = adicionar(lista, "Amanda")
    lista = adicionar(lista, "Marcelo")
    lista = adicionar(lista, "Fernanda")
    lista = adicionar(lista, "Matheus")
    lista = adicionar(lista, "Lucas")

    print("Início do rodízio: ")
    simularPizza(lista, 6)

    print()
    print("Um cliente foi embora.")
    lista = remover(lista, "Matheus")
    print()

    print("Continuação do rodízio: ")
    simularPizza(lista, 6)
main()
