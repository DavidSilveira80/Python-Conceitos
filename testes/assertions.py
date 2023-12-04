"""
Assertions (Afirmações/checagens/questionamentos)

Em Python utilizamos a palavra 'assert' para realizar simples afirmações utilizadas nos testes.

utilizamos o 'assert' em uma expressão que queremos checar se é válida ou não.
Se a expressão for verdadeira, retorna None e caso seja falsa levanta um erro do tipo AssertionError.

# OBS: Nós podemos especificar, opcionalmente, um segundo argumento ou mesmo uma mensagem de erro personalizada

# OBS: A palavra 'assert' pode ser utilizada em qualquer função ou código nosso... naõ precisa ser exclusivamente
nos testes.

# ALERTA: Cuidado ao utilizar 'assert'

Se um programa Python for executado com o parâmetro -O, nenhum assertion será validado. Ou seja, todas as
validações já eram.
"""
assert 4 == 4
# assert 4 == 2, '4 não é igual a 2'


def soma_numeros_positivos(a, b):
    assert a > 0 and b > 0, 'Ambos precisam ser positivos'
    return a + b


ret = soma_numeros_positivos(2, 4)  # 6
print(ret)

# ret = soma_numeros_positivos(-4, 5) # AssertionError


def comer_fast_food(comida):
    assert comida in [
        'pizza',
        'sorvete',
        'doces',
        'batata frita',
        'cachorro quente',
    ], 'A comida precisa ser fast food'
    return f'Eu estou comendo {comida}'


print(comer_fast_food('sorvete'))
# print(comer_fast_food('sopa'))
