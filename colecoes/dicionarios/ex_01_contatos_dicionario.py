lista_contatos = []


def adicionar_contato(contatos):
    contato = {}
    nome_contato = input('Entre com o nome do contato: ')
    telefone_contato = input('Entre com o Telefone do Contato: ')
    email_contato = input('Entra com o email do Contato: ')
    contato['nome'] = nome_contato
    contato['telefone'] = telefone_contato
    contato['email'] = email_contato
    lista_contatos.append(contato)


def listar_contatos(contatos):
    for contato in contatos:
        print(f"Nome: {contato.get('nome')} Telefone: {contato.get('telefone')} Email: {contato.get('email')}")


def buscar_contato(contatos):
    resp = ''
    nome_contato = input('Informe o nome do contato: ')
    for contato in contatos:
        if contato.get('nome') == nome_contato:
            resp = contato
            break
    return resp


def remover_contato(contatos):
    contato = buscar_contato(contatos)
    contatos.remove(contato)


while True:
    option = input('1- Adicionar contato 2- Mostrar Contato 3- Buscar contato 4- Remover Contato 5- Sair\n->')
    if option == '1':
        while True:
            print('\nadicionar\n')
            adicionar_contato(lista_contatos)
            adiciona = input('1- Continuar adicionando 2- voltar ao menu\n->')
            if adiciona == '1':
                continue
            else:
                break

    elif option == '2':
        print('\nMostrar Contatos\n')
        listar_contatos(lista_contatos)
    elif option == '3':
        print('\nbuscando Contato')
        contato = buscar_contato(lista_contatos)
        print(contato)
    elif option == '4':
        print('\nRemover Contato\n')
        print('|n Removendo...\n')
        remover_contato(lista_contatos)

    elif option == '5':
        print('Saindo')
        break