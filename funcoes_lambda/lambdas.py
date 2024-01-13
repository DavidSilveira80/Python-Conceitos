# São fuções sem nome, que possuem apenas declaração e retorno.
# Geralmente são atribuidas a variáveis, para que possam ser utilizadas.


bem_vindo = lambda nome: f'Olá {nome}, seja bem-vindo!'

# print(bem_vindo('David'))

# Elas podem ter nenhuma ou muitas entradas

# python = lambda: print('Bem-vindo ao mndo Python!')
# python()

exponenciacao = lambda x, n: print(x ** n)

# exponenciacao(2, 3)

# Usando lambdas em funções

autores = ['Isaac Asimov', 'Carl Sagam', 'Stephen Hawking', 'Clóvis de Baros Filho', 'Arthur C Clarke', 'H. G. Wells']

# print(autores)


# Lambda como retorno de função

def gerar_função_quadratica(a,b,c):
    return lambda x: a*x**2 + b*x + c


funcao_quadratica = gerar_função_quadratica(3,4,5) # definindo o valor de a, b e c

# Definindo o valor de x
print(funcao_quadratica(3))
print(funcao_quadratica(5))
print(funcao_quadratica(0))
