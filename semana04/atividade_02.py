class No:
    def __init__(self, id, nome, artista, duracao):
        self.id = id
        self.nome = nome
        self.artista = artista
        self.duracao = duracao
        self.proximo = None
        self.anterior = None

def menu():
    print("MENU")
    print("1 - Adicionar música")
    print("2 - Listar músicas")
    print("3 - Remover música")
    print("4 - Buscar música")
    print("5 - Mostrar duração da playlist")
    print("6 - Avançar / Voltar música")
    print("7 - Sair")
    opcao = int(input("Digite uma opção: "))
    return opcao

def adicionarMusica(lista, id, nome, artista, duracao):
    nova = No(id, nome, artista, duracao)
    if lista == None:
        lista = nova
    else:
        nova.proximo = lista
        lista.anterior = nova
        lista = nova
    return lista

def listarMusicas(lista):
    if lista == None:
        print("Playlist vazia")
        return
    atual = lista
    while atual is not None:
        print("ID: ", atual.id)
        print("Nome: ", atual.nome)
        print("Artista: ", atual.artista)
        print("Duração: ", atual.duracao, "min")
        print()
        atual = atual.proximo

def removerMusica(lista, id):
    atual = lista
    while atual is not None:
        if atual.id == id:
            if atual.anterior == None and atual.proximo == None:
                return None
            elif atual.anterior == None:
                atual.proximo.anterior = None
                return atual.proximo
            elif atual.proximo == None:
                atual.anterior.proximo = None
                return lista
            else:
                atual.anterior.proximo = atual.proximo
                atual.proximo.anterior = atual.anterior
                return lista
        atual = atual.proximo
    print("Música não encontrada")
    return lista

def buscarMusica(lista):
    print("1 - Buscar por nome")
    print("2 - Buscar por artista")
    escolha = int(input("Digite uma opção: "))
    if escolha == 1:
        nome = input("Digite o nome da música: ")
        atual = lista
        while atual is not None:
            if atual.nome == nome:
                print("Música encontrada: ")
                print("ID: ", atual.id)
                print("Nome: ", atual.nome)
                print("Artista: ", atual.artista)
                print("Duração: ", atual.duracao, "min")
                return
            atual = atual.proximo
    elif escolha == 2:
        artista = input("Digite o artista: ")
        atual = lista
        while atual is not None:
            if atual.artista == artista:
                print("Música encontrada: ")
                print("ID: ", atual.id)
                print("Nome: ", atual.nome)
                print("Artista: ", atual.artista)
                print("Duração: ", atual.duracao, "min")
                return
            atual = atual.proximo
    print("Música não encontrada")

def duracaoTotal(lista):
    total = 0
    atual = lista
    while atual is not None:
        total += atual.duracao
        atual = atual.proximo
    print("Duração total da playlist: ", total, "min")

def navegarMusicas(lista):
    if lista == None:
        print("Playlist vazia")
        return
    atual = lista
    while True:
        print("Tocando agora:")
        print("ID: ", atual.id)
        print("Nome: ", atual.nome)
        print("Artista: ", atual.artista)
        print("Duração: ", atual.duracao, "min")

        print("1 - Próxima música")
        print("2 - Música anterior")
        print("3 - Sair")
        opcao = int(input("Digite: "))
        if opcao == 1:
            if atual.proximo != None:
                atual = atual.proximo
            else:
                print("Você está na última música.")
        elif opcao == 2:
            if atual.anterior != None:
                atual = atual.anterior
            else:
                print("Você está na primeira música.")
        elif opcao == 3:
            break

def main():
    playlist = None
    opcao = 0

    while opcao != 7:
        opcao = menu()
        if opcao == 1:
            id = input("ID da música: ")
            nome = input("Nome da música: ")
            artista = input("Artista: ")
            duracao = float(input("Duração: "))
            playlist = adicionarMusica(playlist, id, nome, artista, duracao)
        elif opcao == 2:
            listarMusicas(playlist)
        elif opcao == 3:
            id = input("Digite o ID da música para remover: ")
            playlist = removerMusica(playlist, id)
        elif opcao == 4:
            buscarMusica(playlist)
        elif opcao == 5:
            duracaoTotal(playlist)
        elif opcao == 6:
            navegarMusicas(playlist)
        elif opcao == 7:
            print("Até breve")

main()
