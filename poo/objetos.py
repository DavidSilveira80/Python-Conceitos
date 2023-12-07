"""
POO - Objetos

Objetos -> São instâncias da classe. Ou seja, após o mapeamento do objeto do mundo real para sua representação
computacional, devemos poder criar quantos objetos forem necessários. Podemos pensar nos objetos/instâncias de
uma classe como variáveis do tipo definido na classe.
"""


class Lampada:

    def __init__(self, cor, voltagem, luminosidade):
        self.__cor = cor
        self.__voltagem = voltagem
        self.__luminosidade = luminosidade
        self.__ligada = False

    def checa_lampada(self):
        return self.__ligada

    def ligar_desligar(self):
        if self.__ligada:
            self.__ligada = False
        else:
            self.__ligada = True


# Instância/Objetos

lamp1 = Lampada('branca', 110, 60)


print(f'A Lâmpada está ligada? {lamp1.checa_lampada()}')
lamp1.ligar_desligar()
print(f'A Lâmpada está ligada? {lamp1.checa_lampada()}')
