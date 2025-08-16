class Funcionario:
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo

    def calcular_bonus(self):
        if self.cargo == "Gerente":
            return self.salario * 0.10
        else:
            return self.salario * 0.05
    
    def salario_com_bonus(self):
        return self.salario + self.calcular_bonus()

funcionario1 = Funcionario("Maria", 2500, "Gerente")
funcionario2 = Funcionario("João", 1500, "Auxiliar Administrativo")

print("Nome:", funcionario1.nome, "| Salário com bônus: R$", funcionario1.salario_com_bonus(), "| Cargo:", funcionario1.cargo)
print("Nome:", funcionario2.nome, "| Salário com bônus: R$", funcionario2.salario_com_bonus(), "| Cargo:", funcionario2.cargo)
