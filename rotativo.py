vagas_rotativo = []


def cadastro_rotativo(placa, modelo, cor):
    """
    Tem como objetico adquiri os dados do veiculo

    :param placa: Pede a placa do veiculo
    :param modelo: pede o modelo do veiculo
    :param cor: Pede a cor predominante do veiculo
    :return: dados
    """
    dados = {'Placa': placa, 'Modelo': modelo, 'Cor': cor}
    return dados


def dados_veic_rotat():
    enter_placa = input('Informe a placa do veiculo: ')
    enter_modelo = input('Informe o modelo do veiculo: ')
    enter_cor = input('Informe a cor do veiculo: ')

    cadastro = cadastro_rotativo(enter_placa, enter_modelo, enter_cor)  # cadastro --> armazena a função
    # cadastro_rotativo() recebendo como argumento
    # os dados do veiculo informado pelo usuario
    vagas_rotativo.append(cadastro)  # adiciona a lista vaga_rotativo o os dados informado pelo usuario


while True:
    opc = input('Digite (1) para entra ou (2) para sair: ')
    if opc != '2':
        placa_car = input('Placa: ')
        dado = list(filter(lambda p: p['Placa'] == placa_car, vagas_rotativo))  # pecorre a lista vaga_rotativo em
        # comparando o placa_car com dado

        if dado:
            print(dado)
        else:
            um = input('A placa informada não se encontra cadastrada: \npara cadastra-la pressione (1)')
            if um:
                dados_veic_rotat()
            else:
                break
    else:
        break

print(vagas_rotativo)
