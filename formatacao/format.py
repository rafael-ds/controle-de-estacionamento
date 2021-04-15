import datetime as dt


def format_data():
    data = dt.datetime.now()
    data_br = data.strftime('%d/%m/%Y')

    return data_br


def format_hora():
    horario = dt.datetime.now()
    hora = horario.strftime('%H:%M:%S')

    return hora


