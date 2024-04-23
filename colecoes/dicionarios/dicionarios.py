"""
Dicionários

OBS: Em alguma linguagens de programação, os dicionários Python são conhecidos por mapas.

Dicionários são coleções do tipo chave/valor.

Dicionários são representados por chaves {}.

print(type({}))

OBS: Sobre dicionários
    - Chave e valor são separados por dois pontos 'chave:valor';
    - Tanto chave quanto valor podem ser de qualquer tipo de dado;
    - Podemos misturar tipos de dados;

# Criação de dicionários

# Forma 1 (mais comum)

paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

print(paises)
print(type(paises))

# Forma 2 (menos comum)

paises = dict(br='Brasil', eua='Estados Unidos', py='Paraguai')

print(paises)
print(type(paises))

paises = {'br': 'Brasil', 'eua': 'Estados Unidos', 'py': 'Paraguai'}

# Acessando elementos

# Forma 1 - Acessando via chave, da mesma forma que lista/tupla

print(paises['br'])
print(paises['py'])

# print(paises['ru']

# OBS: Caso tentamos fazer um acesso utilizando uma chave que não existe, teremos o erro KeyError.

# Forma 2- Acessando via get - Recomendada

print(paises.get('br'))
print(paises.get('ru'))  # Não dá erro retorna None


# Caso o get não encontre o  objeto com a chave informada será retornado o valor None e não será gerado KeyError

pais = paises.get('py')

if pais:
    print('Encontrei o país.')
else:
    print('Não encontrei o país.')

# Podemos definir um valor padrão para caso não encontremos o objeto com a chave informada

pais = paises.get('ru', 'Não encontrado')
print(pais)

# Podemos verificar se determinada chave se encontra em um dicionário

print('br' in paises)
print('ru' in paises)
print('Estados Unidos' in paises)

# Podemos utilizar qualquer tipo de dado (int, float, string, boolean), inclusive lista, tupla, dicionário,
# como chaves de dicionários.

# Tuplas por exemplo são bastante interessantes de serem utilizadas como chave de dicionário, pois as mesmas
# são imutáveis.
localidades = {
    (35.6895, 39.6917): 'Escritório em Tókio',
    (40.7128, 74.0060): 'Escritório em Nova York',
    (37.7749, 122.4194): 'Escritório em São Paulo',
}

print(localidades)
print(type(localidades))

print(localidades[35.6895, 39.6917])  # retorna Escritório em Tókio

# Adicionar elementos em dicionário

receita_financeira = {'jan': 100, 'fev': 120, 'mar': 300}

print(receita_financeira)
print(type(receita_financeira))

# forma 1 - Mais comum

receita_financeira['abr'] = 350
print(receita_financeira)

# Forma 2

novo_dado = {'mai': 500}

receita_financeira.update(novo_dado) # receita.update({'mai': 500})

print(receita_financeira)

# Atualizando dados em um dicionário

# Forma 1

receita_financeira['mai'] = 550

print(receita_financeira)

# Forma 2

receita_financeira.update({'mai': 600})

print(receita_financeira)

# CONCLUSÃO 1: A forma de adicionar novos elementos ou atualizar dados em um dicionário é a mesma.
# CONCLUSÃO 2: Em dicionários, NÃO podemos ter chaves repetidas

# Remover dados de um dicionário

# Forma 1 - Mais comum

ret = receita_financeira.pop('mar')
print(ret)
print(receita_financeira)

# OBS 1: Aqui precisamos sempre informar a chave, e caso não encontre o elemento, um KeyError é retornado
# OBS 2: Ao removermos um objeto com pop, o valor deste objeto é sempre retornado.

# Forma 2

print(receita_financeira)
del receita_financeira['fev']
print(receita_financeira)

# Se a chave não existir será gerado um KeyError
# OBS: Neste caso o valor removido não é retornado

"""

# Imagine que você tem um comércio eletrônico, onde temos um carrinho de compras na qual adicionamos produtos.

"""
Carrinho de compras: 
   Produto 1:
      - nome;
      - quantidade;
      - preço;
   Produto 2:
      - nome;
      - quantidade;
      - preço; 

# 1 - Poderíamos utilizar uma Lista para isso? Sim

carrinho = []

produto1 = ['playstation 4', 1, 2300.00]
produto2 = ['God of War 4', 1, 150.00]

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# Teríamos que saber qual é o índice de cada informação no produto

# 2 - Poderíamos utilizar uma tupla para isso? Sim

produto1 = ('Playstation 4', 1, 2300.00)
produto2 = ('god of War 4', 1, 150.00)

carrinho = (produto1, produto2)

print(carrinho)

# Teríamos que saber qual é o índice de cada informação no produto

# 3- Poderiamos utilizar um dicionário para isso? Sim

carrinho = []

produto1 = {'nome': 'Playstation 4', 'quantidade': 1, 'preco': 2300.00}
produto2 = {'nome': 'God of War 4', 'quantidade': 1, 'preco': 150.00}

carrinho.append(produto1)
carrinho.append(produto2)

print(carrinho)

# Desta forma, facilmente adicionamos ou removemos produtos no carrinho e em cada produto podemos ter a certeza
# sobre cada informação.

# Métodos de dicionários

d = dict(a=1, b=2, c=3)

print(d)
print(type(d))

# Limpar o dicionário (Zerar dados)
d.clear()
print(d)

# Copiando um dicionário para outro

# Forma 1 Deep Copy

d2 = {'a': 1, 'b': 2, 'c': 3}
novo = d2.copy()  # Deep Copy
novo['d'] = 4

print(d2)
print(novo)
print(type(novo))

# Forma 2 Shallow Copy

novo2 = d

print(novo2)

novo2['d'] = 4
print(d)
print(novo2)

# Forma não usual de criação de dicionários

outro = {}.fromkeys('a', 'b')

print(outro)
print(type(outro))

usuario = {}.fromkeys(['nome', 'pontos', 'email', 'profile'], 'desconhecido')
print(usuario)
print(type(usuario))

# OBS: O método fromkeys recebe dois parâmetros: um iterável e um valor.
# Ele vai gerar para cada valor do iterável uma chave e irá atribuir a esta chave o valor informado.

veja = {}.fromkeys('teste', 'valor')
print(veja)

veja = {}.fromkeys(range(1, 11), 'novo')
print(veja)
"""
