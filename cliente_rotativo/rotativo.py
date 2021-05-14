import csv
from time import sleep
import datetime as dt

from formatacao import format
from bd import bd_rotativo as bd

lista_cadastro = []  # lista para cast de cadastro dos veiculos
vagas_rotativo = []  # lista para cast de rotativo dos veiculos
total_vaga_rotativo = 100  # cria uma logica de configurações -- Refatorar


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
    sleep(1)

    bd.bd_cadastro(dados_user)  # acessa o pacote do banco de dados de cadasttro
    bd.bd_vagas_rotativo(dados_user)  # acessa o pacote do banco de dados do rotativo


def cadastro_veic(placa):
    """
    Funcção que verifica se a placa enformada esta cadastrada e caso não esteja,
    executa a função de cadastro chamando junto com a função dados.
    :param placa:
    """
    print(f'A placa {placa} não esta cadastrada. Deseja cadastra? ')
    cadastra = input('(s) Sim - (n) Não: ')
    print('-' * 40)
    sleep(1)

    if cadastra == 's':
        enter_modelo = input('Informe o modelo do veiculo: ').title()
        enter_cor = input('Informe a cor do veiculo: ').title()

        dados(placa, enter_modelo, enter_cor)  # chamada da função dados com os parametros
        # placa, modelo e cor

    elif cadastra == 'n':
        print('Saindo do cadastro... \n')
        sleep(1)


def entrada_saida_liberada():
    """
    Uma pequena função estetica que mostra a liberação do veiculo
    apos se cadastrado na lista_cadasto ou confirmado na mesma.
    :return:
    """

    for i in range(3):
        print(i)
        sleep(1)
    sleep(1)
    print('')


# Função para buscar e verificar a existencia de placa e liberar entrada do usuario
def entrada(placa):
    """
    Função que tem como objetivo atravez do parametro 'placa' verificar se a mesma existe
    liberando o usuario para entrar no rotativo.

    :param placa: Verifica se a placa digitada existe, caso exista libera a entrada, caso contrario
           cria um cadastro do novo usuario
    """

    # TRY -> Verifica se o arquivo "bd_vagas_rotativos.csv" existe.
    #  Caso exista executa o logica abaixo
    try:

        #  Inicio da logica para verificar se o limite de vagas não foi excedido
        with open('bd_vagas_rotativos.csv', 'r') as abrir:
            ler = list(csv.DictReader(abrir))
            if len(ler) > total_vaga_rotativo:
                print('Não existe vagas disponiveis no rotativo. \n')
                sleep(1)
            #  -----------------------------------------------------------------------
            else:
                #  Verifica se o arquivo "bd_cadastro_cliente_rotativo" existe
                try:
                    with open('bd_cadastro_cliente_rotativo.csv', 'r', encoding='utf-8', newline='') as abrir:
                        ler = csv.DictReader(abrir)
                        usuario = list(filter(lambda user: user['Placa'] == placa, ler))  # busca pela placa do veiculo

                        if usuario:
                            print('Usuario cadastrado: ')

                            #  Mostra os dados do usuario
                            for i in usuario:
                                user = i.get('Placa'), i.get('Modelo'), i.get('Cor')
                                data = i.get('Data'), i.get('Hora')

                                print(user)
                                print(f'Ultimo acesso {data}')
                            print('-' * 40)
                            # -------------- Fim ------------------

                            confirmacao = int(input('Confirme os dados: (1)-OK -- (2)-Cancelar. '))
                            if confirmacao == 1:
                                print('-' * 10)
                                print('Veiculo liberado para entrada. ')
                                print('Ergendo a cancela... ')

                                # chamada da função qua atualiza o arquivo bd_cadastro_cliente_rotativo
                                atualizar_cc_csv(i)
                                entrada_saida_liberada()  # Chamada da função estetica

                                #  ------Logica para atulização da data e hora caso o
                                #  cliente volte a usar o rotativo ------
                                with open('bd_cadastro_cliente_rotativo.csv', 'r', encoding='utf-8',
                                          newline='') as abrir:
                                    ler = csv.DictReader(abrir)
                                    for i in ler:
                                        vagas_rotativo.append(i)

                                for veiculos in vagas_rotativo:
                                    if veiculos['Placa'] == placa:
                                        veiculos['Hora'] = format.format_hora()
                                        veiculos['Data'] = format.format_data()

                                        with open('bd_vagas_rotativos.csv', 'a', encoding='utf-8',
                                                  newline='') as atualizar:
                                            cabecalho = ['Placa', 'Modelo', 'Cor', 'Data', 'Hora']
                                            escrever = csv.DictWriter(atualizar, fieldnames=cabecalho)
                                            if atualizar.tell() == 0:
                                                escrever.writeheader()

                                            escrever.writerow(veiculos)
                                        del vagas_rotativo[:]
                                #  ------Fim  daLogica para atulização da data e hora caso o
                                #  cliente volte a usar o rotativo ----

                            elif confirmacao == 2:
                                sleep(1)

                            else:  # Usar Try Exection (ValueError)
                                'Entrada Invalida! '

                        #  Caso o usuario não esteja cadastrado, realiza o cadastro
                        else:
                            cadastro_veic(placa)

                #  Chamada de except se o "bd_cadastro_cliente_rotativo" não exista.
                except FileNotFoundError:
                    cadastro_veic(placa)

    # EXCEPT -> Caso o arquivo "bd_vagas_rotativos.csv" não exista
    #  executa a função de cadastro
    except FileNotFoundError:
        cadastro_veic(placa)


