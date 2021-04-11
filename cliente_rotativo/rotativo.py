from time import sleep

lista_cadastro = []

vagas_rotativos = []


# Função para buscar e verificar a existencia de placa
def placa_c(placa):
    """
    Função que tem como objetivo atravez do parametro 'placa' verificar se a mesma existe
    liberando o usuario para entrar no rotativo.

    :param placa: Verifica se a placa digitada existe, caso exista libera a entrada, caso contrario
           cria um cadastro do novo usuario


    """

    if len(lista_cadastro) > 0:

        usuario = list(filter(lambda u: u['Placa'] == placa, lista_cadastro))  # faz uma busca na lista atravez da chave
        #  'Placa' e compara com input digitado pelo usuario em rotativo.py atraves do parametro placa da função

        if usuario:
            print('Usuario cadastrado: ')

            for i in usuario:
                print(i)
            print('-' * 40)

            confirmacao = int(input('Confirme os dados: (1)-OK -- (2)-Cancelar. '))
            if confirmacao == 1:
                entrada_liberada()

            elif confirmacao == 2:
                sleep(1)

            else:  # Usar Try Exection (ValueError)
                'Entrada Invalida! '

        else:  # Refatorar
            print(f'A placa {placa} não esta cadastrada. Deseja cadastra? ')
            cadastra = input('(s) Sim - (n) Não: ')
            print('-' * 40)

            if cadastra == 's':
                enter_modelo = input('Informe o modelo do veiculo: ').title()
                enter_cor = input('Informe a cor do veiculo: ').title()

                dados(placa, enter_modelo, enter_cor)

            elif cadastra == 'n':
                print('Saindo do cadastro... \n')
                sleep(1)

    else:  # Verificação falida somente para o primeiro cadastro -- Refatorar

        print(f'A placa {placa} não esta cadastrada. Deseja cadastra? ')
        cadastra = input('(s) Sim - (n) Não: ')
        print('-' * 40)
        sleep(1)

        if cadastra == 's':
            enter_modelo = input('Informe o modelo do veiculo: ').title()
            enter_cor = input('Informe a cor do veiculo: ').title()

            dados(placa, enter_modelo, enter_cor)

        elif cadastra == 'n':
            print('Saindo do cadastro... \n')
            sleep(1)


def dados(placa, modelo, cor):
    """
    Cria um dicionario de dados de cliente

    :param placa: Pede a placa do veiculo
    :param modelo: Pede o modelo do veiculo
    :param cor: Pede a cor do veiculo
    """
    dados_user = {'Placa': placa, 'Modelo': modelo, 'Cor': cor}
    sleep(2)
    print('Usuario cadastrado com sucesso!')

    entrada_liberada()
    lista_cadastro.append(dados_user)

    for i in lista_cadastro:
        sleep(1)
        print(i)
        print('')


def entrada_liberada():
    """
    Uma pequena função estetica que mostra a liberação do veiculo
    apos se cadastrado na lista_cadasto ou confirmado na mesma.
    :return:
    """
    print('Veiculo liberado para entrada. ')
    print('Ergendo a cancela... ')

    for i in range(3):
        print(i)
        sleep(1)
    sleep(3)
    print('')