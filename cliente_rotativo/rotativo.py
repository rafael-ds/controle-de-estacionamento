from time import sleep
from formatacao import format

lista_cadastro = []
vagas_rotativo = []

dia_entrada = format.format_data()
horario_entrada = format.format_hora()


# Função para buscar e verificar a existencia de placa e liberar entrada do usuario
def entrada(placa):
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

    else:  # Verificação valida somente para o primeiro cadastro -- Refatorar(logica se repete)

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


def dados(placa, modelo, cor, dia=dia_entrada, hora=horario_entrada):
    """
    Cria um dicionario de dados de cliente

    :param hora:
    :param dia:
    :param placa: Pede a placa do veiculo
    :param modelo: Pede o modelo do veiculo
    :param cor: Pede a cor do veiculo
    """
    dados_user = {'Placa': placa, 'Modelo': modelo, 'Cor': cor, 'Data': dia, 'Hora': hora}
    sleep(1)
    print('Usuario cadastrado com sucesso!')

    entrada_liberada()
    lista_cadastro.append(dados_user)
    vagas_rotativo.append(dados_user)

    # print(f'Lista de usuario {lista_cadastro}')
    # print(f'Lista da vagas de rotativo {vagas_rotativo}')


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
    sleep(1)
    print('')


# Função para buscar e verificar a existencia de placa, se elas se encontra n rotativo liberar saida do usuario
def saida(placa):

    if len(vagas_rotativo) > 0:

        for placa_user in vagas_rotativo:
            if placa_user['Placa'] == placa:

                pagamento()

                # vagas_rotativo.remove(placa_user)
                sleep(1)

    else:
        sleep(1)
        print('Não existe veiculos no rotativo. ')
        sleep(1)
        print('')


def pagamento():
    pass
