from utils import renderutils, formatutils
from modelos import YearT, Acometida, Factura, Pliego
import datetime


class GraficaHandler(renderutils.MainHandler):
    def get(self):
        primer_year = formatutils.obtener_entity(YearT, 2004)

        # busca en la base de datos  la entity perteneciente al 2004 y a los  3 mas recientes
        resultado = formatutils.obtener_year(primer_year, "EnergiaT")
        resultadoD = formatutils.obtener_year(primer_year, "EnergiaD")
        date_ahora = datetime.date.today().year
        segundo_year = formatutils.obtener_entity(YearT, date_ahora)
        resultado2 = formatutils.obtener_year(segundo_year, "EnergiaT")
        resultado2D = formatutils.obtener_year(segundo_year, "EnergiaD")
        tercer_year = formatutils.obtener_entity(YearT, date_ahora - 1)
        resultado3 = formatutils.obtener_year(tercer_year, "EnergiaT")
        resultado3D = formatutils.obtener_year(tercer_year, "EnergiaD")
        cuarto_year = formatutils.obtener_entity(YearT, date_ahora - 2)
        resultado4 = formatutils.obtener_year(cuarto_year, "EnergiaT")
        resultado4D = formatutils.obtener_year(cuarto_year, "EnergiaD")

        titulo = [date_ahora - 2, date_ahora - 1, date_ahora]

        orientacion = formatutils.obtener_meses("cadena")
        datos2 = list()
        datos1 = list()
        # for utilizado para llenar las listas de datos enviadas al javascript
        # para generar graficas de comparacion de los mas recientes y el primer year
        # en datos1 se encuentran los datos de la energia
        # en datos2 se encuentran los datos de dinero
        for elemento in orientacion:
            datos1.append({
                "mes": elemento,
                "year1": resultado[elemento],
                "year2": resultado2[elemento],
                "year3": resultado3[elemento],
                "year4": resultado4[elemento]
            })
            datos2.append({
                "mes": elemento,
                "year1": resultadoD[elemento],
                "year2": resultado2D[elemento],
                "year3": resultado3D[elemento],
                "year4": resultado4D[elemento]
            })

        # en los 2 for anidados se obtienen todos los elementos el mas externo corre sobre  year_T
        # y en el for mas interno se corre los meses

        orientacion2 = formatutils.obtener_meses("entero")
        todos_year = YearT.query().order(YearT.nombre)
        datos3 = list()
        datos4 = list()
        datos_punta = list()
        datos_valle = list()
        datos_resto = list()
        datos_total = list()
        datos_pot = list()
        datos_anuales = list()

        for year in todos_year:
            for mes in orientacion2:
                #  grafica comparativa valores anuales totales
                if year.nombre > "2000":
                    datos3.append({

                        "date": str(year.nombre) + "-" + mes,
                        "potenciaD": formatutils.obtener_month(year, mes, "PotD"),
                        "EnergiaT": formatutils.obtener_month(year, mes, "EnergiaT"),
                        "EnergiaD": formatutils.obtener_month(year, mes, "EnergiaD"),
                        "DineroTT": formatutils.format_decimal(formatutils.obtener_month(year, mes, "EnergiaD") +
                                                               formatutils.obtener_month(year, mes, "PotD"))
                    })
                # grafica mekko comparativa % del costo de cada franja horaria y la demanda de potencia
                if year.nombre > "2000":
                    datos4.append({
                        "date": str(year.nombre) + "-" + mes,
                        "PotenciaD": formatutils.obtener_month(year, mes, "PotD"),
                        "PuntaD": formatutils.obtener_month(year, mes, "PuntaD"),
                        "ValleD": formatutils.obtener_month(year, mes, "ValleD"),
                        "RestoD": formatutils.obtener_month(year, mes, "RestoD"),
                        "total": (formatutils.obtener_month(year, mes, "PotD") +
                                  formatutils.obtener_month(year, mes, "PuntaD") +
                                  formatutils.obtener_month(year, mes, "ValleD") +
                                  formatutils.obtener_month(year, mes, "RestoD"))
                    })
                    # grafica comparativa de los datos de cada franja horaria  y total
                    datos_punta.append({
                        "date": str(year.nombre) + "-" + mes,
                        "value": formatutils.obtener_month(year, mes, "PuntaE"),
                        "volume": formatutils.obtener_month(year, mes, "PuntaD")
                    })
                    datos_valle.append({
                        "date": str(year.nombre) + "-" + mes,
                        "value": formatutils.obtener_month(year, mes, "ValleE"),
                        "volume": formatutils.obtener_month(year, mes, "ValleD")
                    })
                    datos_resto.append({
                        "date": str(year.nombre) + "-" + mes,
                        "value": formatutils.obtener_month(year, mes, "RestoE"),
                        "volume": formatutils.obtener_month(year, mes, "RestoD")
                    })
                    datos_total.append({
                        "date": str(year.nombre) + "-" + mes,
                        "value": formatutils.obtener_month(year, mes, "EnergiaT"),
                        "volume": formatutils.obtener_month(year, mes, "EnergiaD")
                    })
                    datos_pot.append({
                        "date": str(year.nombre) + "-" + mes,
                        "dinero": formatutils.obtener_month(year, mes, "PotD"),
                        "energia": formatutils.obtener_month(year, mes, "PotE")
                    })
            # Grafica datos  totales por year
            datos_anuales.append({
                "date": str(year.nombre),
                "potenciaD": formatutils.obtener_month(year, "total", "PotD"),
                "EnergiaT": formatutils.obtener_month(year, "total", "EnergiaT"),
                "EnergiaD": formatutils.obtener_month(year, "total", "EnergiaD"),
                "DineroTT": formatutils.obtener_month(year, "total", "EnergiaD") + formatutils.obtener_month(year,
                                                                                                             "total",
                                                                                                             "PotD")
            })
        # graficas con datos organizados por acometidas
        datos_fp = list()
        datos_fp2 = list()
        nombres_fp = list()
        datos_acometida = list()
        datos_acometida2 = list()
        datos_demanda = list()
        datos_demanda2 = list()
        qry_Acometida = Acometida.query().order(Acometida.nombre)
        for entidad in qry_Acometida:
            qry_Factura = Factura.query(Factura.Aco_Key == entidad.nombre).order(Factura.Fecha_Key)
            for elemento in qry_Factura:
                datos_fp2.append({
                    "date": str(elemento.Fecha_Key),
                    "fp": elemento.f_pot_tr[0],
                })
                datos_acometida2.append({
                    "date": str(elemento.Fecha_Key),
                    "energia": formatutils.format_decimal(
                        elemento.Punta_Lista[1] + elemento.Valle_Lista[1] + elemento.Resto_Lista[1] +
                        elemento.Potencia_Lista[1]),
                })
                datos_demanda2.append({
                    "date": str(elemento.Fecha_Key),
                    "energia": elemento.Potencia_Lista[0],
                    "dinero": elemento.Potencia_Lista[1],
                })

            datos_fp.append(datos_fp2)
            datos_fp2 = list()
            datos_acometida.append(datos_acometida2)
            datos_acometida2 = list()
            nombres_fp.append(str(entidad.nombre))
            datos_demanda.append(datos_demanda2)
            datos_demanda2 = list()
        longitud = len(nombres_fp)
        pliego_punta = list()
        pliego_valle = list()
        pliego_resto = list()
        pliego_potencia = list()

        qry_Pliego = Pliego.query().order(Pliego.inicio_p)
        for elemento in qry_Pliego:
            pliego_punta.append(
                {
                    "date": str(elemento.inicio_p),
                    "value": elemento.punta_T,

                })
            pliego_valle.append(
                {
                    "date": str(elemento.inicio_p),
                    "value": elemento.valle_T,

                })
            pliego_resto.append(
                {
                    "date": str(elemento.inicio_p),
                    "value": elemento.resto_T,

                })
            pliego_potencia.append(
                {
                    "date": str(elemento.inicio_p),
                    "value": elemento.potencia_T,

                })


        self.render("graficas.html",
                    datos=datos1,
                    datos2=datos2,
                    titulo=titulo,
                    datos3=datos3,
                    punta=datos_punta,
                    valle=datos_valle,
                    resto=datos_resto,
                    total=datos_total,
                    mekko=datos4,
                    factor=datos_fp,
                    nombres_fp=nombres_fp,
                    longitud=longitud,
                    potencia=datos_pot,
                    acometida=datos_acometida,
                    datos_anuales=datos_anuales,
                    pliego_punta=pliego_punta,
                    pliego_valle=pliego_valle,
                    pliego_resto=pliego_resto,
                    pliego_potencia=pliego_potencia,
                    demanda_pot=datos_demanda)
        # self.response.out.write(datos1)
