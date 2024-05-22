"""
Conjuntos
- Conjuntos em qualquer linguagem de programação, estamos fazendo referência á Teoria dos Conjuntos
da Matemática.

- Aqui no Python, os conjuntos são chamados de Sets.

Dito isto, da mesma forma que na Matemática:
- Sets (Conjuntos) não possuem valores duplicados;
- Sets (Conjuntos) não possuem valores ordenados;
- Elementos não são acessados via índice, ou seja, conjuntos não são indexados;

Conjuntos são bons para se utilizar quando precisamos armazenar elementos
mas não nos importamos com a ordenação deles. Quando não precisamos se preocupar
com chaves, valores e itens duplicados.

Os Conjuntos (Sets) são referenciados em Python com chaves {}

Diferença entre Conjuntos (Sets) e Mapas (Dicionários) em Python:
    - Um Dicionário tem chave/valor
    - Um conjunto tem apenas valor;

# Definindo um Conjunto

# Forma 1

s = set({1, 2, 3, 4, 5, 5, 6, 7, 2, 3})  # Repare que temos valores repitidos.
print(s)
print(type(s))

# OBS: Ao criar um Conjunto, caso seja adicionado um valor já existente, o mesmo
# será ignorado sem gerar error e não fará parte do conjunto.

# Forma 2 - Mais comum

s = {1, 2, 3, 4, 5, 5}
print(s)
print(type(s))

# Gerando um Set de uma lista
lista = [1, 2, 3, 4, 4, 5, 6, 6]
print(lista)
print(type(lista))
conjunto = set(lista)
print(conjunto)
print(type(conjunto))

# Podemos verificar se determinado elemento está contido no conjunto

if 3 in conjunto:
    print('Tem o 3')
else:
    print('Não tem o 3')

# Importante lembrar que, além de não termos valores duplicados, não temos ordem

# Listas aceitam valores duplicados, então temos 10 elementos
lista = [99, 2, 34, 23, 2, 12, 1, 44, 5, 34]
print(f'Lista: {lista} com {len(lista)} elementos.')

# Tuplas aceitam valores duplicados, então temos 10 elementos
tupla = (99, 2, 34, 23, 2, 12, 1, 44, 5, 34)
print(f'Tupla: {tupla} com {len(tupla)} elementos.')

# Dicionários não aceitam chaves duplicadas, então temos 8 elementos
dicionario = {}.fromkeys([99, 2, 34, 23, 2, 12, 1, 44, 5, 34], 'dict')
print(f'Dicionário: {dicionario} com {len(dicionario)} elementos.')

# Conjuntos não aceitam valores duplicados, então temos 8 elementos
conjunto = {99, 2, 34, 23, 2, 12, 1, 44, 5, 34}
print(f'Conjunto: {conjunto} com {len(conjunto)} elementos.')

# Assim como todo outro conjunto Python podemos colocar tipos de dados misturados em Sets.

s = {1, 'b', True, 34.22, 44}
print(s)
print(type(s))

# Podemos iterar em um set normalmente

for valor in s:
    print(valor)

   # Usos interessantes com Sets

# Imagine que fizemos um formulário de cadastro de visitantes e muma feira ou museu e os visitantes
# informam manualmente a cidade de onde vieram.

# Nós adicionamos cada cidade em uma lista Python, já que em uma lista podemos adicionar novos elementos
# e ter repetição.

cidades = ['Belo Horizonte', 'São Paulo', 'Campo Grande', 'Cuiba', 'Campo Grande', 'São Paulo', 'Cuiba']
print(cidades)
print(len(cidades))

# Precisamos saber quantas cidades distintas, ou seja, únicas, temos.

# O que você faria? Faria um loop na lista ...?

# Podemos utilizar o set para isso
print(len(set(cidades)))

# Adicionando elementos em um Conjunto

s = {1, 2, 3}

s.add(4)
s.add(4)  # Duplicidade não gera erro. Simplismente é ignorado e não é adicionado.
print(s)

# Remover elementos em um Conjunto
print(s)
# Forma 1
s.remove(3)  # Não é índice! Informamos o valor a ser removido. Nenhum valor é retornado.
print(s)
# s.remove(33)
# OBS: Caso o valor não seja encontrado será gerado um erro KeyError

# Forma 2

s.discard(2)
print(s)
# s.discard(22)
# OBS: Se o valor não for encontrado, nenhum erro é gerado.

s = {1, 2, 3}
print(s)
# Copiando um Conjunto para outro...

# Forma 1 - Deep Copy
# novo = s.copy()
# print(novo)

# novo.add(4)

# print(novo)
# print(s)

# Forma 2 - Shallow copy

novo = s
novo.add(4)
print(novo)
print(s)

# Podemos remover todos os elementos de um conjunto

s.clear()
print(s)

# Métodos Matemáticos de um Conjunto

# Imagine que temos dois Conjuntos; um contendo estudantes do curso Python e um contendo
# estudantes do curso de Java.

estudantes_python = {'Marcos', 'Patricia', 'Ellen', 'Pedro', 'Julia', 'Gilherme'}
estudantes_java = {'Fernando', 'Gustavo', 'Julia', 'Ana', 'Patricia'}

# Veja que alguns alunos que estudam Python também estudam Java.

# Precisamos gerar um conjunto com nomes de estudantes únicos.

# Forma 1 - Utilizando union

unicos1 = estudantes_python.union(estudantes_java)
print(unicos1)

# forma 2 - Utilizando o caractere pipe |
unicos2 = estudantes_python | estudantes_java
print(unicos2)

# Gerar um conjunto de estudantes que estão em ambos os cursos

# Forma 1 - Utilizando intersection

ambos1 = estudantes_python.intersection(estudantes_java)
print(ambos1)

# Forma 2 - Utilizandoo &

ambos2 = estudantes_python & estudantes_java
print(ambos2)

# Gerar um conjunto de estudantes que não estão no outro curso

so_python = estudantes_python.difference(estudantes_java)
print(so_python)

so_java = estudantes_java.difference(estudantes_python)
print(so_java)

# Soma*, valor Máximo*, valor Mínimo, Tamanho

# * Se os valores forem todos inteiros ou reais

s = {1, 2, 3, 4, 5, 6}

print(sum(s))
print(max(s))
print(min(s))
print(len(s))
"""
