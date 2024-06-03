"""
Sistema de Contas Bancárias:
Crie uma classe base chamada ContaBancaria com os atributos numero_conta, titular e saldo, e métodos para
depositar e sacar. Em seguida, crie uma classe derivada chamada ContaPoupanca que herda de ContaBancaria e
adicione um novo atributo taxa_juros. Adicione um método na classe ContaPoupanca para calcular os juros acumulados
com base na taxa de juros e no saldo atual.
"""


class ContaBancaria:

    def __init__(self, numero_conta, titular, saldo):
        self.numero_conta = numero_conta
        self.titular = titular
        self.saldo = saldo

    def depositar(self, valor):
        self.saldo += valor

    def sacar(self, valor):
        self.saldo -= valor


class ContaPoupanca(ContaBancaria):

    def __init__(self, numero_conta, titular, saldo, taxa_juros):
        super().__init__(numero_conta, titular, saldo)
        self.taxa_juros = taxa_juros

    def calcular_juros(self):
        return self.saldo * (self.taxa_juros / 100)


conta1 = ContaPoupanca('1230', 'David', 50.0, 5)

print(conta1.saldo)
print(conta1.taxa_juros)
print(conta1.calcular_juros())
conta1.depositar(50)
print(conta1.saldo)
print(conta1.calcular_juros())
conta1.sacar(25)
print(conta1.saldo)
print(conta1.calcular_juros())
