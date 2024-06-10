"""
POO - Interfaces

Interfaces definem o que uma classe deve fazer e não como;

Interface não é um conceito nativo da linguagem Python, mas é possível simular
interfaces usando classes da bibliotéca abc (Abstract Base Classes)

OBS: Classes abstratas não podem ser instânciadas.

Uma interface é um contrato que define métodos que devem ser implementados por
qualquer classe que implemente essa interface. No Python usamos classes abstratas
para definir esses métodos que devem ser decorados com '@abstractmethod' e assegurar
que qualquer classe derivada deve implementar
esse métodos, caso contrário, a classe não poderá ser instânciada.

class Animal(ABC):
    @abstractmethod
    def faz_som(self):
        pass

    @abstractmethod
    def andar(self):
        pass



class Gato(Animal):

    def andar(self):
        return 'correndo...'

gatinho = Gato()

Gera um TypeError: Can't instantiate abstract class Gato with abstract method faz_som

"""

# Passo 1 -> Definindo uma interface

"""
Primeiro, impotamos os módulos necessaŕios da biblioteca 'abc' e definimos uma classe
abstrata com os métodos abstratos que queremos na nossa interface
"""

from abc import ABC, abstractmethod


class Animal(ABC):
    @abstractmethod
    def faz_som(self):
        pass

    @abstractmethod
    def andar(self):
        pass


"""
Aqui, 'Animal' é uma classe abstrata que define dois métodos abstratos: 'faz_som' e 'andar'.
Qualquer classe que herdar de 'Animal' terá que implementar esse métodos.
"""

# Passo 2 -> Implementando a interface

"""
Agora, vamos criar algumas classes que implementam essa interface.
"""


class Cachorro(Animal):
    def faz_som(self):
        return 'au au'

    def andar(self):
        return 'andando..'


class Gato(Animal):
    def faz_som(self, som):
        return som

    def andar(self):
        return 'correndo...'

"""
Aqui, 'Cachorro' e 'Gato' são classes que herdam de 'Animal' e implementam os métodos
'faz_som' e 'andar'.
"""

# Passo 3 -> Usando as Classes

"""Podemos agora criar instâncias e usar seus métodos."""

cusco = Cachorro()
print(cusco.faz_som())
print(cusco.andar())

gatinho = Gato()
print(gatinho.faz_som('miau-miau'))
print(gatinho.andar())
