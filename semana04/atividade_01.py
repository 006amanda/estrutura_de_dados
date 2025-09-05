class No:
    def __init__(self, nome):
        self.nome = nome
        self.proximo = None
        self.anterior = None

def menu():
    print("1 - Inserir")
    print("2 - Listar")
    print("3 - Remover")
    print("4 - Verificar")
    print("5 - Sair")
    opcao = int(input("Digite uma opção: "))
    return opcao

def inserirNo(lista, nome):
    novo = No(nome)
    if lista == None:
        lista = novo
    else:
        novo.proximo = lista
        lista.anterior = novo
        lista = novo
    return lista

def listarNos(lista):
    if lista == None:
        print("Lista está vazia")
        return
    elemento = lista
    pos = 1
    while elemento is not None:
        print("Posição:", pos, "- Nome:", elemento.nome)
        elemento = elemento.proximo
        pos += 1
    print()

def removerNo(lista, nome):
    elemento = lista
    while elemento is not None:
        if elemento.nome == nome:
            if elemento.anterior == None and elemento.proximo == None:
                return None
            elif elemento.anterior == None:
                elemento.proximo.anterior = None
                return elemento.proximo
            elif elemento.proximo == None:
                elemento.anterior.proximo = None
                return lista
            else:
                elemento.anterior.proximo = elemento.proximo
                elemento.proximo.anterior = elemento.anterior
                return lista
        elemento = elemento.proximo
    print("Nó não encontrado")
    return lista

def verificarNo(lista):
    print("1 - Buscar por nome")
    print("2 - Buscar por identificador")
    escolha = int(input("Digite uma opção: "))

    if escolha == 1:
        nome = input("Digite o nome: ")
        elemento = lista
        while elemento is not None:
            if elemento.nome == nome:
                print("Nó encontrado -> Nome: ", elemento.nome)
                return
            elemento = elemento.proximo
        print("Nó não encontrado")

    elif escolha == 2:
        posicao = int(input("Digite a posição: "))
        elemento = lista
        atual = 1
        while elemento is not None:
            if atual == posicao:
                print("Nó encontrado -> Nome: ", elemento.nome)
                return
            elemento = elemento.proximo
            atual += 1
        print("Nó não encontrado")

def main():
    opcao = 0
    lista = None

    while opcao != 5:
        opcao = menu()
        if opcao == 1:
            nome = input("Digite o nome: ")
            lista = inserirNo(lista, nome)
        elif opcao == 2:
            listarNos(lista)
        elif opcao == 3:
            nome = input("Digite o nome do nó para remover: ")
            lista = removerNo(lista, nome)
        elif opcao == 4:
            verificarNo(lista)

main()
