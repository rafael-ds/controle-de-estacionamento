
def format_data():
    import datetime
    data = datetime.datetime.today()
    data_br = data.strftime('%d/%m/%Y')

    return data_br


def format_hora():
    from datetime import datetime
    horario = datetime.now()

    return f'{horario.hour}:{horario.minute}:{horario.second}'


