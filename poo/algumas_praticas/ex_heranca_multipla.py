"""
Criar uma hierarquia de classes que representa aparelhos domésticos inteligentes, utilizando
herança múltipla em Python.

Você deve criar classes base e subclasses que combinam funcionalidades para simular aparelhos
domésticos inteligentes, como uma geladeira inteligente.

"""


class Aparelho:

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
        self.ligado = None

    def ligar(self):
        self.ligado = True

    def desligar(self):
        self.ligado = False


class Inteligente:
    def __init__(self):
        self.conectado = None

    def conectar_internet(self):
        self.conectado = True

    def desconectar_internet(self):
        self.conectado = False

    def atualizar_software(self):
        print('Atualizando Software...')


class GeladeiraInteligente(Aparelho, Inteligente):
    def __init__(self, marca, modelo):
        Aparelho.__init__(self, marca, modelo)
        Inteligente.__init__(self)
        self.temperatura = 0.0

    def ajustar_temperatura(self, nova_temperatura):
        if self.ligado and self.conectado:
            print(f'Ajustando temperatura para {nova_temperatura}°')
            self.temperatura = nova_temperatura
        else:
            print('A Geladeira não está ligada e nem conectada a Internet')

    def verificar_comida(self):
        if self.ligado and self.conectado:
            print('Há 5 tipos de comida na geladeira')
        else:
            print('A geladeira não está ligada e nem conectada á internet.')


geladeira = GeladeiraInteligente('Brastemp', 'xpto')


geladeira.ajustar_temperatura(27.5)
geladeira.ligar()
geladeira.conectar_internet()
print(geladeira.temperatura)
geladeira.ajustar_temperatura(25.5)
print(geladeira.temperatura)
geladeira.desconectar_internet()
geladeira.desligar()
geladeira.verificar_comida()
geladeira.ligar()
geladeira.conectar_internet()
geladeira.verificar_comida()

