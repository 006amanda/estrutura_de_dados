class Node:
    def __init__(self, chamado):
        self.chamado = chamado 
        self.proximo = None 
        self.anterior = None 
    
class Deque:
    def __init__(self):
        self.inicio = None 
        self.fim = None 

    def inserir_inicio(self, chamado):
        novo = Node(chamado)

        if self.inicio is None:
            self.inicio = self.fim = novo 
        else:
            novo.proximo = self.inicio 
            self.inicio.anterior = novo 
            self.inicio = novo
        print(chamado, " - Chamado adicionado.")
    
    def inserir_fim(self, chamado):
        novo = Node(chamado)

        if self.fim is None:
            self.inicio = self.fim = novo 
        else:
            novo.anterior = self.fim 
            self.fim.proximo = novo 
            self.fim = novo 
        print(chamado, " - Chamado adicionado.")
    
    def remover_fim(self):
        if self.fim is None:
            print("Sem chamados")
            return 
        self.fim = self.fim.anterior
        if self.fim:
            self.fim.proximo = None 
        else: 
            self.inicio = None 
        print("Chamado deletado.")

    def remover_inicio(self):
        if self.inicio is None:
            print("Sem chamados")
            return 
        self.inicio = self.inicio.proximo 
        if self.inicio:
            self.inicio.anterior = None 
        else:
            self.fim = None 
        print("Chamado deletado.")

    def listar(self):
        if self.inicio is None:
            print("Sem chamados")
            return 
        aux = self.inicio
        print()
        while aux is not None:
            print("-> ", aux.chamado)
            aux = aux.proximo 
        print()


def main():
    opcao = 0
    deque = Deque()

    while opcao != 6:
        print("1 - Inserir chamado comum")
        print("2 - Inserir chamado urgente")
        print("3 - Remover no início")
        print("4 - Remover no fim")
        print("5 - Listar chamados")
        print("6 - Sair")
        opcao = int(input("Selecione a opção: "))

        if opcao == 1:
            chamado = input("Inserir chamado comum: ")
            deque.inserir_inicio(chamado)
        elif opcao == 2:
            chamado = input("Inserir chamado urgente: ")
            deque.inserir_fim(chamado)
        elif opcao == 3:
            deque.remover_inicio()
        elif opcao == 4:
            deque.remover_fim()
        elif opcao == 5:
            deque.listar()
        elif opcao == 6:
            print("Saindo do sistema...")

main()
