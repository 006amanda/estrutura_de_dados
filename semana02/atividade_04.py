class Livro:
    def __init__(self, titulo, autor, numeroP):
        self.titulo = titulo
        self.autor = autor
        self.numeroP = numeroP

    def informar(self):
        if self.numeroP <= 100:
            return "O livro é curto"
        else:
            return "O livro é longo"

livro1 = Livro("O Menino do Pijama Listrado", "John Boyne", 192)
livro2 = Livro("O Príncipe", "Nicolau Maquiavel", 96)

print("Livro 1:", livro1.titulo, "| Autor:", livro1.autor, "| Número de páginas:", livro1.numeroP)
print(livro1.informar())
print("Livro 2:", livro2.titulo, "| Autor:", livro2.autor, "| Número de páginas:", livro2.numeroP)
print(livro2.informar())
