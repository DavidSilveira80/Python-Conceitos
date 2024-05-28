"""
POO - Atributos

Atributos -> Representam as caracteristicas do objeto, Ou seja pelos atributos nós conseguimos representar
computacionalmente os estados de um objeto.

Em Python, dividimos os atributos em 3 grupos:
        - Atributos de instância;
        - Atributos de classe;
        - Atributos Dinâmicos;

# Atributo de instância:  São atributos declarados dentro do método construtor.

# OBS: Método construtor: É um método especial que utlizamos para a construção do objeto.

# Em Java, uma classe Lâmpada, incluindo seus atributos ficaria mais ou menos:

public classs Lampada(){
    private int voltagem;
    private String cor;
    private Boolean ligada = false;

    public Lampada(int voltagem, String cor){
        this.voltagem = voltagem;
        this.cor = cor;
    }
}

# Em Python, por convenção, ficou estabelecido que, todos os atributos de uma classe é público.
Ou seja, pode ser acessado em qualquer parte do projeto.
Caso queiramos demonstrar que determinado atributo deve ser tratado como privado, ou seja, que deve ser
acessado/utilizado somente da própria classe onde está declarado, utiliza-se: __ duplo undescore no início
de seu nome.

Isso é conhecido também como Name Mangling.
"""

# Classes com Atributos de Instância Públicos


class Lampada:

    def __int__(self, voltagem, cor):  # Método construtor
        self.voltagem = voltagem
        self.cor = cor
        self.ligada = False


class ContaCorrente:

    def __init__(self, numero, limite, saldo):
        self.numero = numero
        self.limite = limite
        self.saldo = saldo


class Produto1:

    def __init__(self, nome, descricao, valor):
        self.nome = nome
        self.descricao = descricao
        self.valor = valor


class Usuario:

    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha


# Atributos públicos e privados

class Acesso:
    def __init__(self, email, senha):
        self.email = email  # publico
        self.__senha = senha  # privado

    def mostra_senha(self):
        return self.__senha

    def mostra_email(self):
        return self.email

#  OBS: Lembre-se que isso é uma convenção, ou seja, a linguagem Python não vai
#  impedir que façamos acesso aos atributos sinalizados como privados fora da classe

# Exemplo


user = Acesso('user@email.com', '123456')

print(user.email)

# print(user.__senha) # AttributeError


print(user._Acesso__senha)  # Temos acesso. Mas não deveriamos fazer este acesso. Name Mangling.
print(f'Senha: {user.mostra_senha()}')  # Modo correto de acessar.
print(user.mostra_email())

"""
O Que significa atributos de instância?

Significa, que ao criarmos instâncias/objetos de uma classe, todas as instâncias terão estes atributos.
"""

user1 = Acesso('user1@email.com', '123456')
user2 = Acesso('user2@email.com', '78910')

print(user1.mostra_email())
print(user2.mostra_email())

# Atributos de Classe
# Atributos de classe, são declarados diretamente na classe, ou seja, fora do construtor. Geralmente já
# inicializamos um valor, e este valor é compartilhado entre todas as instâncias da classe. Ou seja ao invés
# de cada instãncia da classe ter seus próprios valores como é o caso dos atributos de instância, com
# os atributos de classe todas as instâncias terão o mesmo valor para este atributo.


class Produto:
    # Atributo de classe
    imposto = 1.05  # 0.05% de imposto
    contador = 0

    def __init__(self, nome, descricao, valor):
        self.id = Produto.contador + 1
        Produto.contador = self.id
        self.nome = nome
        self.descricao = descricao
        self.valor = (valor * Produto.imposto)


produto1 = Produto('PlayStation 5', 'Vídeo Game', 5300)
produto2 = Produto('Xbox 5', 'Vídeo Game', 4500)

print(produto1.imposto)  # Acesso possível, mas incorreto de um atributo de classe
print(produto2.imposto)  # Acesso possível, mas incorreto de um atributo de classe

print(Produto.imposto)  # Acesso correto de um atributo de classe

print(f'Nome: {produto1.nome}, Valor: {produto1.valor}')
print(f'Nome: {produto1.nome}, id: {produto1.id}')
print(f'Nome: {produto2.nome}, Valor: {produto2.valor}')
print(f'Nome: {produto2.nome}, id: {produto2.id}')

# OBS: Não precisamos criar uma instância de uma classe para fazer acesso a um atributo de classe

print(Produto.imposto)  # Acesso correto de um atributo de classe

#  OBS: Em linguagens como o Java, os atributos conhecidos como atributos de classe aqui em Python
#  são chamados de atributos estáticos;

# Atributos Dinâmicos -> Um atributo de instância que pode ser criado em tempo de execução.

# OBS: O atributo dinâmico será exclusivo da instância que o criou.

arroz = Produto('Arroz', 'Mercearia', 5.99)

# Criando um atributo dinâmico em tempo de execução

arroz.peso = '5kg'  # Note que na classe produto não existe o tributo peso

print(arroz.peso)

# Deletando atributos

print(produto1.__dict__)
print(arroz.__dict__)

del arroz.peso

print(produto1.__dict__)
print(arroz.__dict__)
