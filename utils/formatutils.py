import datetime
from google.appengine.ext import ndb
from modelos import Pliego, YearT, Recientes, Usuarios


def objeto_fecha(arg):
    resultado = datetime.datetime.strptime(arg, "%Y-%m-%d")
    resultado = resultado.date()
    return resultado


def calculo_costo(fecha, lista, horario):
    inicio = fecha.inicio
    final = fecha.fin
    parte1 = 0.0
    parte2 = 0.0
    # primer prueba para obtener pliego si el mes esta dentro
    resultados = Pliego.query(Pliego.inicio_p < inicio)
    # encontrado = None
    if resultados:
        for resultado in resultados:
            if (resultado.final_p > final) & (resultado.final_p > inicio):
                # ---------------agregar un solo return--------------------
                # si entra aca tenemos el caso que el mes esta dentro de un pliego
                if horario == "punta":
                    lista[2] = lista[0] * resultado.punta_T * 1.13
                    return lista
                elif horario == "valle":
                    lista[2] = lista[0] * resultado.valle_T * 1.13
                    return lista
                elif horario == "resto":
                    lista[2] = lista[0] * resultado.resto_T * 1.13
                    return lista
                elif horario == "potencia":
                    lista[2] = lista[0] * resultado.potencia_T * 1.13
                    return lista
            elif (resultado.final_p < final) & (resultado.final_p > inicio):
                delta1 = (float((resultado.final_p - inicio).days)) / (float((final - inicio).days))
                if horario == "punta":
                    parte1 = lista[0] * resultado.punta_T * delta1 * 1.13
                elif horario == "valle":
                    parte1 = lista[0] * resultado.valle_T * delta1 * 1.13
                elif horario == "resto":
                    parte1 = lista[0] * resultado.resto_T * delta1 * 1.13
                elif horario == "potencia":
                    parte1 = lista[0] * resultado.potencia_T * delta1 * 1.13
                    # ---------en parte 1 se almacena el calculo con respecto al primer pliego--------------
    resultado2 = Pliego.query(Pliego.inicio_p > inicio)
    if resultado2:
        for resul in resultado2:
            if (resul.final_p > final) & (resul.inicio_p < final):
                delta2 = (float((final - resul.inicio_p).days)) / (float((final - inicio).days))
                if horario == "punta":
                    parte2 = lista[0] * resul.punta_T * delta2 * 1.13
                elif horario == "valle":
                    parte2 = lista[0] * resul.valle_T * delta2 * 1.13
                elif horario == "resto":
                    parte2 = lista[0] * resul.resto_T * delta2 * 1.13
                elif horario == "potencia":
                    parte2 = lista[0] * resul.potencia_T * delta2 * 1.13
        lista[2] = parte1 + parte2
    # else:
        # lista[2] = 0.0
    return lista


def total_acometida(lista_punta, lista_valle, lista_resto, lista_pot):
    suma_total = [0, 0]
    for contador in range(2):
        suma_total[contador] = lista_punta[contador] + lista_valle[contador] + lista_resto[contador]
        suma_total += lista_punta + lista_valle + lista_resto + lista_pot
    # suma_total= [kw/h total, $ eneria total, punta[Energia,Dinero,Calculo], valle[Energia,Dinero,Calculo],
    #              resto[Energia,Dinero,calculo], potencia[kw, $pot, #calculado]]
    # suma_total.append(lista_pot[0])
    # suma_total[1]+=lista_pot[1]
    # suma_total[2] += lista_pot[2]
    return suma_total
    # total energia, total dinero


def total_mes(total_aco, lista_mes):
    suma_mes = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
    for contador in range(14):
        suma_mes[contador] = total_aco[contador] + lista_mes[contador]
    return suma_mes


def obtener_entity(tipo, entity_id):
    entity_key = ndb.Key(tipo, entity_id)
    respuesta = entity_key.get()
    return respuesta


def crear_year(date, lista):
    mes = date.month
    nombre = str(date.year)
    lista2 = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    year_entity = YearT(id=date.year,
                        nombre=nombre,
                        Enero=lista2,
                        Febrero=lista2,
                        Marzo=lista2,
                        Abril=lista2,
                        Mayo=lista2,
                        Junio=lista2,
                        Julio=lista2,
                        Agosto=lista2,
                        Septiembre=lista2,
                        Octubre=lista2,
                        Noviembre=lista2,
                        Diciembre=lista2,
                        Total_anual=lista)

    if mes == 1:
        year_entity.Enero = lista
    elif mes == 2:
        year_entity.Febrero = lista
    elif mes == 3:
        year_entity.Marzo = lista
    elif mes == 4:
        year_entity.Abril = lista
    elif mes == 5:
        year_entity.Mayo = lista
    elif mes == 6:
        year_entity.Junio = lista
    elif mes == 7:
        year_entity.Julio = lista
    elif mes == 8:
        year_entity.Agosto = lista
    elif mes == 9:
        year_entity.Septiembre = lista
    elif mes == 10:
        year_entity.Octubre = lista
    elif mes == 11:
        year_entity.Noviembre = lista
    elif mes == 12:
        year_entity.Diciembre = lista

    return year_entity


