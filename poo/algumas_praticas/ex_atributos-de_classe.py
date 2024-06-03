"""
Contador de Instâncias:
Crie uma classe Animal com um atributo de classe contador_instancias que mantém a contagem de quantas instâncias
da classe foram criadas. Adicione um método para exibir o valor do contador de instâncias. Cada vez que um novo
objeto Animal for criado, o contador deve ser incrementado. Crie algumas instâncias da classe e exiba o valor
do contador.
"""

# Animal


class Animal:
    contador_instancias = 0

    def __init__(self, nome):
        self.id = Animal.contador_instancias + 1
        Animal.contador_instancias = self.id
        self.nome = nome

    @classmethod
    def exibir_contador(cls):
        return cls.contador_instancias


cachorro1 = Animal('Pincher')
cachorro2 = Animal('Pastor Alemão')
cachorro3 = Animal('Lebreiro')

print(f'Foram criadas {Animal.contador_instancias} instâncias da classe Animal.')
