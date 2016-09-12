import datetime
from google.appengine.ext import ndb


def objeto_fecha(arg):
    resultado = datetime.datetime.strptime(arg, "%Y-%m-%d")
    resultado = resultado.date()
    return resultado


def calculo_costo(fecha, lista):
    inicio = fecha.inicio
    final = fecha.final


def total_acometida(lista_pico, lista_valle, lista_resto, lista_pot):
    suma_total = [0, 0, 0]
    for contador in range(3):
        suma_total[contador] = lista_pico[contador]+lista_valle[contador]+lista_resto[contador]
        suma_total.append(lista_pot[contador])
    # suma_total= [kw/h, $ eneria, #calculado, kw, $pot, #calculado]
    # suma_total.append(lista_pot[0])
    # suma_total[1]+=lista_pot[1]
    # suma_total[2] += lista_pot[2]
    # total_energia = lista_pico[0]+lista_valle[0]+lista_resto[0]
    # dinero_energia = lista_pico[1]+lista_valle[1]+lista_resto[1]
    # total_calculado = lista_pico[2]+lista_valle[2]+lista_resto[2]
    # total_acometida = numpy.array([total_energia, dinero_energia, total_calculado])
    return suma_total
    # total energia, total dinero


def total_mes(total_aco, lista_mes):
    suma_mes = [0, 0, 0, 0, 0, 0]
    for contador in range(6):
        suma_mes[contador] = total_aco[contador]+lista_mes[contador]
    return suma_mes

def obtener_entity(tipo, entity_id):
    entity_key = ndb.Key(tipo, entity_id)
    respuesta = entity_key.get()
    return respuesta
