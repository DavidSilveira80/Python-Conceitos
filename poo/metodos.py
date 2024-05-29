"""
POO - Métodos

- Métodos (funções) -> Representam os comportamentos do objeto. Ou seja, as ações que este objeto pode
realizar no seu sistema.

Em Python, dividimos os métodos, em 2 grupos: Métodos de instância e Métodos de classe.

# Métodos de Instância

# O método dunder init __init__ é um método especial chamado de construtor e sua função é construir o objeto
a partir da classe.

OBS: Todo elemento em Python que inicia e finaliza com duplo underline __ é chamado de dunder (Double Underline)

OBS: Os métodos/funções dunder em Python são chamados de métodos mágicos.

ATENÇÃO!! Por mais que possamos criar nossas próprias funções utilizando dunder não é aconselhado. Python
possui vários métodos com esta nomenclatura e pode ser que mudemos o comportamento dessas funções mágicas
internas da linguagem. Então, evite ao máximo. De preferência nunca os faça.

# Métodos são escritos em letras minúsculas. Se o nome for composto, o nome terá as palavras separadas por
underline _ (snack_case).

# Métodos de classe em Python são conhecidos como métodos Estáticos em outras linguagens.

"""


class Lampada:
    def __init__(self, cor, voltagem, luminosidade):
        self.cor = cor
        self.voltagem = voltagem
        self.luminosidade = luminosidade
        self.ligada = False


class ContaCorrente:

    contador = 4999

    def __init__(self, limite, saldo):
        self.numero = ContaCorrente.contador + 1
        self.limite = limite
        self.saldo = saldo
        ContaCorrente.contador = self.numero


class Produto:

    contador = 0

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1
        self.nome = nome
        self.descricao = descricao
        self.valor = valor
        Produto.contador = self.id

    def desconto(self, porcentagem):  # Método de Instância
        """Retorna o valor do produto com o desconto"""
        return (self.valor * (100 - porcentagem)) / 100


class Usuario:

    contador = 0

    @classmethod
    def conta_usuarios(cls):
        """Método de Classe"""
        print(f'Temos {cls.contador} usuários no sistema.')


    @staticmethod
    def definicao():
        """Método estático"""
        return 'UXR344'

    def __init__(self, nome, sobrenome, email, senha):
        self.__id = Usuario.contador + 1
        Usuario.contador = self.__id
        self.__sobrenome = sobrenome
        self.__nome = nome
        self.__email = email
        self.__senha = senha
        print(f'Usuário criado: {self.__gera_usuario()}')

    def nome_completo(self):
        """Método de instância"""
        return f'{self.__nome} {self.__sobrenome}.'

    def __gera_usuario(self):
        """Método privado só para uso interno"""
        return self.__email.split('@')[0]


user1 = Usuario('Angelina', 'Jolie', 'angelina@email.com', '123456')
user2 = Usuario('Felicity', 'Jones', 'felicity@email.com', '654321')

print(user1.nome_completo())
print(user2.nome_completo())


# Métodos de Classe

user = Usuario('Chris', 'Pratt', 'cris@email.com', '123457')

Usuario.conta_usuarios()  # Forma correta
user.conta_usuarios()  # Possível, mas incorreta


# Método Estático

print(Usuario.definicao())
print(user.definicao())
