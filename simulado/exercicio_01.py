class No:
    def __init__(self, id, altitude):
        self.id = id
        self.altitude = altitude
        self.integridade = 100
        self.proximo = None
        self.anterior = None

def cadastrar(lista, id, altitude):
    novo = No(id, altitude)
    if lista is None:
        return novo
    atual = lista
    while atual.proximo:
        atual = atual.proximo
    atual.proximo = novo
    novo.anterior = atual
    return lista

def listar(lista):
    if lista is None:
        print("Nenhum satélite")
        return
    atual = lista
    while atual:
        print("ID: ", atual.id)
        print("Altitude: ", atual.altitude)
        print("Integridade: ", atual.integridade, "%")
        atual = atual.proximo

def remover(lista, id):
    if lista is None:
        return None
    atual = lista
    while atual:
        if atual.id == id:
            if atual.anterior:
                atual.anterior.proximo = atual.proximo
            else:
                lista = atual.proximo
            if atual.proximo:
                atual.proximo.anterior = atual.anterior
            break
        atual = atual.proximo
    return lista

def simular_voltas(lista, voltas=3):
    for volta in range(1, voltas + 1):
        print("Volta: ", volta)

        atual = lista
        cont = 0

        while atual and cont < 2:
            atual.integridade -= 20
            if atual.integridade <= 0:
                id_remover = atual.id
                atual = atual.proximo
                lista = remover(lista, id_remover)
            else:
                atual = atual.proximo
            cont += 1
        listar(lista)
    return lista

def main():
    lista = None
    lista = cadastrar(lista, "Hubble", 550)
    lista = cadastrar(lista, "James Webb", 1500)
    lista = cadastrar(lista, "Amazônia-1", 780)
    
    print("Satélites cadastrados: ")
    listar(lista)
    
    lista = simular_voltas(lista, 3)

main()
