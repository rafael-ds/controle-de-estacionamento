# Meus Diretorios
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
    print('3 - Total de Vagas : ')
    print('4 - Total de Vagas Disponivel no Rotativo: ')
    print('5 - Total de Vagas Disponivel no Vip: ')
    print('6 - Mostra Veiculos no Rotativo: ')
    print('7 - Mostra Veiculos no Vip: ')
    print('8 - Cadastrar Vip: ')
    print('9 - Remover Vip: ')
    print('10 - Remover Rotativo: ')
    print('11 - Buscar por Veiculo: ')
    print('12 - Sair do Programa: ')
    print('')

    opcao = int(input('Opcão -> \n'))

    if opcao == 1:
        print('-' * 17 + ' Gerando Entrada ' + '-' * 17)

        placa = input('Informe a placa do veiculo: \n')
        rotativo.placa_c(placa)
        menu()

    elif opcao == 2:
        pass

    elif opcao == 3:
        pass

    elif opcao == 4:
        pass

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
        pass

    elif opcao == 12:
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