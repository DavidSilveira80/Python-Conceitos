"""
Poo - Herança (Inheritance)

A ideia de herança é a de reaproveitar código. Também extender nossas classes.

OBS: Com a herança, a partir de uma classe existente, nós extendemos outra classe
que passa a herdar atributos e métodos da classe herdada.

Cliente
   - nome;
   - sobrenome;
   - cpf;
   - renda;

Funcionario:
   - nome;
   - sobrenome;
   - cpf;
   - matricula;

Perguntar: Existe alguma entidade genérica o suficiente para encapsular os atributos e métodos comuns a
outras entidades?

class Cliente:

    def __init__(self, nome, sobrenome, cpf, renda):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf
        self.renda = renda

    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'


class Funcionario:

    def __init__(self, nome, sobrenome, cpf, matricula):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf
        self.matricula = matricula

    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'

OBS: Quando uma classe herda de outra classe ela herda TODOS os atributos e métodos da classe herdada.

Quando uma classe herda outra classe, a classe herdada é conhecida por:
       [Pessoa]
       - Super Classe;
       - Classe Mãe;
       - Classe Pai;
       - Classe Base;
       - Classe Genérica;

Quando uma classe herda de outra classe, ela é chamada:
       [Cliente, Funcionario]
       - Sub classe;
       - classe Filha;
       - Classe Específica;


class Pessoa:

    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf

    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'


class Cliente(Pessoa):
    # Cliente herda de Pessoa

    def __init__(self,nome, sobrenome, cpf, renda):
        super().__init__(nome, sobrenome, cpf)
        self.renda = renda


class Funcionario(Pessoa):
    # Funcionario herda de Pessoa

    def __init__(self,nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)
        self.matricula = matricula


cliente1 = Cliente('Angelina', 'Jolie', '123.456.789.00', 5000)
funcionario1 = Funcionario('Felicity', 'jones', '987.654.321.11', 1234)



print(cliente1.nome_completo())
print(funcionario1.nome_completo())

# Sobrescrita de Métodos (Overriding)

Sobrescrita de método, ocorre quando reescrevemos/reimplementamos um método presente na super classe
 em classes filhas.

"""


class Pessoa:

    def __init__(self, nome, sobrenome, cpf):
        self.nome = nome
        self.sobrenome = sobrenome
        self.cpf = cpf

    def nome_completo(self):
        return f'{self.nome} {self.sobrenome}'


class Cliente(Pessoa):
    # Cliente herda de Pessoa

    def __init__(self,nome, sobrenome, cpf, renda):
        super().__init__(nome, sobrenome, cpf)
        self.renda = renda


class Funcionario(Pessoa):
    # Funcionario herda de Pessoa

    def __init__(self, nome, sobrenome, cpf, matricula):
        super().__init__(nome, sobrenome, cpf)
        self.matricula = matricula

    def nome_completo(self):
        print(super().nome_completo())  # método da super classe
        return f'Funcionário: {self.matricula} Nome: {self.nome}'


cliente1 = Cliente('Angelina', 'Jolie', '123.456.789.00', 5000)
funcionario1 = Funcionario('Felicity', 'jones', '987.654.321.11', 1234)


print(cliente1.nome_completo())
# print(funcionario1.nome_completo())
print(funcionario1.nome_completo())
