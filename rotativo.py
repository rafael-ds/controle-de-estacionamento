rotativo = [{'Placa': '1234', 'Modelo': 'dk150', 'Cor': 'vermelha'}]


def entrada(placa_car, modelo_car, cor_car):
    user = {'Placa': placa_car, 'Modelo': modelo_car, 'Cor': cor_car}

    for i in rotativo:
        for b in i:
            return b


#  Menu
print('=' * 20 + ' RS ROTATIVO ' + '=' * 20)
print('\n')

while True:
    print('-' * 10 + ' MENU ' + '-' * 10)

    print(' Entre com a opção desejada\n'
          '1 - Gerar entrada de veiculos: ')

    opc = input()

    if opc == '1':
        print('=' * 20)
        print('Entrada de veiculos')
        print('-' * 20)

        placa = input('Informe a placa: ')
        modelo = input('Informe o modelo: ')
        cor = input('Informe a cor: ')

        print(entrada(placa, modelo, cor))

    else:
        break

