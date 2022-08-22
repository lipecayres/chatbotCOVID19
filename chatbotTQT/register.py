import menu

def register ():
    print()
    print("Você foi informado na unidade que poderia obter comigo o resultado dos seus exames, certo? ")
    print("Aqui você pode receber o seu laudo do teste sem sair de casa")
    print("Pra isso vou precisar que você digite o seu CPF e sua senha")
    print()
    print("Seu login e senha estão no seu termo de assentimento com a participação no projeto!")
    print()
    
    print("Digite o seu cpf (só numeros):")

    while True:
        cpf = menu.intEntry()
        if len(cpf) == 11:
            break
        else:
            print("CPF inválido. Tente novamente.")
    
    while True:
        key = input("Senha: ")
        if len(key) >= 6:
            break
        else:
            print("Senha inválida. Minímo de 6 dígitos.")

    print("Legal. Agora você pode conferir o seu laudo digital!")
    print()
    print("Acesse este link que você poderá verificar os seus resultados:")
    print()
    print("https://tqtcovid.com/m03_prontuario_individual/")
    print()
    menu.endChat()