"""
Cadastro de Produtos:
Crie uma classe Produto com atributos nome, preco e quantidade. Implemente um método para calcular o valor
total do estoque (preço * quantidade) e outro método para exibir as informações do produto. Crie alguns objetos
da classe Produto e teste seus métodos.
"""

"""Controle de Funcionários:
Desenvolva uma classe Funcionario com atributos nome, salario e cargo. Adicione um método para aumentar o salário em
 uma porcentagem fornecida.
"""

"""
Biblioteca de Livros:
Crie uma classe Livro com atributos titulo, autor e ano_publicacao. Adicione um método para
verificar se o livro é considerado antigo (publicado há mais de 50 anos). Crie uma instância da classe Livro e teste
seu método.
"""

"""
Gerenciamento de Contas Bancárias:
Crie uma classe ContaBancaria com atributos numero_conta, titular e saldo. Adicione métodos para depositar, sacar
e exibir o saldo. Implemente um método que verifica se a conta está com saldo negativo. Crie algumas contas bancárias
e realize operações de depósito e saque para testar os métodos.
"""


class Produto:

    def __init__(self, nome, preco, quantidade):
        self.nome = nome
        self.preco = preco
        self.quantidade = quantidade

    def calcular_valor_total(self):
        return self.quantidade * self.preco

    def exibir_info_do_produto(self):
        return (
            f'Nome: {self.nome}\nPreço: {self.preco:.2f} R$\nQuantidade: {self.quantidade}\nValor total do Estoque: '
            f'{self.calcular_valor_total():.2f} R$')


class Funcionario:
    def __init__(self, nome, salario, cargo):
        self.nome = nome
        self.salario = salario
        self.cargo = cargo

    def aumenta_salario(self, porcentagem):
        return self.salario + (self.salario * (porcentagem / 100))


class Livro:
    def __init__(self, titulo, autor, ano_publicacao):
        self.titulo = titulo
        self.autor = autor
        self.ano_publicacao = ano_publicacao

    def eh_antigo(self):
        publicado_ha = 2024 - self.ano_publicacao
        if publicado_ha > 50:
            resp = True
        else:
            resp = False
        return resp


if __name__ == "__main__":
    produto = Produto('Martelo', 3.50, 3)

    assert type(produto) == Produto
    assert produto.nome == 'Martelo'
    assert produto.preco == 3.50
    assert produto.quantidade == 3

    assert produto.calcular_valor_total() == 10.50
    assert produto.exibir_info_do_produto() == ('Nome: Martelo\nPreço: 3.50 R$\nQuantidade: 3\nValor total do Estoque: '
                                                '10.50 R$')
    print(produto.exibir_info_do_produto())

    funcionario_teste = Funcionario('Alencar', 5500.99, 'Programador')

    assert type(funcionario_teste) == Funcionario
    assert funcionario_teste.nome == 'Alencar'
    assert funcionario_teste.salario == 5500.99
    assert funcionario_teste.cargo == 'Programador'

    assert funcionario_teste.aumenta_salario(5) == 5776.0395

    livro = Livro('Código Limpo', 'Robert C. Martin', 2009)
    assert type(livro) == Livro
    assert livro.titulo == 'Código Limpo'
    assert livro.autor == 'Robert C. Martin'
    assert livro.ano_publicacao == 2009

    assert livro.eh_antigo() is False
