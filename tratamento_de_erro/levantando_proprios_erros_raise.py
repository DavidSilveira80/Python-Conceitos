"""
Lidando com Erros em Python

Introdução


Como tratar e levantar erros em nossos programas. Vamos focar em como lançar nossos próprios
erros utilizando a palavra-chave raise.

Levantando Erros com raise

Vimos diversos erros apresentados pelo Python durante a execução do código. Porém, ainda
não discutimos como lançar nossos próprios erros em situações específicas. Saber como fazer
isso é fundamental para aplicar regras e validações em nossos códigos.

Estrutura Básica

Para lançar um erro, utilizamos a palavra-chave raise seguida pelo tipo de erro e uma mensagem
descritiva. Vamos ver um exemplo básico:

raise ValueError("Mensagem de erro")

Ao executar essa linha, Python interromperá a execução e apresentará a mensagem de erro especificada.

Exemplo Prático
Vamos criar uma função que lança erros customizados:

def colorir(texto, cor):
    # Verificação se o texto é uma string
    if not isinstance(texto, str):
        raise TypeError("O texto precisa ser uma string")

    # Verificação se a cor é uma string
    if not isinstance(cor, str):
        raise TypeError("A cor precisa ser uma string")

    # Lista de cores permitidas
    cores_permitidas = ("verde", "amarelo", "azul", "branco")

    # Verificação se a cor está na lista de cores permitidas
    if cor not in cores_permitidas:
        raise ValueError(f"A cor precisa ser uma entre: {cores_permitidas}")

    # Imprimir o texto na cor especificada (aqui apenas simulamos)
    print(f"O texto '{texto}' será impresso na cor {cor}")

Testando a Função
Vamos testar a função colorir com diferentes entradas:

Teste com valores válidos

colorir("Olá, mundo!", "azul")
# Saída esperada: O texto 'Olá, mundo!' será impresso na cor azul

Teste com tipo incorreto para texto

colorir(123, "azul")
# Saída esperada: TypeError: O texto precisa ser uma string

Teste com tipo incorreto para cor

colorir("Olá, mundo!", 123)
# Saída esperada: TypeError: A cor precisa ser uma string

Teste com cor não permitida

colorir("Olá, mundo!", "vermelho")
# Saída esperada: ValueError: A cor precisa ser uma entre: ('verde', 'amarelo', 'azul', 'branco')

Observações Importantes

1 - Finalização da Função: Ao lançar um erro com raise, a execução da função é interrompida
imediatamente, assim como acontece com o comando return.

2 - Clareza das Mensagens: As mensagens de erro devem ser claras e descritivas, facilitando a
identificação e correção do problema por parte do usuário.

Conclusão

Vimos como lançar nossos próprios erros em Python utilizando a palavra-chave raise. Essa
prática é essencial para garantir que nossas funções recebam entradas válidas e para
comunicar claramente qualquer violação de regras.
"""
