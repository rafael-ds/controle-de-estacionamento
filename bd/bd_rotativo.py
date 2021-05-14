import csv
from formatacao import format


def bd_cadastro(dados):
    """
     Criar um .CSV com os dados de entrarda do veiculo
     :param dados: Variavel que atravez da placa traz as caracteristica do veiculo

     """
    with open('bd_cadastro_cliente_rotativo.csv', 'a', encoding='utf-8', newline='') as salvar:
        cabecalho = ['Placa', 'Modelo', 'Cor', 'Data', 'Hora']
        escrever = csv.DictWriter(salvar, fieldnames=cabecalho)

        if salvar.tell() == 0:
            escrever.writeheader()

        escrever.writerow(dados)


def bd_vagas_rotativo(dados):
    with open('bd_vagas_rotativos.csv', 'a', encoding='utf-8', newline='') as salvar:
        cabecalho = ['Placa', 'Modelo', 'Cor', 'Data', 'Hora']
        escrever = csv.DictWriter(salvar, fieldnames=cabecalho)

        if salvar.tell() == 0:
            escrever.writeheader()

        escrever.writerow(dados)
