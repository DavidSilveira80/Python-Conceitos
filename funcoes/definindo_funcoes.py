"""
Definindo Funções

- Funçoes são pequenas partes de código que realizam tarefas específicas;
- Pode ou não receber entradas de dados e retornar uma saída de dados;
- muito uteis para executar procedimentos similares por por repetidas vezes;

OBS: Se você escrever uma função que realiza várias tarefas dentro dela
é bom fazer uma verificação para que a função seja simplificada.

Já utlizamos várias funções:
- print()
- len()
- max()
- min()
- count()
- e muitas outras;

"""

# Exemplo de utlização de funções:

# cores = ['verde', 'amarelo', 'azul', 'branco']
# curso = 'Programação em Python: Essencial'
# print(cores)
# print(curso)
# cores.append('roxo')
# print(cores)
# curso.append('Mais dados...') # AttributeError

# Mas então como definir funções?

"""
Em Python, a forma de definir uma função é:

def nome_da_funcao(parametros_de_entrada):
    bloco_da_funcao
    
Onde:

nome_da_funcao -> SEMPRE, com letras minúsculas, e se for nome composto, separado por underline _
(Snake Case);
parametros_de_entrada -> Opcionais, omde tendo mais de um, cada um separado por vírgula, podendo
ser opcionais ou não;
bloco_da_funcao -> Também chamado de corpo da função ou implementação, é onde o processamento da função acontece.
Neste bloco, pode ter ou não retorno da função.

OBS: Veja que para definir uma função, utlizamos a palavra reservada 'def' informando ao Python que estamos
definindo uma função. Também abrimos o bloco de código com o já conhecido dois pontos : que é utlizado em Python
para definir blocos.
"""

# Definindo a primeira função

# Definição
def diz_oi():
    print('oi')

"""
OBS:

1 - Veja que, dentro de nossas funções podemos utlizar outras funções;
2 - Veja que nossa função só executa 1 tarefa, ou seja, a única coisa que ela faz é dizer oi;
3 - Veja que esta função não recebe nenhum parâmetro de entrada;
4 - Veja que esta função não retorna nada;
"""

# Utlizando funções

# chamada de execução
# diz_oi()

"""
ATENÇÂO:

Nunca esqueça de usar o parênteses ao excutar uma função

# Exemplo:

# Errado!
diz_oi
diz_oi ()

# Certo!
diz_oi()
"""