# Meus Diretorios
import cliente_rotativo.rotativo
from cliente_rotativo import rotativo

from time import sleep

def menu():
    print('=' * 40)
    print('-' * 15 + ' Rotativo ' + '-' * 15)
    print('-' * 15 + ' RS DevWeb ' + '-' * 14)
    print('=' * 40 + '\n')

    print('-' * 17 + ' Menu ' + '-' * 17)

    print('Entre com a opção desejada: ')
    print('-' * 40 + '\n')

    print('1 - Gerar Entrada:  ')
    print('2 - Gerar Saida:  ')
    print('3 - Total de Vagas Rotativo : ')
    print('4 - Vagas Disponivel no Rotativo: ')
    print('5 - Mostra Veiculos no Rotativo: ')
    print('6 - Buscar por Veiculo: ')
    print('7 - Cadastrar Vip:')
    print('8 - Mostra Veiculos Vip: ')
    print('9 - Vagas Disponivel no Vip: ')
    print('10 - Remover Vip: ')
    print('11 - Sair do Programa: ')
    print('')

    opcao = int(input('Opcão -> '))

    # Entrada
    if opcao == 1:
        print('-' * 17 + ' Gerando Entrada ' + '-' * 17)

        placa_user = input('Informe a placa do veiculo: \n')
        rotativo.entrada(placa_user)

        menu()

    # Saida
    elif opcao == 2:
        print('-' * 17 + ' Gerando Saida ' + '-' * 17)

        placa_saida = input('Informe a placa do veiculo: \n')
        rotativo.saida(placa_saida)

        menu()

    # Total de Vagas Rotativo
    #  Mostrar no menu configurações
    elif opcao == 3:
        pass

    # Vagas Disponivel no Rotativo
    elif opcao == 4:
        print('-' * 17 + ' Vagas Disponivel no Rotativo ' + '-' * 17)
        print(cliente_rotativo.rotativo.qnt_vagas_disponivel())
        print('')
        sleep(1)
        menu()

    elif opcao == 5:
        pass

    elif opcao == 6:
        pass

    elif opcao == 7:
        pass

    elif opcao == 8:
        pass

    elif opcao == 9:
        pass

    elif opcao == 10:
        pass

    elif opcao == 11:
        print('Deseja sair do programa? ')
        sair = str(input('(s) sair - (n) não sair. '))

        if sair == 's':
            print('Encerrando o programa... ')
            sleep(2)
            exit(0)
        elif sair == 'n':
            sleep(1)
            print('')
            menu()
        else:
            print('Opção Invalida. \n')
            sleep(1)
            menu()

    else:
        print('Entrada Invalida. Tente novamente. ')
        sleep(1)
        menu()


menu()