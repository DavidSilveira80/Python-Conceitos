"""
Funções com Parâmetro (de entrada)

- Funções que recebem dados para serem processados dentro da mesma;

Se a gente pensar  e mum programa qualquer, geralmente temos:

entrada -> processamento -> saída

Se a gente pensar em uma função, já sabemos que temos funções que:
- Não possuem entrada;
- Não possuem saída;
- Possuem entrada mas não possuem saída;
- Não possuem entrada mas possuem saída;
- Possuem entrada e saída;

def quadrado(numero):
    # return numero * numero
    return numero ** 2


print(quadrado(7))
print(quadrado(2))
print(quadrado(5))

# Funções podem ter n parâmetros de entrada. Ou seja, podemos receber como entrada em uma função
# quantos parâmetros forem necessários. Eles são separados por vírgula.

# Exemplo


def soma(a, b):
    return a + b


print(soma(2, 2))

# OBS: Se a gente informar um número errado de parâmetros ou argumentos, teremos TypeError

print(soma(2, 3, 4))  # TypeError - Passando argumentos a mais
print(soma(4))  # TypeError - Passando argumentos a menos

# Nomeando parâmetros


def nome_completo(nome, sobrenome):
    return f'Seu nome é {nome} {sobrenome}'


print(nome_completo('Angelina', 'Jolie'))

# A diferença entre Parâmetros e Argumentos

# Parâmetros são variáveis decladas na definição de uma função;
# Argumentos são dados passados durante a execução de uma função;


# A ordem dos parâmetros importam !

nome = 'Felicity'
sobrenome = 'Jones'

print(nome_completo(sobrenome, nome))

# Argumentos nomeados (Keyword Arguments)

# Caso utilizemos nomes dos parâmetros nos argumentos para informá-los, podemos
# utilizar qualquer ordem.

print(nome_completo(nome='Angelina', sobrenome='Jolie'))
print(nome_completo(nome=nome, sobrenome=sobrenome))
print(nome_completo(sobrenome='Marques', nome='Marcia'))

# Erro comum na utlização do return


def soma_impares(numeros):
    total = 0
    for numero in numeros:
        if numero % 2 != 0:
            total += numero
        return total # erro retornará 1
    return total  # execução correta retornará 16


lista_numeros = [1, 2, 3, 4, 5, 6, 7]

print(soma_impares(lista_numeros))
"""
