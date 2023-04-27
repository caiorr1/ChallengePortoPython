bancoDeDados = {'Login1': 'Senha1', 'Login2': 'Senha2'}


def main():
    print('*'*28)
    print('SISTEMA ANDROMEDA')
    print('*'*28)
    choice = input(
        'Pressione (1) se deseja fazer o Cadastro.\nPressione (2) se deseja fazer o Login.\nPressione (3) se deseja Sair.\n')
    if choice == '3':
        print('Você saiu da aplicação')
    elif choice == '1':
        cadastro()
    elif choice == '2':
        login()
    else:
        while choice != '1' and choice != '2' and choice != '3':
            print('Não entendi. Tente novamente')


def cadastro():
    print('*'*28)
    print('CADASTRO')
    print('*'*28)
    loginCadastro = input(
        'Olá, aqui você pode adicionar uma nova conta! \nQual o nome de usuário?\n')
    print('-'*30)
    global cpf
    cpf = input('Insira o seu CPF\n')
    print('-'*30)
    global placa
    placa = input('Insira a placa do veículo (Em letras maiusculas)\n')
    while len(placa) != 7:
        print('Placa inválida. Sua placa deve ter 7 caracteres.')
        placa = input('Insira a placa do veículo\n')
    print('-'*30)
    global modelo
    modelo = input('Insira o modelo do veículo (Em letras maiusculas)\n')
    print('-'*30)
    senhaCadastro = input('Qual a senha?\n')
    print('-'*30)
    senhaConfirmacao = input('Confirme a senha\n')

    while senhaConfirmacao != senhaCadastro:
        print('='*25)
        print('Senhas não conferem')
        senhaConfirmacao = input('Confirme a senha\n')
        print('='*25)

    if senhaCadastro == senhaConfirmacao:
        loginUsuario = {loginCadastro: senhaCadastro}
        bancoDeDados.update(loginUsuario)
        # print (bancoDeDados) Lista de Usuários
        print('\nParabéns! Você realizou o seu cadastro!\n')
        main()


def login():
    print('*'*28)
    print('LOGIN')
    print('*'*28)
    login = input(
        'Olá, aqui você pode fazer o login! \nQual o nome de usuário?\n')
    print('-'*30)
    senha = input('Qual a senha?\n')
    for i in bancoDeDados:
        if i == login:
            if senha == bancoDeDados[i]:
                print('-'*38)
                print(f'Olá {login}! Você realizou o seu login!')
                print('-'*38)
                modal()
            else:
                print('-'*20)
                print('Senha Incorreta')
            break
    else:
        print('Usuário Invalido')
        print('-'*20)

# chamando o modal

