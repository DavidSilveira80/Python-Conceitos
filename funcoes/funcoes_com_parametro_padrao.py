"""
Funções com parâmetro padrão (Default Paramters)

- Funções onde a passagem de parâmetro seja opcional;

# Exemplo de função onde a passagem de parâmetro seja opcional

print('Hello World')
print()

# Exemplo de função onde a passagem de parâmetro seja obrigatória

def quadrado(numero):
    return numero ** 2

print(quadrado(3))
print(quadrado()) # TypeError

def exponencial(numero, potencia=2):
    return numero ** potencia


print(exponencial(2, 3))  # 2 * 2 * 2 = 8
print(exponencial(3, 2))  # 3 * 3 = 9

print(exponencial(3)) # Por padrão eleve ao quadrado
print(exponencial(3, 5))  # Eleva á potência informada pelo usuário

# OBS
# Se o usuário passar somente 1 parâmetro, este será atribuido ao parâmetro numero, e será calculado
# o quadrado deste número;
# Se o usuário passar 2 argumentos, o primeiro será atribuido ao parâmetro numero e o segundo ao parâmetro
# potencia. Então será calculada esta potência.

# OBS: Em funções Python, os parâmetros com valores default (padrão) DEVEM sempre estar no final da declaração.

# ERRO!
def test(num=2, potencia):
    return num ** potencia


# Outros exemplos

def soma(num1, num2):
    return num1 + num2

print(soma(3, 4))
print(soma(4))  # TypeError
print(soma())   # TypeError

# Exemplo mais complexo

def mostra_informacao(nome='Geek', instrutor=False):
    if nome == 'Geek' and instrutor:
        return 'Bem-vindo instrutor Geek!'
    elif nome == 'Geek':
        return 'Eu pensei que você era o instrutor'
    return f'Olá {nome}'

print(mostra_informacao())
print(mostra_informacao(instrutor=True))
print(mostra_informacao('Ozzy'))
print(mostra_informacao(nome='Stephany'))

# Por quê utilizar parâmetros com valor default?

- Nos permite ser mais flexíveis nas funções;
- Evita erros com parâmetros incorretos;
- Nos permite trabalhar com exemplos mais legíveis de código;

# Quais os tipos de dados podemos utlizar como valores default para parâmetros?

- Qualquer tipo de dado:
    - Números, strings, floats, booleanos, listas, tuplas, dicionários, funções e etc;

# Exemplos


def soma(num1, num2):
    return num1 + num2


def mat(num1, num2, fun=soma):
    return fun(num1, num2)


def subtracao(num1, num2):
    return num1 - num2


print(mat(2, 3))
print(mat(2, 2, subtracao))

# Escopo - Evitar problemas e confusões...

# Variáveis globais
# Variáveis locais

intrutor = 'Geek' # Variável global


def diz_oi():
    instrutor = 'Python'  # variável local
    return f'Oi {instrutor}'


print(diz_oi())

# OBS: Se tivermos uma variável local com o mesmo nome de uma variável global, a local terá preferência.


def diz_oi():
    prof = 'Geek'  # variável local
    return f'Olá {prof}'


print(diz_oi())

print(prof)  # NameError

# ATENÇÃO com variáveis globais (SE puder evitar, evite!)

total = 0

def incrementa():
    total += 1   # UnboundLocalError ( A Variável local está sendo utilizada para processamento sem ter sido inicializada)
    return total

# Como resolver:
def incrementa():
    global total  # Avisando que queremos utilizar a variável global
    total += 1
    return total

print(incrementa())
"""