def actualizar_year(date, lista, entity2):
    mes = date.month
    total = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    if mes == 1:
        entity2.Enero = lista
    elif mes == 2:
        entity2.Febrero = lista
    elif mes == 3:
        entity2.Marzo = lista
    elif mes == 4:
        entity2.Abril = lista
    elif mes == 5:
        entity2.Mayo = lista
    elif mes == 6:
        entity2.Junio = lista
    elif mes == 7:
        entity2.Julio = lista
    elif mes == 8:
        entity2.Agosto = lista
    elif mes == 9:
        entity2.Septiembre = lista
    elif mes == 10:
        entity2.Octubre = lista
    elif mes == 11:
        entity2.Noviembre = lista
    elif mes == 12:
        entity2.Diciembre = lista

    for contador in range(14):
        total[contador] = (entity2.Enero[contador] + entity2.Febrero[contador] + entity2.Marzo[contador] +
                           entity2.Abril[contador] + entity2.Mayo[contador] + entity2.Junio[contador] +
                           entity2.Julio[contador] + entity2.Agosto[contador] + entity2.Septiembre[contador] +
                           entity2.Octubre[contador] + entity2.Noviembre[contador] + entity2.Diciembre[contador])

    entity2.Total_anual = total

    # for para iterar sobre los 14 elementos de cada mes y sumarlos
    return entity2


def obtener_meses(seleccion):
    if seleccion == "cadena":
        lista_meses = ["Enero", "Febrero", "Marzo", "Abril", "Mayo", "Junio",
                       "Julio", "Agosto", "Septiembre", "Octubre", "Noviembre", "Diciembre"]

    elif seleccion == "entero":
        lista_meses = ["01", "02", "03", "04", "05", "06", "07", "08", "09", "10", "11", "12"]

    return lista_meses


def obtener_year(year_entity, peticion):
    #       [kw / h total, $ eneria total, punta[Energia, Dinero, Calculo], valle[Energia, Dinero, Calculo],
    #        resto[Energia,Dinero,calculo], potencia[kw, $pot, #calculado]]
    lista_peticion = {"EnergiaT": 0,
                      "EnergiaD": 1,
                      "PuntaE": 2,
                      "PuntaD": 3,
                      "ValleE": 5,
                      "ValleD": 6,
                      "RestoE": 8,
                      "RestoD": 9,
                      "PotE": 11,
                      "PotD": 12}

    valor = lista_peticion[peticion]

    lista_year = {"Enero": year_entity.Enero[valor], "Febrero": year_entity.Febrero[valor],
                  "Marzo": year_entity.Marzo[valor], "Abril": year_entity.Abril[valor],
                  "Mayo": year_entity.Mayo[valor], "Junio": year_entity.Junio[valor],
                  "Julio": year_entity.Julio[valor], "Agosto": year_entity.Agosto[valor],
                  "Septiembre": year_entity.Septiembre[valor], "Octubre": year_entity.Octubre[valor],
                  "Noviembre": year_entity.Noviembre[valor], "Diciembre": year_entity.Diciembre[valor]}

    return lista_year


def obtener_month(year_entity, mes, peticion):
    lista_peticion = {"EnergiaT": 0,
                      "EnergiaD": 1,
                      "PuntaE": 2,
                      "PuntaD": 3,
                      "ValleE": 5,
                      "ValleD": 6,
                      "RestoE": 8,
                      "RestoD": 9,
                      "PotE": 11,
                      "PotD": 12}

    valor = lista_peticion[peticion]

    dict_peticion = {"01": year_entity.Enero[valor], "02": year_entity.Febrero[valor],
                     "03": year_entity.Marzo[valor], "04": year_entity.Abril[valor],
                     "05": year_entity.Mayo[valor], "06": year_entity.Junio[valor],
                     "07": year_entity.Julio[valor], "08": year_entity.Agosto[valor],
                     "09": year_entity.Septiembre[valor], "10": year_entity.Octubre[valor],
                     "11": year_entity.Noviembre[valor], "12": year_entity.Diciembre[valor],
                     "total": year_entity.Total_anual[valor]}

    return dict_peticion[mes]


def meses_recientes(inicio, lista_mes):
    #       [kw / h total, $ eneria total, punta[Energia, Dinero, Calculo], valle[Energia, Dinero, Calculo],
    #        resto[Energia,Dinero,calculo], potencia[kw, $pot, #calculado]]
    inicializacion = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]
    orientacion_meses = {1: "Enero", 2: "Febrero", 3: "Marzo", 4: "Abril", 5: "Mayo", 6: "Junio",
                         7: "Julio", 8: "Agosto", 9: "Septiembre", 10: "Octubre", 11: "Noviembre", 12: "Diciembre"}

    mes = orientacion_meses[inicio.month] + " de " + str(inicio.year)

    constructor = obtener_entity(Recientes, "ultimos")
    if constructor:
        constructor.mes1 = constructor.mes2
        constructor.mes2 = constructor.mes3
        constructor.mes3 = lista_mes
        constructor.mes_str[0] = constructor.mes_str[1]
        constructor.mes_str[1] = constructor.mes_str[2]
        constructor.mes_str[2] = mes
    else:
        constructor = Recientes(mes_str=["no info", "no info", mes],
                                mes1=inicializacion,
                                mes2=inicializacion,
                                mes3=lista_mes,
                                id="ultimos")

    return constructor


def iniciar_usuario():
    primero = Usuarios(nombre="Teddy",
                       contra="teddycalderon",
                       id="Teddy")

    primero.put()


def formatcifra(numero):
    # ""Adicionar comas como separadores de miles a n. n debe ser de tipo string"
    s = str(numero)
    i = s.index('.')
    # Se busca la posicion del punto decimal
    while i > 3:
        i -= 3
        s = s[:i] + ',' + s[i:]
    return s
