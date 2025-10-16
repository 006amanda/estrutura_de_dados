def menu():
    print("MENU: ")
    print("1. Adicionar jogador ao final da fila")
    print("2. Remover jogador específico")
    print("3. Simular 1 rodada")
    print("4. Simular N rodadas")
    print("5. Mostrar fila")
    print("6. Mostrar próximo a jogar")
    print("7. Limpar fila")
    print("8. Sair")

def main():
    fila = []

    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            jogador = input("Digite o nome do jogador: ")
            fila.append(jogador)
            print("Jogador ", jogador, " adicionado ao final da fila")

        elif opcao == "2":
            jogador = input("Digite o nome do jogador a remover: ")
            nova_fila = []
            encontrado = False
            for j in fila:
                if j != jogador:
                    nova_fila.append(j)
                else:
                    encontrado = True
            fila = nova_fila
            if encontrado:
                print("Jogador ", jogador, " removido da fila.")
            else:
                print("Jogador ", jogador, " não encontrado na fila.")

        elif opcao == "3":
            if fila:
                jogador = fila.pop(0)
                print("Rodada: ", jogador, " jogou e volta para o final da fila.")
                fila.append(jogador)
            else:
                print("A fila está vazia")

        elif opcao == "4":
            if fila:
                n = int(input("Quantas rodadas deseja simular? "))
                for i in range(n):
                    jogador = fila.pop(0)
                    print("Rodada ", i+1, ":", jogador, " jogou e volta para o final da fila.")
                    fila.append(jogador)
                    print("Fila atual: ")
                    for j in fila:
                        print("-> ", j)
            else:
                print("A fila está vazia.")

        elif opcao == "5":
            if fila:
                print("Fila atual:")
                for j in fila:
                    print("-", j)
            else:
                print("A fila está vazia.")

        elif opcao == "6":
            if fila:
                print("Próximo a jogar:", fila[0])
            else:
                print("A fila está vazia.")

        elif opcao == "7":
            fila = []
            print("Fila limpa com sucesso.")

        elif opcao == "8":
            print("Saindo do programa...")
            break

main()
