from time import sleep
import datetime as dt
from formatacao import format

lista_cadastro = [{'Placa': '123', 'Modelo': 'Fd', 'Cor': 'Rew', 'Data': '14/04/2021', 'Hora': '17:34:44'}]
vagas_rotativo = [{'Placa': '123', 'Modelo': 'Fd', 'Cor': 'Rew', 'Data': '14/04/2021', 'Hora': '13:34:44'}]


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


def dados(placa, modelo, cor, dia=format.format_data(), hora=format.format_hora()):
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

    # entrada_liberada()
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

                modelo = placa_user.get('Modelo')
                cor = placa_user.get('Cor')
                print(f'-------------Descrição do veiculo---------------\nModelo: {modelo}\nCor: {cor}')
                pagamento(placa_user)
                pg_efetuado = input('Liberar saida? (s) - (n): ')

                if pg_efetuado == 's':
                    vagas_rotativo.remove(placa_user)
                    sleep(1)
                else:
                    print('Entrada Invalida! ')
                    sleep(1)

    else:
        sleep(1)
        print('Não existe veiculos no rotativo. ')
        sleep(1)
        print('')


def pagamento(placa_usuario):

    valor_rotativo = float(7.0)

    dia_entrada = placa_usuario.get('Data')
    hora_entrada = placa_usuario.get('Hora')  # Busca a hora de entrada do usuario
    h_convertida = dt.datetime.strptime(hora_entrada, '%H:%M:%S')  # converte a hora de STR para datatime
    hora_ent = h_convertida.hour, h_convertida.minute

    hora_saida = dt.datetime.now()
    hora_sd = hora_saida.hour, hora_saida.minute

    sub_hora = hora_sd[0] - hora_ent[0]

    if sub_hora <= 1:
        print(f'Hora da entrada {hora_entrada}')
        print(f'Valor a ser pago é R$ {valor_rotativo}')
        sleep(1)
    else:
        excedente = (sub_hora - 1) / .5

        pg = (excedente * 3) + valor_rotativo
        print(f'Hora da Entrada: {dia_entrada} - {hora_entrada}')
        print(f'Hora da Saida: {format.format_data()} - {format.format_hora()}')
        print(f'Valor a ser pago R$ {pg}')
        sleep(1)


