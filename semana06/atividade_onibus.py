class No:
    def __init__(self, parada):
        self.parada = parada
        self.proximo = None 
        self.anterior = None

def adicionar(lista, parada):
    novaParada = No(parada)

    if lista is None:
        lista = novaParada
        lista.proximo = novaParada
        lista.anterior = novaParada
        return lista 
    else:
        ultimo = lista.anterior
        novaParada.proximo = lista
        novaParada.anterior = ultimo 
        ultimo.proximo = novaParada
        lista.anterior = novaParada
        return lista

def remover(lista, parada):
    aux = lista 
    if lista is None:
        print("Sem paradas")
        return lista

    while True:
        if aux.parada == parada: 
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
            print("Parada não localizada.")
            return lista

def simular(lista):
    if lista is None:
        print("Nenhuma parada localizada.")
        return lista

    aux = lista
    while True:
        print(aux.anterior.parada, " -> ", aux.parada, " -> ", aux.proximo.parada)
        aux = aux.proximo
        if aux == lista:
            break
    return lista

def menu():
    print("MENU")
    print("1 - Adicionar parada")
    print("2 - Remover parada")
    print("3 - Simular percurso")
    print("4 - Sair")
    opc = int(input("Escolha uma opção: "))
    return opc

def main():
    lista = None
    opc = 0

    while opc != 4:
        opc = menu()
        if opc == 1:
            parada = input("Digite uma parada para adicionar: ")
            lista = adicionar(lista, parada)
        elif opc == 2:
            paradas = input("Digite uma parada para remover: ")
            lista = remover(lista, paradas)
        elif opc == 3:
            print("SIMULAÇÃO DO PERCURSO: ")
            simular(lista)
        elif opc == 4:
            print("Saindo do sistema...")
            break
main()
