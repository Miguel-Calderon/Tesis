import datetime
from google.appengine.ext import ndb
from modelos import Pliego


def objeto_fecha(arg):
    resultado = datetime.datetime.strptime(arg, "%Y-%m-%d")
    resultado = resultado.date()
    return resultado


def calculo_costo(fecha, lista, horario):
    inicio = fecha.inicio
    final = fecha.fin
    # primer prueba para obtener pliego si el mes esta dentro
    resultados = Pliego.query(Pliego.inicio_p < inicio)
    # encontrado = None
    if resultados:
        for resultado in resultados:
            if (resultado.final_p > final) & (resultado.final_p > inicio):
                # ---------------agregar un solo return--------------------
                # si entra aca tenemos el caso que el mes esta dentro de un pliego
                if horario == "punta":
                    lista[2] = lista[0] * resultado.punta_T
                    return lista
                elif horario == "valle":
                    lista[2] = lista[0] * resultado.valle_T
                    return lista
                elif horario == "resto":
                    lista[2] = lista[0] * resultado.resto_T
                    return lista
                elif horario == "potencia":
                    lista[2] = lista[0] * resultado.potencia_T
                    return lista
            elif (resultado.final_p < final) & (resultado.final_p > inicio):
                delta1 = (float((resultado.final_p - inicio).days))/(float((final-inicio).days))
                if horario == "punta":
                    parte1 = lista[0] * resultado.punta_T * delta1
                elif horario == "valle":
                    parte1 = lista[0] * resultado.valle_T * delta1
                elif horario == "resto":
                    parte1 = lista[0] * resultado.resto_T * delta1
                elif horario == "potencia":
                    parte1 = lista[0] * resultado.potencia_T * delta1
        # ---------en parte 1 se almacena el calculo con respecto al primer pliego--------------
    resultado2 = Pliego.query(Pliego.inicio_p > inicio)
    if resultado2:
        for resul in resultado2:
            if (resul.final_p > final) & (resul.inicio_p < final):
                delta2 = (float((final - resul.inicio_p).days)) / (float((final-inicio).days))
                if horario == "punta":
                    parte2 = lista[0] * resul.punta_T * delta2
                elif horario == "valle":
                    parte2 = lista[0] * resul.valle_T * delta2
                elif horario == "resto":
                    parte2 = lista[0] * resul.resto_T * delta2
                elif horario == "potencia":
                    parte2 = lista[0] * resul.potencia_T * delta2
    lista[2] = parte1 + parte2
    return lista


def total_acometida(lista_punta, lista_valle, lista_resto, lista_pot):
    suma_total = [0, 0, 0]
    for contador in range(3):
        suma_total[contador] = lista_punta[contador]+lista_valle[contador]+lista_resto[contador]
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
