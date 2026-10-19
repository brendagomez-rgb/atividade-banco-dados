# Angélica R Muniz Brenda Lisie Gomes
banco = {}
opcao = 0
while opcao != 4:
    print("Banco Chave Valor")
    print("1- Cadastrar")
    print("2- Consultar")
    print("3- Excluir")
    print("4- Sair")

    opcao = int(input("Escolha uma opção:  "))

    if opcao == 1:
        chave = input("Digite a chave:  ")

        if chave in banco:
            print("Essa chave já existe!!")
        else:
            valor = input("Digite o valor:  ")
            banco[chave] = valor
            print("Cadastro realizado!!")

    elif opcao == 2:
        chave = input("Digite a chave que deseja consultar: ")

        if chave in banco:
            print("Valor:", banco[chave])
        else:
            print("Chave não encontrada!")

    elif opcao == 3:
        chave = input("Digite a chave que deseja excluir: ")

        if chave in banco:
            del banco[chave]
            print("Registro excluído!")
        else:
            print("Chave não encontrada!")

    elif opcao == 4:
        print("Programa encerrado!")

    else:
        print("Opção inválida!")
