import datetime


def objeto_fecha(arg):
    resultado = datetime.datetime.strptime(arg, "%Y-%m-%d")
    resultado = resultado.date()
    return resultado


