class Contato:

    def __init__(self, nome, telefone, email):
        self.nome = nome
        self.telefone = telefone
        self.email = email


user1 = Contato("Amanda", 991625300, "amandarooscosta@gmail.com")
user2 = Contato("Ana", 991825300, "ana@gmail.com")
user3 = Contato("Anna", 996625300, "anna@gmail.com")
user4 = Contato("Ana Luh", 991625920, "analuh@gmail.com")
user5 = Contato("Anna Luh", 991777300, "annaluh@gmail.com")

agenda = [user1, user2, user3, user4, user5]

for Contato in agenda:
    print(Contato.nome)
    print(Contato.telefone)
    print(Contato.email)
  
