class Aluno:
    def __init__(self, nome, notas):
        self.nome = nome
        self.notas = notas

    def calcular_media(self):
        return sum(self.notas) / len(self.notas)

ana = Aluno("Ana", [7, 8, 6])
pedro = Aluno("Pedro", [5, 9, 6])
carlos = Aluno("Carlos", [7, 8, 7])
turma = [ana, pedro, carlos]

for aluno in turma:
    print("Nome: ", aluno.nome, " | Média: ", aluno.calcular_media())
