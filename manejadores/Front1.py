from utils import renderutils, formatutils
from modelos import YearT, Factura, Recientes
import datetime


class FrontHandler(renderutils.MainHandler):
    def get(self):
        # -----------------Datos actuales  para slide show ------------------------------------
        valor1 = 0.0
        date_ahora = datetime.date.today().year
        primer_year = formatutils.obtener_entity(YearT, date_ahora)
        if primer_year:
            valor1 = formatutils.obtener_month(primer_year, "total", "EnergiaD") + formatutils.obtener_month(
                primer_year,
                "total",
                "PotD")
        date_anterior = date_ahora - 1
        date_comparacion = formatutils.objeto_fecha(str(date_anterior) + "-01-01")
        date_final = formatutils.objeto_fecha(str(date_anterior) + "-12-31")
        anterior_year = formatutils.obtener_entity(YearT, date_anterior)
        valor2 = formatutils.obtener_month(anterior_year, "total", "EnergiaD") + formatutils.obtener_month(
                                                                                                        anterior_year,
                                                                                                        "total",
                                                                                                        "PotD")

        # ------------------datos para slide 2 totales anuales----------------------------------
        lista = [formatutils.formatcifra(str(formatutils.obtener_month(anterior_year, "total", "PuntaE"))),
                 formatutils.formatcifra(str(formatutils.obtener_month(anterior_year, "total", "PuntaD"))),
                 formatutils.formatcifra(str(formatutils.obtener_month(anterior_year, "total", "ValleE"))),
                 formatutils.formatcifra(str(formatutils.obtener_month(anterior_year, "total", "ValleD"))),
                 formatutils.formatcifra(str(formatutils.obtener_month(anterior_year, "total", "RestoE"))),
                 formatutils.formatcifra(str(formatutils.obtener_month(anterior_year, "total", "RestoD"))),
                 formatutils.formatcifra(str(formatutils.obtener_month(anterior_year, "total", "PotE"))),
                 formatutils.formatcifra(str(formatutils.obtener_month(anterior_year, "total", "PotD")))]

        # ------------------------datos para slide 3 totales por acometida --------------------------
        Qry_factura_agro = Factura.query(Factura.Aco_Key == "Agronomia", Factura.Fecha_dt >= date_comparacion,
                                         Factura.Fecha_dt <= date_final)

        Qry_factura_huma = Factura.query(Factura.Aco_Key == "Humanidades", Factura.Fecha_dt >= date_comparacion,
                                         Factura.Fecha_dt <= date_final)
        Qry_factura_comp = Factura.query(Factura.Aco_Key == "Complejo_Deportivo", Factura.Fecha_dt >= date_comparacion,
                                         Factura.Fecha_dt <= date_final)

        # Energia total  y demanda de potencia total de cada acometida
        # [kw/h total, $ energia, KW pot, $ pot]
        suma_agro = [0, 0, 0, 0]
        suma_huma = [0, 0, 0, 0]
        suma_comp = [0, 0, 0, 0]
        for elemento in Qry_factura_agro:
            for conteo in range(4):
                suma_agro[conteo] += elemento.ftotal[conteo]

        for elemento in Qry_factura_huma:
            for conteo in range(4):
                suma_huma[conteo] += elemento.ftotal[conteo]

        for elemento in Qry_factura_comp:
            for conteo in range(4):
                suma_comp[conteo] += elemento.ftotal[conteo]

        # -------------variable que contiene todos los datos de las acometidas para enviar al html
        acometidas = suma_agro + suma_huma + suma_comp

        for elemento in range(len(acometidas)):
            acometidas[elemento] = formatutils.formatcifra(str(acometidas[elemento]))

        # -------------------- variable con datos para grafica de pastel ------------------------------

        pie_morris = [suma_agro[1] + suma_agro[3], suma_huma[1] + suma_huma[3], suma_comp[1] + suma_comp[3]]
        total1 = float(sum(pie_morris))
        pie_morris = [(pie_morris[0]/total1)*100, (pie_morris[1]/total1)*100, (pie_morris[2]/total1)*100]

        pie_morris = [formatutils.format_decimal(pie_morris[0]), formatutils.format_decimal(pie_morris[1]),
                      formatutils.format_decimal(pie_morris[2])]

        # ----------------------variable con datos de meses recientes --------------------------------
        meses_recientes = formatutils.obtener_entity(Recientes, "ultimos")

        # -------------- datos para grafica de echarts y morris ---------------------------------------------
        lista_echarts_punta = list()
        lista_echarts_valle = list()
        lista_echarts_resto = list()
        lista_meses = formatutils.obtener_meses("entero")
        barras_morris = list()

        for elemento in lista_meses:
            lista_echarts_punta.append(formatutils.obtener_month(anterior_year, elemento, "PuntaE"))
            lista_echarts_valle.append(formatutils.obtener_month(anterior_year, elemento, "ValleE"))
            lista_echarts_resto.append(formatutils.obtener_month(anterior_year, elemento, "RestoE"))

            barras_morris.append(
                {"x": str(anterior_year.nombre) + "-" + elemento,
                 "Resto": formatutils.obtener_month(anterior_year, elemento, "RestoD"),
                 "Valle": formatutils.obtener_month(anterior_year, elemento, "ValleD"),
                 "Punta": formatutils.obtener_month(anterior_year, elemento, "PuntaD")})

        # -------------codigo para encontrar  el mes de mayor consumo  en grafica de echarts-------------

        mayor = [max(lista_echarts_punta), max(lista_echarts_valle), max(lista_echarts_resto)]
        orientacion_meses = {1: "Enero", 2: "Febrero", 3: "Marzo", 4: "Abril", 5: "Mayo", 6: "Junio",
                             7: "Julio", 8: "Agosto", 9: "Septiembre", 10: "Octubre", 11: "Noviembre", 12: "Diciembre"}
        posiciones = [orientacion_meses[lista_echarts_punta.index(mayor[0]) + 1],
                      orientacion_meses[lista_echarts_valle.index(mayor[1]) + 1],
                      orientacion_meses[lista_echarts_resto.index(mayor[2]) + 1]]

        echarts_total = [lista_echarts_punta, lista_echarts_valle, lista_echarts_resto]

        # self.response.out.write(barras_morris)
        lista2 = [formatutils.obtener_month(anterior_year, "total", "PuntaD"),
                  formatutils.obtener_month(anterior_year, "total", "ValleD"),
                  formatutils.obtener_month(anterior_year, "total", "RestoD"),
                  formatutils.obtener_month(anterior_year, "total", "PotD")]

        lista2 = [(lista2[0] / (lista2[0] + lista2[1] + lista2[2] + lista2[3]))*100,
                  (lista2[1] / (lista2[0] + lista2[1] + lista2[2] + lista2[3])) * 100,
                  (lista2[2] / (lista2[0] + lista2[1] + lista2[2] + lista2[3])) * 100,
                  (lista2[3] / (lista2[0] + lista2[1] + lista2[2] + lista2[3])) * 100]

        datos = [date_ahora, date_anterior, formatutils.formatcifra(str(valor1)), formatutils.formatcifra(str(valor2))]

        todos_year = YearT.query(YearT.nombre != str(date_ahora)).order(YearT.nombre)
        datos_anuales = list()
        for year in todos_year:
            datos_anuales.append({
                "date": str(year.nombre),
                "potenciaD": formatutils.obtener_month(year, "total", "PotD"),
                "EnergiaT": formatutils.obtener_month(year, "total", "EnergiaT"),
                "EnergiaD": formatutils.obtener_month(year, "total", "EnergiaD"),
                "DineroTT": formatutils.obtener_month(year, "total", "EnergiaD") + formatutils.obtener_month(year,
                                                                                                             "total",
                                                                                                             "PotD")
            })
        self.render("template base.html",
                    echart=echarts_total,
                    datos=datos,
                    lista=lista,
                    aco=acometidas,
                    meses=meses_recientes,
                    posi=posiciones,
                    mayor=mayor,
                    pie=pie_morris,
                    barras=barras_morris,
                    lista2=lista2,
                    datos_anuales=datos_anuales)
