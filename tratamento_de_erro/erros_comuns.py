"""
Documentação: Erros Comuns em Python

Introdução

É crucial conhecer esses erros, pois são frequentes no dia a dia, especialmente para iniciantes.
Reconhecê-los rapidamente pode acelerar a resolução de problemas.

Analisando Saídas de Erros

Quando escrevemos código e ocorre um erro, Python gera uma saída de erro que nos ajuda a
identificar o problema.

Exemplos Práticos

Exemplo de Saída de Erro

printF("Olá, Mundo!")

Saída:

NameError: name 'printF' is not defined

O erro NameError indica que o nome printF não está definido. Corrigindo para print("Olá, Mundo!")
resolve o problema.

Erros Mais Comuns em Python

1. SyntaxError

Ocorre quando o Python encontra um erro de sintaxe.

Exemplos:

Definição de função sem parênteses:

def minha_funcao:
    pass

Saída:

SyntaxError: invalid syntax

Utilização de palavra reservada:

None = 1

Saída:

SyntaxError: cannot assign to None

2. NameError

Ocorre quando uma variável ou função não foi definida.

Exemplos:

Variável não definida:

print(variavel_nao_definida)

Saída:

NameError: name 'variavel_nao_definida' is not defined

Função não definida:

funcao_inexistente()

Saída:

NameError: name 'funcao_inexistente' is not defined

3. TypeError

Ocorre quando uma operação ou função é aplicada a um objeto de tipo inadequado.

Exemplos:

Concatenação inválida:

print("string" + 5)

Saída:

TypeError: can only concatenate str (not "int") to str

4. IndexError

Ocorre quando tentamos acessar um elemento de uma lista ou string com um índice inválido.

Exemplos:

Índice fora do alcance:

lista = [1, 2, 3]
print(lista[5])

Saída:

IndexError: list index out of range

5. ValueError

Ocorre quando uma função recebe um argumento do tipo correto, mas com valor inadequado.

Exemplos:

Conversão de string inválida:

int("abc")

Saída:

ValueError: invalid literal for int() with base 10: 'abc'

6. KeyError

Ocorre quando tentamos acessar uma chave que não existe em um dicionário.

Exemplos:

Chave inexistente:

dicionario = {"chave": "valor"}
print(dicionario["outra_chave"])

Saída:

KeyError: 'outra_chave'

7. AttributeError

Ocorre quando uma variável não possui um atributo ou função que estamos tentando acessar.

Exemplos:

Método inexistente em uma tupla:

tupla = (1, 2, 3)
tupla.sort()

Saída:

AttributeError: 'tuple' object has no attribute 'sort'

8. IndentationError

Ocorre quando a indentação do código não é respeitada.

Exemplos:

Indentação incorreta:

def minha_funcao():
print("Erro de indentação")

Saída:

def minha_funcao():
print("Erro de indentação")

Saída:

IndentationError: expected an indented block

Importância de Ler e Prestar Atenção nas Saídas de Erros

É fundamental ler e entender as saídas de erros para resolver problemas de forma eficaz.

Observações Finais

* Exceções e Erros: Na programação, exceções e erros são sinônimos.

* Referência de Erros: Consulte a documentação oficial do Python para uma lista completa de erros.

Estudem e pratiquem a leitura das saídas de erro para melhorar suas habilidades de debug em Python.
"""
