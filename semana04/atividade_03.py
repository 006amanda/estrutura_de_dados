class No:
    def __init__(self, descricao, prazo):
        self.descricao = descricao
        self.prazo = prazo
        self.proximo = None
        self.anterior = None

def menu():
    print("MENU")
    print("1 - Inserir tarefa")
    print("2 - Remover tarefa")
    print("3 - Listar tarefas")
    print("4 - Sair ")
    opcao = int(input("Digite uma opção: "))
    return opcao

def inserirTarefa(lista, descricao, prazo):
    nova = No(descricao, prazo)
    if lista == None:
        lista = nova
    else:
        nova.proximo = lista
        lista.anterior = nova
        lista = nova
    return lista

def removerTarefa(lista, descricao):
    atual = lista
    while atual is not None:
        if atual.descricao == descricao:
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
    print("Tarefa não encontrada")
    return lista

def listarTarefas(lista):
    if lista == None:
        print("Nenhuma tarefa cadastrada")
        return
    atual = lista
    while atual is not None:
        print("Descrição: ", atual.descricao)
        print("Prazo: ", atual.prazo)
        print()
        atual = atual.proximo

def main():
    lista = None
    opcao = 0
    while opcao != 4:
        opcao = menu()
        if opcao == 1:
            descricao = input("Digite a descrição da tarefa: ")
            prazo = input("Digite o prazo: ")
            lista = inserirTarefa(lista, descricao, prazo)
        elif opcao == 2:
            descricao = input("Digite a descrição da tarefa para remover: ")
            lista = removerTarefa(lista, descricao)
        elif opcao == 3:
            listarTarefas(lista)
        elif opcao == 4:
            print("Até breve")

main()
