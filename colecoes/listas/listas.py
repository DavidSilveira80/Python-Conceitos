"""
Listas
-----

Listas em Python funcionam como vetores/matrizes (arrays) em outras linguagens, com a diferença de serem
dinâmicas e também de podermos colocar QUALQUER tipo de dado.

Linguagens C/Java
- Possuem tamanho e tipo de dado fixo;
   ou seja, nestas linguagens se você criar um array do tipo int e com tamanho 5, este array será SEMPRE
   do tipo inteiro de poderá ter SEMPRE no máximo 5 valores.

Já em Python:
- Dinâmico: Não possuem tamanho fixo, ou seja, podemos criar a lista e simplesmente ir adicionando alementos;
- Qaulquer tipo de dado: Nã possuem tipo de dado fixo, ou seja, podemos colocar qualquer tipo de Dado.

As listas em Python são represantados por colchetes []

type([])  # Mostra que é tipo list

lista1 = [1, 99, 4, 27, 15, 22, 3, 1, 44, 42, 27]

lista2 = ['G', 'e', 'e', 'k', ' ', 'U', 'n', 'i', 'v', 'e', 'r', 's', 'i', 't', 'y']

lista3 = []

lista4 = list(range(11))

lista5 = list('Geek University')

# Podemos facilmente checar se determinado valor está contido na lista

if 8 in lista4:
    print('Encontrei o número 8')
else:
    print('Não encontrei o número 8')

# Podemos facilmente ordenar uma lista

lista1.sort()
print(lista1)

#  Podemos facilmente contar o número de ocorrências de um valor em uma lista

print(lista1.count(1))
print(lista5.count('e'))

# Adicionar elementos em listas

# Para adicionar elementos em listass, utlizamos a função append
# OBS: Com append, nós só conseguimos adicionar um elemento por vez
# lista1.append(12, 34, 56) # erro
print(lista1)
lista1.append(42)
print(lista1)

lista1.append([8, 3, 1]) # Coloca a lista como elemento único (sublista)
print(lista1)

lista1.extend([123, 44, 67])  # Coloca cada elemento da lista como valor adicional á lista
print(lista1)

# Podemos inserir um novo elemento na lista informando a posição do índice
# OBS: Issa não substitui o valor inicial. O mesmo será deslocado para direita da lista.
lista1.insert(2, 'Novo Valor')
print(lista1)

# Podemos facilmente juntar duas listas

lista6 = lista1 + lista2
print(lista6)

# Podemos facilmente inverter uma lista
print(lista1)
print(lista2)

lista1.reverse() # lista1[::-1]
lista2.reverse() # lista2[::-1]

print(lista1)
print(lista2)

# Copiar uma lista

lista6 = lista2.copy()
print(lista6)

# Podemos contar quantos elementos existem dentro da lista
print(len(lista5))

# Podemos facilmente remover o último elemento de uma lista
# OBS: o pop não somente remove o último elemento mas também o retorna
print(lista5)
lista5.pop()
print(lista5)

# podemos remover um elemento pelo índice
# OBS: Os lementos a direita deste índice serão deslocados para a esquerda
# OBS: Se não houver elemento no índice informado, teremos o erro IndexError
lista5.pop(2)
print(lista5)

# podemos remover todos os elementos
print(lista5)
lista5.clear()
print(lista5)

# Podemos facilmente converter uma String para uma lista

# Exemplo 1
curso = 'Programação em Python: Essencial'
print(curso)
curso = curso.split()
# OBS: Por padrão, o split separa os elementos da lista pelo espaço entre eles.
print(curso)

# Exemplo2

curso = 'Programação,em,Python:,Essencial'
print(curso)
curso = curso.split(',') # Separador ,
print(curso)

# Convertendo uma lista em uma String

lista6 = ['Programação', 'em', 'Python:', 'Essencial']
print(lista6)

# OBS: Abaixo estamos falando: Pega a lista6, coloca espaço entre cada elemento e transforma em uma String.
curso = ' '.join(lista6)
print(curso)

# Iterando sobre listas

for elemento in lista1:
    print(elemento)

# Fazemos acesso aos elementos de forma indexada

#          0          1         2       3
cores = ['verde', 'amarelo', 'azul', 'branco']

print(cores[0])  # verde
print(cores[1])  # amarelo
print(cores[2])  # azul
print(cores[3])  # branco

# Podemos fazer acesso aos elementos de forma indexada inversa

print(cores[-1])  # branco
print(cores[-2])  # azul
print(cores[-3])  # amarelo
print(cores[-4])  # verde
# print(cores[-5]) # Erro, pois não existe índice -5 nesta lista.

# Desenpacotamento de listas

lista = [1, 2, 3]

num1, num2, num3 = lista
print(num1)
print(num2)
print(num3)

# OBS: Se tivermos um número diferente de elementos na lista ou variáveis para receber dados, teremos valueError

# Copiando uma lista para outra (Shallow Copy e Deep Copy)

# Forma 1 - Deep Copy
lista = [1, 2, 3]
print(lista)

nova = lista.copy()  # Cópia

print(nova)
nova.append(4)

print(lista)
print(nova)

# Veja que ao utilizarmos lista.copy() copiamos os dados da lista para uma nova lista, mas elas ficaram totalmente
# independentes ou seja, modificando uma lista, não afeta a outra. Isso em Python é chamado de Deep Copy.

# Forma 2 - Shallow Copy

lista = [1, 2, 3]
print(lista)

nova = lista  # Cópia
print(nova)

nova.append(4)

print(lista)
print(nova)

# Veja que utilizamos a cópia via atribuição e copiamos os dados da lista para a nova listas, mas após realizar
# modificação em uma das listas, essa modificação se refletiu em ambas as listas. Isso em Python é chamado de
# Shallow Copy.
"""



