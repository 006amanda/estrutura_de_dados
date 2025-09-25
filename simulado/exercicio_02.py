class No:
    def __init__(self, nome, pais):
        self.nome = nome
        self.pais = pais
        self.proximo = None

def inserir(lista, nome, pais):
    novo = No(nome, pais)
    if lista is None:
        return novo
    atual = lista
    while atual.proximo:
        atual = atual.proximo
    atual.proximo = novo
    return lista

def exibir(lista):
    if lista is None:
        print("Lista vazia")
        return
    atual = lista
    while atual:
        print(atual.nome, " -> ", atual.pais)
        atual = atual.proximo

def remover(lista, nome):
    if lista is None:
        return None
    if lista.nome == nome:
        return lista.proximo
    atual = lista
    while atual.proximo:
        if atual.proximo.nome == nome:
            atual.proximo = atual.proximo.proximo
            break
        atual = atual.proximo
    return lista

def main():
    lista = None
    lista = inserir(lista, "Hubble", "EUA")
    lista = inserir(lista, "James Webb", "UK")
    lista = inserir(lista, "Amazônia-1", "BR")
    print("Lista atual: ")
    exibir(lista)
    print()
    lista = remover(lista, "Hubble")
    print("Lista atualizada: ")
    exibir(lista)

main()
