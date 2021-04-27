import csv


def banco(dados):
     with open('cliente_rotativo.csv', 'a', encoding='utf-8', newline='' ) as salvar:
          cabecalho =  ['Placa', 'Modelo', 'Cor','Data', 'Hora']
          escrever = csv.DictWriter(salvar, fieldnames=cabecalho)

          if salvar.tell() == 0:
               escrever.writeheader()

          escrever.writerow(dados)