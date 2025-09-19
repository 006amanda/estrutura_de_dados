class No:
    def __init__(self, nome, idade, prioridade):
        self.nome = nome
        self.idade = idade
        self.prioridade = prioridade
        self.proximo = None
        self.anterior = None

def inserir(lista, nome, idade, prioridade):
    novo = No(nome, idade, prioridade)

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

def remover(lista,  paciente):
    aux = lista
    if lista is None:
        return None

    while True:
        if aux == paciente:
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

def mostrar(lista):
    if lista is None:
        print("Nenhum paciente")
        return

    aux = lista
    while True:
        print("Paciente: ", aux.nome, "| Idade: ", aux.idade, "| Prioridade: ", aux.prioridade)
        aux = aux.proximo
        if aux == lista:
            break

def simular_atendimento(lista):
    prioridades = ["emergência", "urgente", "normal"]

    while lista is not None:
        atendido = None
        for prioridade in prioridades:  
            aux = lista
            while True:
                if aux.prioridade == prioridade:
                    atendido = aux
                    break
                aux = aux.proximo
                if aux == lista:
                    break
            if atendido is not None:
                break

        print("Atendendo paciente: ", atendido.nome, "| Idade: ", atendido.idade, "| Prioridade: ", atendido.prioridade)
        lista = remover(lista, atendido)
    print("Todos os pacientes foram atendidos")

def main():
    lista = None
    lista = inserir(lista, "Amanda", 18, "emergência")
    lista = inserir(lista, "João", 20, "normal")
    lista = inserir(lista, "Nicoly", 19, "urgente")
    lista = inserir(lista, "Carlos", 19, "normal")
    lista = inserir(lista, "Miguel", 18, "urgente")

    print("Pacientes cadastrados: ")
    mostrar(lista)
    print()

    print("Simulação de atendimento: ")
    simular_atendimento(lista)
main()
