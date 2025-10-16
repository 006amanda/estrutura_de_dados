def menu():
    print("1. Inserir operação na pilha")
    print("2. Retirar última operação")
    print("3. Mostrar última operação inserida")
    print("4. Mostrar todas as operações pendentes")
    print("5. Sair")

def main():
    pilha = []

    while True:
        menu()
        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            operacao = input("Digite a operação: ")
            pilha.append(operacao)
            print("Operação ", operacao, " inserida na pilha.")

        elif opcao == "2":
            if len(pilha) > 0:
                removida = pilha.pop()
                print("Operação ", removida, " removida da pilha.")
            else:
                print("A pilha está vazia. Nada a remover.")

        elif opcao == "3":
            if len(pilha) > 0:
                print("Última operação inserida:", pilha[len(pilha)-1])
            else:
                print("A pilha está vazia.")

        elif opcao == "4":
            if len(pilha) > 0:
                print()
                print("Operações pendentes na pilha: ")
                indice = len(pilha) - 1
                while indice >= 0:
                    print("-", pilha[indice])
                    indice -= 1
            else:
                print("Nenhuma operação pendente.")

        elif opcao == "5":
            print("Saindo do programa...")
            break
main()
