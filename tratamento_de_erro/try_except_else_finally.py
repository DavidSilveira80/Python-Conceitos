"""
Revisão Rápida
Já aprendemos como tratar e capturar erros que podem ocorrer em nossas aplicações.
O processo de tratamento de erros eleva a qualidade das aplicações que desenvolvemos.

Quando Tratar um Erro?
Você pode estar se perguntando como saber quando tratar um erro. A dica principal é:

* Toda entrada do usuário deve ser tratada.

Usuários podem destruir seu sistema com entradas inesperadas. Vamos ver isso na prática.

Exemplo Prático

num = int(input("Informe um número: "))
print(f"Você digitou {num}")

Ao executar este código, se o usuário digitar algo que não pode ser convertido para um inteiro, o
correrá um erro. Para tratar isso, usamos try e except:

try:
    num = int(input("Informe um número: "))
    print(f"Você digitou {num}")
except ValueError:
    print("Valor incorreto, informe um número.")

Exemplo com Variável Local

num = 0
try:
    num = int(input("Informe um número: "))
except ValueError:
    print("Valor incorreto.")
print(f"Você digitou {num}")

Blocos else e finally

O bloco else é executado apenas se não ocorrer um erro no bloco try. Já o finally é executado
sempre, independentemente de ter ocorrido um erro ou não.

try:
    num = int(input("Informe um número: "))
except ValueError:
    print("Valor incorreto.")
else:
    print(f"Você digitou {num}")
finally:
    print("Execução finalizada.")

Uso do finally

O finally é comumente usado para liberar recursos, como fechar arquivos ou conexões de
banco de dados.

Exemplo Complexo de Tratamento de Erros

Criar uma função que receba dois valores e retorne a divisão de um pelo outro.

def divide(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Não é possível realizar uma divisão por zero."
    except ValueError:
        return "Valor precisa ser numérico."
    except Exception as e:
        return f"Ocorreu um problema: {e}"

try:
    num1 = int(input("Informe o primeiro número: "))
    num2 = int(input("Informe o segundo número: "))
    print(divide(num1, num2))
except ValueError:
    print("Valor precisa ser numérico.")

Tratamento Genérico e Semi-Genérico
Tratamento genérico captura todos os erros, mas não especifica a causa:

try:
    num1 = int(input("Informe o primeiro número: "))
    num2 = int(input("Informe o segundo número: "))
    print(divide(num1, num2))
except Exception as e:
    print(f"Ocorreu um problema: {e}")

Tratamento semi-genérico:

def divide(a, b):
    try:
        return a / b
    except (ZeroDivisionError, ValueError) as e:
        return f"Ocorreu um problema: {e}"

try:
    num1 = int(input("Informe o primeiro número: "))
    num2 = int(input("Informe o segundo número: "))
    print(divide(num1, num2))
except (ValueError, TypeError) as e:
    print(f"Ocorreu um problema: {e}")

Conclusão
Tratamento de erros é essencial para a robustez do seu código. Pratique com
diferentes cenários e erros para melhorar suas habilidades. Refaça os exemplos, teste.
"""