def cast_vaga_rotivo():
    """
     Função que pega os elementos do .csv e joga para o lista vagas rotativos
    """
    try:
        with open('bd_vagas_rotativos.csv', 'r', encoding='utf-8', newline='') as abrir:
            ler = csv.DictReader(abrir)

            #  Pecorre a variavel "ler" e adiciona na lista "vagas_rotativo"
            #  para que possa ser realizada a interação de um item
            for dados in ler:
                vagas_rotativo.append(dados)

    #  retorna a msgm caso o arquivo "bd_vagas_rotativos" não exista ou estaja vazio.
    except FileNotFoundError:
        return 'Ainda não existe nenhum veiculo no patio. '


def atualizar_vr_csv():
    """
    Função que atualiza o arquivo bd_vagas_rotativos.csv na hora da saida do veiculo
    """

    #  Abre o arquivo "bd_vagas_rotativos" em modo de escrita
    with open('bd_vagas_rotativos.csv', 'w', encoding='utf-8', newline='') as atualizar:
        cabecalho = ['Placa', 'Modelo', 'Cor', 'Data', 'Hora']
        escrever = csv.DictWriter(atualizar, fieldnames=cabecalho)
        if atualizar.tell() == 0:
            escrever.writeheader()

        for veiculos in vagas_rotativo:
            escrever.writerow(
                {'Placa': veiculos['Placa'], 'Modelo': veiculos['Modelo'],
                 'Cor': veiculos['Cor'], 'Data': veiculos['Data'], 'Hora': veiculos['Hora']})
    # Limpando a lista "vagas_rotativo" para que não haja
    #  Duplicadatas na proxíma interação
    del vagas_rotativo[:]


def cast_cadastro_cliente():
    """
    Função que acessa os itens do arquivo bd_cliente_rotativo em modo read e,
    faz o append dos dados para a lista_cadastro para iteração.

    :return: Condição que informa que não existe nenhum veiculo cadastrada para iterar
    """
    try:
        with open('bd_cadastro_cliente_rotativo.csv', 'r', encoding='utf-8', newline='') as abrir:
            ler = csv.DictReader(abrir)
            for dados in ler:
                lista_cadastro.append(dados)

    except FileNotFoundError:
        return 'Ainda não existe nenhum veiculo Cadastrado. '


def atualizar_cc_csv(placa):
    """
    Função que tem como objetivo atualiza os dados do arquivo "bd_cadastro_cliente_rotativo".
    Desenvolvida para quando um veiculo sair do estacionamento, no banco de cadastro a chave
    Data e Hora sejam atualizadas

    :param placa: Busca a placa do veiculo para que a iteração seja realizada no mesmo.
    """
    #  Chamada da função que realiza o cast, isto é, cria um lista iteravel.
    cast_cadastro_cliente()

    #  For que ira pecorrer a lista_cadastro e atualizar a Hora e a Data
    #  Para Data e Hora atual
    for veiculo in lista_cadastro:
        if veiculo == placa:
            veiculo['Hora'] = format.format_hora()
            veiculo['Data'] = format.format_data()

    with open('bd_cadastro_cliente_rotativo.csv', 'w', encoding='utf-8', newline='') as atualizar:
        cabecalho = ['Placa', 'Modelo', 'Cor', 'Data', 'Hora']
        escrever = csv.DictWriter(atualizar, fieldnames=cabecalho)
        if atualizar.tell() == 0:
            escrever.writeheader()

        for veiculo in lista_cadastro:
            escrever.writerow(veiculo)
    del lista_cadastro[:]


