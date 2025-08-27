# desafio final: Agenda para salvar, editar, deletar e marcar um contato com favorito.

def adicionar_contato(nome, telefone, email, contatos):
    contato = {"nome": nome, "telefone": telefone, "email": email, "favorito":False}
    contatos.append(contato)                                                                # função que adiciona um novo contato.
    print(f"\no contato de: {nome} foi adicionado com sucesso!")
    return

def lista_contatos(contatos):
    print("\nLista de contatos: ")
    # preciso percorrer a lista de contatos para exibi-lá.
    for indice, contato in enumerate (contatos, start=1):        # pegando o indice/endereço e o contato.
        status = "✓" if contato["favorito"] else " "
        nome_contato = contato["nome"]
        telefone_contato = contato["telefone"]
        email_contato = contato["email"]
        print(f"{indice}. [{status}] {nome_contato} - {telefone_contato} - {email_contato}")
    return

def editar_contato(indice, opcao, lista, novo_nome=None, novo_telefone=None, novo_email=None):
    indice_contato = indice - 1 # ajustando a possicão corretamente.
    if indice_contato >= 0 and indice_contato < len(lista): # tratamento de erros!
        if opcao == "1":
            lista[indice_contato] ["nome"] = novo_nome

        elif opcao == "2":
            lista[indice_contato] ["telefone"] = novo_telefone

        elif opcao == "3":
            lista[indice_contato] ["email"] = novo_email

        elif opcao == "4":
            lista[indice_contato] ["nome"] = novo_nome
            lista[indice_contato] ["telefone"] = novo_telefone
            lista[indice_contato] ["email"] = novo_email

    else:
        print("Opção inválida.")
        # tarefas[indice_ajustado] ["tarefa"] = novo_nome_tarefa
    return

def deletar_contato(indice, lista): # deletar através do indice.
    indice_contato = indice - 1 # ajustando a possicão corretamente.
    if indice_contato >= 0 and indice_contato < len(lista): # tratamento de erros, verifica se foi digitado uma opção valida!
        lista.pop(indice_contato)

    else: print("\nTarefa não existente!")
    return

def favorito_contato(contato, lista): # 
    indice_contato = contato - 1
    if lista[indice_contato] ["favorito"] == True:
        lista[indice_contato] ["favorito"] = False # Marca a função como favorita.

    else: lista[indice_contato] ["favorito"] = True
    return

def contatos_favoritos(lista):

    for indice, contato in enumerate (lista, start=1):        # pegando o indice/endereço e o contato.
        if contato["favorito"] == True:
            status = "✓"
            nome_contato = contato["nome"]
            telefone_contato = contato["telefone"]
            email_contato = contato["email"]
            print(f"{indice}. [{status}] {nome_contato} - {telefone_contato} - {email_contato}")
        
        else: " "
    return

lista = [] # lista que será responsavél por salver os contatos.

# Iniciando a construção do Menu.
while True:
    print("\nMenu da Agenda de contatos.")
    print("1. Salvar novo contato")
    print("2. Apresentar lista de contatos")
    print("3. Editar contato")
    print("4. Deletar contato") 
    print("5. Marcar/desmarcar contato como favorito")
    print("6. Apresentar lista de contatos favoritos")
    print("7. Sair")

    escolha = input("Digite a opção desejada: ")

    if escolha == "1":
        contato_nome = input("Digite o nome do contato a ser salvo: ")
        contato_telefone = input("Digite o telefone do contato a ser salvo: ")
        contato_email = input("Digite o E-mail do contato a ser salvo: ")
        adicionar_contato(contato_nome, contato_telefone, contato_email, lista)

    elif escolha == "2":
        lista_contatos(lista)

    elif escolha =="3":
        lista_contatos(lista)
        editar_contatos = int(input("\nDigite o indice do contato a ser atualizado: "))
        opcao_contato = input("o que você quer editar ? \n 1. Nome \n 2. Telefone \n 3. E-mail \n 4. Todos \n")
        if opcao_contato == "1":
            novo_nome = input("Digite o novo nome: ")
            editar_contato(editar_contatos, opcao_contato, lista, novo_nome=novo_nome)

        elif opcao_contato == "2":
            novo_telefone = input("Digite o novo Telefone: ")
            editar_contato(editar_contatos, opcao_contato, lista, novo_telefone=novo_telefone)

        elif opcao_contato == "3":
            novo_email = input("Digite o novo E-mail: ")
            editar_contato(editar_contatos, opcao_contato, lista, novo_email=novo_email)

        elif opcao_contato == "4":
            novo_nome = input("Digite o novo nome: ")
            novo_telefone = input("Digite o novo Telefone: ")
            novo_email = input("Digite o novo E-mail: ")
            editar_contato(editar_contatos, opcao_contato, lista, novo_nome, novo_telefone, novo_email)
        

    elif escolha == "4":
        # deletar contato...
        lista_contatos(lista)
        contato_deletar = int(input("Digite o indice do contato a ser deletado: "))
        deletar_contato(contato_deletar, lista)
        lista_contatos(lista)

    elif escolha == "5":
        # marcar contato como favorito...
        lista_contatos(lista)
        contato_favorito = int(input("Digite o contato a ser adicionado/removido dos favoritos: "))
        favorito_contato(contato_favorito, lista)
        lista_contatos(lista)

    elif escolha == "6":
        contatos_favoritos(lista)

    elif escolha == "7":
        break

print("\nPrograma finalizado")