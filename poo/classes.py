"""
POO - Classes

Em POO, Classes nada mais são do que modelos dos objetos do mundo real sendo representados
computacionalmente.

Imagine que você queira fazer um sistema para automatizar o controle das lâmpadas da sua casa.

Classes podem conter:
   - Atributos -> Representam as caracteristicas do objeto. Ou seja, pelos atributos conseguimos representar
    computacionalmente os estados de um objeto. No caso da lâmpada, possivelmente  iríamos saber se a lâmpada
    é 110 ou 220 volts, se ela é branca, amarela, vermelha ou outra cor, qual é a luminosidade dela e etc...

   - Métodos (funções) -> Representam os comportamentos do objeto. Ou seja, as ações que este objeto pode
     realizar no seu sistema. No caso da lâmpda, por exemplo, um comportamento comum que muito provalvemente
     iríamos querer representar no nosso sistema é o de ligar e desligar a mesma.

Em Python, para definir uma classe utilizamos a palavra reservada class.

OBS: Utilizamos a palavra 'pass' em Python quando temos um bloco de código que ainda não está implementado.

OBS: Quando nomeamos nossas classes em Python utilizamos por convenção o nome com inicial em maiúsculo. Se o
nome for composto, utiliza-se as iniciais de ambas as palavras em maiúsculo, todas juntas.

Dica: Em computação não utilizamos: Acentuação, caracteres especiais, espaços ou similares para nomes de classes,
atributos, métodos, arquivos, diretórios e etc...

OBS: Quando estamos planejando um software e definimos quais classes teremos que ter no sistema, chamamos
estes objetos que serão mapeados para classes de entidade.

OBS:
- As Classes internas do Python são nomeadas em minúsculas: conferir com print(help(int));
- Já as Classes definidas pelo programador devem ser nomeadas com a inicial em maiúsculas;
Essa convenção existe justamente para diferenciar o que é da linguagem do que é feita pelo programador.
"""


class Lampada:
    pass


lamp = Lampada()
print(lamp)
print(type(lamp))


class ContaCorrente:
    pass


class Produto:
    pass


class Usuario:
    pass