def modal():
    print('*'*28)
    print('GUINCHO')
    print('*'*28)
    chamarModal = input('Pressione (1) para chamar um Guincho\nPressione (2) para Sair\n')
    # while chamarModal != '1' and chamarModal != '2':
    #     print('\n-----------------------------------')
    #     print('Não entendi, digite novamente.')
    #     print('-------------------------------------')
    #     chamarModal = input('Pressione (1) para chamar um Guincho\nPressione (2) para Sair\n')
    #     break 
    if chamarModal == '2':
        print('-'*40)
        print('Você saiu da aplicação')
        print('-'*40)
        main()
    elif chamarModal == '1':
        print('-'*60)
        descobrindo_caso = input('Presione (1) se foi um acidente de transito\nPressione (2) se foi uma falha operacional\n')
        # while descobrindo_caso != '1' and descobrindo_caso != '2':
        #     print('\n-------------------------------------------------------------------------------')
        #     print('Não entendi, digite novamente.')
        #     print('---------------------------------------------------------------------------------')
        #     descobrindo_caso = input('Presione (1) se foi um acidente de transito\nPressione (2) se foi uma falha operacional\n')
        # caso 1, acidente de transito e veiculo leve
        if descobrindo_caso == '1':
            print('-'*60)
            tipo_veiculo = input('Pressione (1) se o veículo é leve(Peso de até 3,5 toneladas\nPressione (2) se o veículo é pesado(Acima de 3,5 toneladas)\n')
            print('-'*60)
            # while tipo_veiculo != '1' and tipo_veiculo != '2':
            #     print('\n------------------------------')
            #     print('Não entendi, digite novamente.')
            #     print('--------------------------------')
            #     tipo_veiculo = input(
            #     'Pressione (1) se o veículo é leve(Peso de até 3,5 toneladas\nPressione (2) se o veículo é pesado(Acima de 3,5 toneladas)\n')
            #     print('------------------------------------------------------------')
            #     break
            if tipo_veiculo == '1':
                endereco = input('Qual endereco da ocorrência?\n')
                print('-'*35)
                telefone = input('Qual telefone para atendimento?\n')
                print('-'*35)
                print(f'O guincho será enviado para o veiculo comum/leve de placa: {placa}\nProprietário de CPF:{cpf}\nTelefone: {telefone}\nPara o endereco: {endereco}')
                print('-'*22)
                print('ATENDIMENTO ENCERRADO')
                print('-'*22) 
              
        # caso 1.1, acidente de transito e veiculo pesado
            elif descobrindo_caso == '1':
                if tipo_veiculo == '2':
                    endereco_2 = input('Qual endereco da ocorrência?\n')
                    print('-'*35)
                    telefone = input('Qual telefone para atendimento?\n')
                    print('-'*70)
                    print('Para a escolha de guincho ser assertiva, responda algumas perguntas. Se não souber responder, digite 0\n')
                    print('-'*70)
                    tipo_carroceria = input("Digite o tipo de carroceria: ")
                    chassi = input("Seu chassi é alongado?: ")
                    comprimento = input("Qual o comprimento do seu veiculo?: ")
                    peso_com_carga = input("Peso do veiculo com a carga: ")
                    peso_sem_carga = input("Peso do veiculo sem a carga: ")
                    quantidade_eixos = input("Qual a quantidade de eixo: ")
                    informacao_adicional = input('Responda caso seu veiculo tenha alguma alteração, ou você queira adicionar alguma informação sobre. Caso não tenha nenhuma informação a mais, deixe em branco\n')
                    if tipo_carroceria and chassi and comprimento and peso_com_carga and peso_sem_carga and quantidade_eixos == '0':
                        print('-'*100)
                        print('Vamos enviar um atendente de moto para nos auxiliar na escolha do guincho. Obrigado pelo contato!')
                        print('ATENDIMENTO ENCERRADO')
                        print('-'*100)
                    else:
                        print(f'O guincho será enviado para o veículo pesado de placa: {placa}, do proprietário de CPF: {cpf}\nTelefone: {telefone}\nPara o endereco: {endereco_2}')
                        print('-'*22)
                        print('ATENDIMENTO ENCERRADO')
                        print('-'*22)
                        
                        
                    # while tipo_veiculo == '2':
                    #     print('----------------------')
                    #     print('ATENDIMENTO ENCERRADO')
                    #     print('----------------------')
                    #     break   
                else:
                    main()
            else:
                main()
        else:
            main()
        #caso 1.2, falha operacional e veiculo leve
        if descobrindo_caso == '2':
            print('-'*60)
            tipo_veiculo = input('Pressione (1) se o veículo é leve(Peso de até 3,5 toneladas\nPressione (2) se o veículo é pesado(Acima de 3,5 toneladas)\n')
            print('-'*60)
            # while tipo_veiculo != '1' and tipo_veiculo != '2':
            #     print('\n------------------------------')
            #     print('Não entendi, digite novamente.')
            #     print('--------------------------------')
            #     tipo_veiculo = input(
            #     'Pressione (1) se o veículo é leve(Peso de até 3,5 toneladas\nPressione (2) se o veículo é pesado(Acima de 3,5 toneladas)\n')
            #     print('------------------------------------------------------------')
            #     break
            if tipo_veiculo == '1':
                endereco = input('Qual endereco da ocorrência?\n')
                print('-'*35)
                telefone = input('Qual telefone para atendimento?\n')
                print('-'*35)
                print(f'O guincho será enviado para o veiculo comum/leve de placa: {placa}\nProprietário de CPF:{cpf}\nTelefone: {telefone}\nPara o endereco: {endereco}')
                print('-'*22)
                print('ATENDIMENTO ENCERRADO')
                print('-'*22)
            else:
                main()
        else:
            main()
            
        # falha operacional e veiculo pesado
        if descobrindo_caso == '2':
            # while tipo_veiculo != '1' and tipo_veiculo != '2':
            #     print('\n------------------------------')
            #     print('Não entendi, digite novamente.')
            #     print('--------------------------------')
            #     tipo_veiculo = input(
            #     'Pressione (1) se o veículo é leve(Peso de até 3,5 toneladas\nPressione (2) se o veículo é pesado(Acima de 3,5 toneladas)\n')
            #     print('------------------------------------------------------------')
            #     break
            if tipo_veiculo == '2':
                print('-'*35)
                endereco_2 = input('Qual endereco da ocorrência?\n')
                print('-'*35)
                telefone = input('Qual telefone para atendimento?\n')
                print('-'*70)
                print('Para a escolha de guincho ser assertiva, responda algumas perguntas. Se não souber responder, digite 0\n')
                print('-'*70)
                tipo_carroceria = input("Digite o tipo de carroceria: ")
                chassi = input("Seu chassi é alongado?: ")
                comprimento = input("Qual o comprimento do seu veiculo?: ")
                peso_com_carga = input("Peso do veiculo com a carga: ")
                peso_sem_carga = input("Peso do veiculo sem a carga: ")
                quantidade_eixos = input("Qual a quantidade de eixo: ")
                informacao_adicional = input('Responda caso seu veiculo tenha alguma alteração, ou você queira adicionar alguma informação sobre. Caso não tenha nenhuma informação a mais, deixe em branco\n')
                if tipo_carroceria and chassi and comprimento and peso_com_carga and peso_sem_carga and quantidade_eixos == '0':
                    print('-'*100)
                    print('Vamos enviar um atendente de moto para nos auxiliar na escolha do guincho. Obrigado pelo contato!')
                    print('ATENDIMENTO ENCERRADO')
                    print('-'*100)
                else:
                    print(f'O guincho será enviado para o veículo pesado de placa: {placa}, do proprietário de CPF: {cpf}\nTelefone: {telefone}\nPara o endereco: {endereco_2}')
                    print('-'*22)
                    print('ATENDIMENTO ENCERRADO')
                    print('-'*22)
                # while tipo_veiculo == '2':
                #     print('----------------------')
                #     print('ATENDIMENTO ENCERRADO')
                #     print('----------------------')
                #     break
            else:
                main()        
        else:
            main()
    else:
        main()       
        
        
           
# inicio do programa
print('BEM VINDO AO SISTEMA ANDROMEDA PORTO DE SUPORTE')
print('*'*47)
porto = input('Pressione (1) para Inicializar\nPressione (2) para Sair\n')
if porto == '2':
    print('Você saiu da aplicação')
elif porto == '1':
    main()
else:
    while porto != '1' and porto != '2':  # alteração na condição do while
        print('='*30)
        print('Não entendi. Tente novamente.')
        print('='*30)
        porto = input(
            '\nPressione (1) para Inicializar\nPressione (2) para Sair\n')
    if porto == '2':
        print('Você saiu da aplicação')
    elif porto == '1':
        main()
