"""
List Comprehension

- Utilizando List Comprehensions nós podemos gerar novas listas com dados processados a partir de outro iterável

# sintaxe da List Comprehension

[ dado for dado in iterável ]

"""

"""
# Exemplos

numeros = [1, 2, 3, 4, 5]

res = [numero * 10 for numero in numeros]
print(res)


def multiplicar(valor):
    return valor * valor


result = [multiplicar(numero) for numero in numeros]

print(result)
Para melhor entermos o que esta acontecendo devemos divir a expressão em duas partes

- A primeira parte: for numero in numeros
- A segunda parte: numero * 10

# List Comprehension VS Loop

#Loop
numeros = [1, 2, 3, 4, 5]
numeros_dobrados = []
for numero in numeros:
    numero_dobrado = numero * 2
    numeros_dobrados.append(numero_dobrado)
print(numeros_dobrados)

# List Comprehension
print([numero * 2 for numero in numeros])

"""

# Outros exemplos

# 1
nome = 'Geek University'

print([letra.upper() for letra in nome])

# 2

amigos = ['maria', 'julia', 'pedro', 'guilherme']

# Primeira Letra maiúscula
print([amigo.capitalize() for amigo in amigos])

# Nome em maiúsculo
print([amigo.upper() for amigo in amigos])

# 3

print([numero * 3 for numero in range(1, 10)])

# 4

print([bool(valor) for valor in [0, [], '', True, ', 1,  3.14']])

# 5

print([str(numero) for numero in [1, 2, 3, 4, 5, True]])