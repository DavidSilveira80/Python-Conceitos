"""
Bloco try except

Objetivo

Utilizar o bloco try except para tratar erros que possam ocorrer no código Python.
Isso é especialmente útil para desenvolvedores que vêm de outras linguagens de programação.

Conceitos Importantes

* Erros: Erros fazem parte do desenvolvimento e podem ocorrer em diversas fases.

* Tratamento de Erros: Tratar erros é fundamental para evitar que o programa seja interrompido
abruptamente e para impedir que usuários vejam mensagens de erro inesperadas.

* Bloco try except: Em Python, utilizamos o bloco try except para tentar executar um bloco de
código e, em caso de erro, capturar e tratar a exceção.

Estrutura Básica do try except

A forma mais simples do bloco try except é a seguinte:

try:
    # Código que pode gerar um erro
except:
    # Código a ser executado em caso de erro

Exemplos Práticos

Exemplo 1: Tratando um Erro Genérico

try:
    # Tentativa de executar um código que gera erro
    print(nome)
except:
    # Código a ser executado em caso de erro
    print("Deu um problema")

Neste exemplo, o erro de variável não definida (NameError) é capturado pelo bloco except,
evitando que o programa seja interrompido.

Exemplo 2: Tratando Erros de Forma Específica

try:
    # Tentativa de executar um código que gera um erro específico
    print(nome)
except NameError:
    # Código a ser executado em caso de NameError
    print("Erro: Nome não definido")

Aqui, o bloco except captura especificamente o NameError.

Exemplo 3: Tratando Vários Tipos de Erro

try:
    # Tentativa de execução que pode gerar diferentes tipos de erro
    lista = [1, 2, 3]
    print(lista[5])
except NameError:
    # Tratamento específico para NameError
    print("Erro: Nome não definido")
except IndexError:
    # Tratamento específico para IndexError
    print("Erro: Índice fora do alcance")

Neste exemplo, diferentes tipos de erro são tratados de forma específica, garantindo um
tratamento mais preciso.

Exemplo 4: Usando um Alias para a Exceção

try:
    # Tentativa de execução que pode gerar um erro
    print(10 / 0)
except ZeroDivisionError as e:
    # Tratamento específico para ZeroDivisionError com detalhe do erro
    print(f"A aplicação gerou o seguinte erro: {e}")

Utilizando um alias (as e), podemos capturar a mensagem de erro específica e utilizá-la no tratamento.

Exemplo 5: Tratamento de Erros em Funções

def pega_valor(dicionario, chave):
    try:
        # Tentativa de acessar um valor no dicionário pela chave
        return dicionario[chave]
    except KeyError:
        # Tratamento específico para KeyError
        return "Chave não encontrada"

meu_dicionario = {"nome": "João"}
print(pega_valor(meu_dicionario, "nome"))
print(pega_valor(meu_dicionario, "idade"))

Neste exemplo, a função pega_valor trata a exceção KeyError caso a chave não seja encontrada
no dicionário.

Conclusão

O tratamento de erros é uma prática essencial em desenvolvimento de software para garantir que
aplicações funcionem de maneira robusta e amigável ao usuário. O bloco try except em Python
é uma ferramenta poderosa para implementar essa prática, permitindo capturar e tratar erros d
e maneira eficiente.
"""