def saida(placa):
    """
    Função tem como objetivo verificar a existencia do veiculo no partio do rotativo atraves da placa.
    caso se encontre no rotativo, o mesmo será informado, realizando assim a cobrança da estadia ao usuario.

    :param placa: Necessario para que se possa iterar com o item no rotativo.
    """

    #  Chamada da função que realizara o cast para a lista vagas_rotativo
    cast_vaga_rotivo()

    for veiculo in vagas_rotativo:
        if veiculo['Placa'] == placa:  # Compara se a placa digitada se encotra no rotativo
            modelo = veiculo.get('Modelo')  # Cria uma variavel com o modelo do veiculo
            cor = veiculo.get('Cor')  # Cria uma variavel com a cor do veiculo

            print(f'-------------Descrição do veiculo---------------'
                  f'\nPlaca: {placa}\nModelo: {modelo}\nCor: {cor}')
            print('-' * 50)
            pagamento(veiculo)  # Chamada da função que tem a logica de pagamento
            liberar_saida = input('Liberar saida? (s) - (n): ')

            if liberar_saida == 's':
                vagas_rotativo.remove(veiculo)  # Remove o veiculo da lista vagas_rotativos

    # Chama a função que tem como objetivo atualizar o arquivo bd_vagas_rotativos
    # Com os itens da lista vagas_rotativo
    atualizar_vr_csv()

    print('Veiculo liberado para saida. ')
    print('Ergendo a cancela... ')
    entrada_saida_liberada()  # função estetica


def qnt_vagas_disponivel():
    """
    Função que terar como objetivo verificar a quantidade de vagas dsiponivel no rotativo
    por enquanto esta sendo ultilizada direto no função entrada
    :return:
    """
    with open('bd_vagas_rotativos.csv', 'r') as abrir:
        ler = list(csv.DictReader(abrir))
        l = total_vaga_rotativo
        qnt = l - len(ler)
    return f'Existem {qnt} vagas disponiveis no rotativo. '


def pagamento(placa_usuario):
    """
    Uma mini função do tipo gateway de pagamento, que tem como objetivo calcula atraves da entrada
    e saida do usuario do rotativo, a taxa de cobrança com uma logica de cobrança de um valor fixo para primeira hora
    e um valor fracionado para cada meia-hora excedente.

    :param placa_usuario:
    """
    valor_rotativo = float(7.0)  # valor fixo do rotativo

    dia_entrada = placa_usuario.get('Data')  # Variavel que armozena o dia da entrada do usuario
    hora_entrada = placa_usuario.get('Hora')  # Variavel que armazena a hora de entrada do usuario

    h_convertida = dt.datetime.strptime(hora_entrada, '%H:%M:%S')  # converte a hora de STR para datatime
    hora_ent = h_convertida.hour  # Variavel que armazena a hora convertida

    hora_saida = dt.datetime.now()  # variavel que armazena a data completa de saida do usuario
    hora_sd = hora_saida.hour  # variavel que  armazena somente a hora da saida

    sub_hora = hora_sd - hora_ent  # variavel que armazena a subtração da hora de saida menos a hora de entrada

    # Algoritimo que tem como objetivo verifica o tempo que o veiculo ficou no rotativo
    # Caso a hora seja de ate 1 hora, o valor cobrado serar  a taxa
    if sub_hora <= 1:
        print(f'Hora da entrada {hora_entrada}')
        print(f'Valor a ser pago é R$ {valor_rotativo}')
        sleep(1)

    # Caso a hora exceda a 1 hora, sera cobrado o exedente.
    else:

        # Exedente -> sb_hora - 1 -> retirando uma hora do excedente e dividindo o retante por meio
        # para que possa ser somada a fração.
        excedente = (sub_hora - 1) / .5

        pg = (excedente * 3) + valor_rotativo  # Valor a ser pago
        print(f'Hora da Entrada: {dia_entrada} - {hora_entrada}')
        print(f'Hora da Saida: {format.format_data()} - {format.format_hora()}')
        print(f'Valor a ser pago R$ {pg}')
        sleep(1)


def lista_veic_rotativo():

    with open('bd_vagas_rotativos.csv', 'r', newline='', encoding='utf-8') as abrir:
        ler = list(csv.DictReader(abrir))

        for i in ler:
            usuario = i.get('Placa'), i.get('Modelo'), i.get('Cor')
            data = i.get('Data'), i.get('Hora')

            print(f'Usuario: {usuario}')
            print(f'Entrada: {data}')
            print('-' * 50 + '\n')
