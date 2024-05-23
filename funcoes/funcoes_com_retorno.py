"""
Funções com retorno

print() # Não retorna nada só imprime
lista.pop() # Remove e retorna o último elemento da lista.

OBS: Em Python, quando uma função não retorna nenhum valor, o retorno é None

OBS: Funções Python que retornan valores, devem retornar estes valores com a palavra reservada return

OBS: Não precisamos necessariamente criar uma variável para receber o retorno de uma função. Podemos passar a
execução da função para outras funções.

OBS: Sobre a palavra reservada return

1 - Ela finaliza a função, ou seja, ela sai da execução da função;
2 - Podemos ter, em uma função, diferentes returns;
3 - Podemos em uma função, retornar qualquer tipo de dado e até mesmo mútiplos valores;

1) Ela finaliza a função, ou seja, ela sai da execução da função;
def diz_oi():
    print('Estou sendo executado antes do retorno....')
    return 'oi!'
    print('Estou depois do return, nunca serei executado')

2) Podemos ter, em uma função, diferentes returns;
def nova_funcao():
    variavel = True
    if variavel:
        return 4
    elif variavel is None:
        return 3.2
    return 'b'

3) Podemos em uma função, retornar qualquer tipo de dado e até mesmo mútiplos valores;
def outra_funcao():
    return 2, 3, 4, 5

"""

"""
def quadrado_de_7():
    print(7 * 7)
ret = quadrado_de_7()

print(f'Retorno {ret}')

# Vamos refatorar esta função para que ela retorne o valor


def quadrado_de_7():
    return 7 * 7

# Criamos uma variável para receber o retorno da função
ret = quadrado_de_7()

print(f'Retorno: {ret}')
print(f'Retorno: {quadrado_de_7()} ')
    
"""
