"""
Documentação do Operador Ternário em Python

Introdução

Neste documento, vamos explorar o operador ternário em Python. O operador ternário é uma forma
concisa de escrever expressões condicionais em uma única linha. Ele é frequentemente usado quando
você precisa atribuir um valor a uma variável com base em uma condição.

Sintaxe
A sintaxe do operador ternário em Python é a seguinte:

resultado = expressão1 if condição else expressão2

* expressão1: valor retornado se a condição for verdadeira.

* condição: a condição a ser avaliada. Se for verdadeira, expressão1 será avaliada e seu
valor será retornado. Caso contrário, expressão2 será avaliada.

* expressão2: valor retornado se a condição for falsa.

Funcionamento

O Python avalia a condição primeiro. Se for verdadeira, a expressão1 é avaliada e seu valor
é retornado como resultado da expressão ternária. Se a condição for falsa, a expressão2 é
avaliada e seu valor é retornado.

Por exemplo, considerando o seguinte código:

resultado = expressão1 if condição else expressão2

Se condição for verdadeira, resultado será igual ao valor de expressão1. Caso contrário,
será igual ao valor de expressão2.

Exemplos de Uso

1 - Atribuindo o resultado da expressão ternária a uma variável:

idade = 20
maioridade = "Maior de idade" if idade >= 18 else "Menor de idade"
print(maioridade)  # Saída: "Maior de idade"

2 - Chamando funções com base em uma condição:

temperatura = 25
acao = enviar_email() if temperatura > 30 else abrir_janela()

3 - Utilizando o resultado da expressão ternária em uma função:

quantidade = 10
status = "Em estoque" if quantidade > 0 else "Sem estoque"
print(status)  # Saída: "Em estoque"

Considerações Finais

O operador ternário é uma ferramenta útil para escrever código mais conciso e legível em Python.
Ele permite que você tome decisões com base em condições de forma rápida e eficiente,
economizando espaço e melhorando a clareza do seu código.
"""

numero = 13

par_ou_impar = 'PAR' if numero % 2 == 0 else 'Ímpar'

print(par_ou_impar)
