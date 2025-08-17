class Aluno:
    def __init__(self, nome, notas):
        self.nome = nome
        self.notas = notas

    def calcular_media(self):
        return sum(self.notas) / len(self.notas)

    def verificar_aprovacao(self):
        if self.calcular_media() >= 7:
            return "Aprovado"
        else:
            return "Reprovado"

maria = Aluno("Maria", [9, 8, 7])
joao = Aluno("João", [8, 8, 4])
print("Nome: ", maria.nome, " | Média: ", maria.calcular_media(), " | Situação: ", maria.verificar_aprovacao())
print("Nome: ", joao.nome, " | Média: ", joao.calcular_media(), " | Situação: ", joao.verificar_aprovacao())
