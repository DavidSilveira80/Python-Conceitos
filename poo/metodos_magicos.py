"""
POO - Métodos Mágicos

Métodos mágicos, são todos os métodos que utilizam dunder.

dunder init -> __init__

    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

dunder -> double Underscore

dunder repr -> Representação do objeto
    def __repr__(self):
        return self.titulo

Como consultar os dunder builtins

dir(__builtins__)
"""


class Livro:
    def __init__(self, titulo, autor, paginas):
        self.titulo = titulo
        self.autor = autor
        self.paginas = paginas

    def __str__(self):  # Terá sempre a prefrência sobre __repr__
        return self.titulo

    def __len__(self):
        return self.paginas


livro1 = Livro('Python Rocks!', 'Geek University', 400)
livro2 = Livro("Inteligência Artificial com Python", "Geek University", 350)

print(livro1)
print(len(livro1))
print(livro2)
print(len(livro2))
