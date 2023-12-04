def comer(comendo):
    if comendo:
        resp = 'Estou comendo'
    else:
        resp = 'Não estou comendo'
    return resp


def dormindo_acordado(horas):
    saida = ''
    if horas >= 23 or horas <= 7:
        saida = 'Estou dormindo'
    elif 22 >= horas > 7:
        saida = 'Estou acordado'
    return saida
