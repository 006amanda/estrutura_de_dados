class Node:
    def __init__(self, cliente):
        self.cliente = cliente
        self.proximo = None
        self.anterior = None

class Deque:
    def __init__(self):
        self.inicio = None
        self.fim = None

    def inserir_inicio(self, cliente):
        novo = Node(cliente)
        if self.inicio is None:
            self.inicio = self.fim = novo
        else:
            novo.proximo = self.inicio
            self.inicio.anterior = novo
            self.inicio = novo
        print(cliente, "-> Cliente preferencial")

    def inserir_fim(self, cliente):
        novo = Node(cliente)
        if self.fim is None:
            self.inicio = self.fim = novo
        else:
            novo.anterior = self.fim
            self.fim.proximo = novo
            self.fim = novo
        print(cliente, " - Cliente comum")

    def remover_inicio(self):
        if self.inicio is None:
            print("Sem clientes na fila.")
            return
        print("Cliente atendido: ", self.inicio.cliente)
        print()
        self.inicio = self.inicio.proximo
        if self.inicio:
            self.inicio.anterior = None
        else:
            self.fim = None

    def listar(self):
        if self.inicio is None:
            print("Sem clientes na fila.")
            return
        aux = self.inicio
        print("Ordem atual de atendimento: ")
        while aux is not None:
            print("->", aux.cliente)
            aux = aux.proximo
        print()


def main():
    opcao = 0
    deque = Deque()

    while opcao != 4:
        print("1 - Inserir cliente comum")
        print("2 - Inserir cliente preferencial")
        print("3 - Atendendimento ao cliente - preferencial e comum")
        print("4 - Sair")
        opcao = int(input("Selecione a opção: "))

        if opcao == 1:
            nome = input("Nome do cliente: ")
            deque.inserir_fim(nome)
            print()
            deque.listar()
        elif opcao == 2:
            nome = input("Nome do cliente: ")
            deque.inserir_inicio(nome)
            print()
            deque.listar()
        elif opcao == 3:
            deque.remover_inicio()
            deque.listar()
        elif opcao == 4:
            print("Saindo do sistema...")

main()
