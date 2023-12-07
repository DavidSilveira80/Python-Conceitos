"""
POO - Abstração e Encapsulamento

O grande objetivo da POO é encapsular nosso código dentro de um grupo lógico e hierárquico utilizando classes.

Encapsular -. cápsula

           Classe
-----------------------------
/                           /
/      Atributos e métodos  /
/                           /
/----------------------------/

# Relembrando Atributos/Métodos privados em Python

Imagine que temos uma classe chamada Pessoa, contendo um atributo
privado chamado __nome e um método privado chamada __falar()

Esses elelemntos privados só devem/deveriam ser acessados dentro da classe.
É possível criar métodos de acesso e alteração dessas variáveis.


# Abstração, em POO, é o ato de expor apenas dados relevantes de uma classe, escondendo atributos e métodos
privados de usuário.

"""


class Conta:

    contador = 400

    def __init__(self, titular, saldo, limite):
        Conta.contador += 1
        self.__numero = Conta.contador
        self.__titular = titular
        self.__saldo = saldo
        self.__limite = limite

    def get_titular(self):
        return self.__titular

    def get_saldo(self):
        return self.__saldo

    def get_limite(self):
        return self.__limite

    def extrato(self):
        print(f'Saldo de {self.__saldo} do títular {self.__titular} com o limite de {self.__limite} ')

    def depositar(self, valor):
        self.__saldo += valor

    def sacar(self, valor):
        self.__saldo -= valor

    def transferir(self, valor, conta_destino):
        self.__saldo -= valor
        conta_destino.__Conta__saldo += valor


conta1 = Conta('David', 150, 1500)

print(conta1.get_titular())
print(conta1.get_saldo())
print(conta1.get_limite())
