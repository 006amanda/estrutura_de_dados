import random
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

def remover(lista, alvo):
    aux = lista
    if lista is None:
        return None

    while True:
        if aux.nome == alvo:
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
            return lista


def roletaRussa(quantidade):
    lista = None
    for i in range(1, quantidade + 1):
        nome = "Guerreiro " + str(i)
        lista = adicionar(lista, nome)

    vivos = quantidade
    atual = lista
    while vivos > 1:
        sorteado = random.randint(1, vivos) 
        for _ in range(sorteado - 1):
            atual = atual.proximo
        print(atual.nome, "eliminado")
        proximo = atual.proximo
        lista = remover(lista, atual.nome)
        atual = proximo
        vivos -= 1

    print("Sobrevivente: ", lista.nome)

def main():
    quantidade = int(input("Digite o número de guerreiros: "))
    roletaRussa(quantidade)
main()
