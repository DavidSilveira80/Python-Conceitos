nome_arquivo = "teste.txt"
f= open(f"/home/david-rockman/PycharmProjects/Python-Conceitos/arquivos/{nome_arquivo}", "w")

"""
 r - read - Leitura
 a - append - Anexar
 w - write - Escrita
 x - create - Criar
 t - texto
 b - binário
"""

f.write("Curso Python\n")
f.write("Manipulação de arquivos.")

f.close()
