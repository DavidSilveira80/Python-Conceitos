""""
Listas aninhadas (Nested Lists)

- Algumas linguagens de programação (C/Java) possuem uma estrutura de dados chamadas arrays:
    - Unidimensionais (Arrays/vetores);
    - multidimensionais (Matrizes);

Em Python nós temos as listas

numeros = [1, 2, 3, 4, 'b', 3.34, True, 5]
"""

# Exemplos

listas = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]  # Matriz 3 X 3

print(listas)
print(type(listas))

# Como fazemos para acessar os dados?

print(listas[0])
print(listas[0][1])  # 2
print(listas[2][1])  # 8
print()
# Iterando com loops em uma lista aninhada

for lista in listas:
    for numero in lista:
        print(numero)

# List Comprehension

[[print(valor) for valor in lista] for lista in listas]