from utils import renderutils, formatutils
from modelos import YearT
import datetime


class GraficaHandler(renderutils.MainHandler):
    def get(self):
        primer_year = formatutils.obtener_entity(YearT, 2004)
        # busca en la base de datos  la entity perteneciente al 2004
        resultado = formatutils.obtener_year(primer_year, "EnergiaT")
        resultadoD = formatutils.obtener_year(primer_year, "EnergiaD")
        date_ahora = datetime.date.today().year
        segundo_year = formatutils.obtener_entity(YearT, date_ahora)
        # resultado2 = formatutils.obtener_year(segundo_year, "Energia")

        orientacion = formatutils.obtener_meses("cadena")

        datos1 = list()
        for elemento in orientacion:
            datos1.append({
                "mes": elemento,
                "year1": resultado[elemento],
                # "year2": resultado2[elemento],
                "year3": resultado[elemento],
                "year4": resultado[elemento]
            })

        datos2 = list()
        for elemento in orientacion:
            datos2.append({
                "mes": elemento,
                "year1": resultadoD[elemento],
                # "year2": resultado2[elemento],
                "year3": resultadoD[elemento],
                "year4": resultadoD[elemento]
            })
        orientacion2 = formatutils.obtener_meses("entero")
        todos_year = YearT.query().order(YearT.nombre)
        datos3 = list()
        for year in todos_year:
            for mes in orientacion2:
                datos3.append({
                    "date": str(year.nombre) + "-" + mes,
                    "potenciaD": formatutils.obtener_month(year, mes, "PotD"),
                    "EnergiaT": formatutils.obtener_month(year, mes, "EnergiaT"),
                    "EnergiaD": formatutils.obtener_month(year, mes, "EnergiaD"),
                    "DineroTT": formatutils.obtener_month(year, mes, "EnergiaD") + formatutils.obtener_month(year, mes,
                                                                                                             "PotD")
                })

        datos = [{
            "mes": "Enero",
            "year1": 3.1,
            "year2005": 4.2,
            "year2006": 3.5,
            "year2007": 4.2
        }, {
            "mes": "Febrero",
            "year1": 1.7,
            "year2005": 3.1,
            "year2006": 3.5,
            "year2007": 4.2
        }, {
            "mes": "Marzo",
            "year1": 2.8,
            "year2005": 2.9,
            "year2006": 3.5,
            "year2007": 4.2
        }, {
            "mes": "Abril",
            "year1": 2.6,
            "year2005": 2.3,
            "year2006": 3.5,
            "year2007": 4.2
        }, {
            "mes": "Mayo",
            "year1": 1.4,
            "year2005": 2.1,
            "year2006": 3.5,
            "year2007": 4.2
        }, {
            "mes": "Julio",
            "year1": 2.6,
            "year2005": 4.9,
            "year2006": 3.5,
            "year2007": 4.2
        }, {
            "mes": "Agosto",
            "year1": 1.7,
            "year2005": 3.1,
            "year2006": 3.5,
            "year2007": 4.2
        }, {
            "mes": "Septiembre",
            "year1": 2.8,
            "year2005": 2.9,
            "year2006": 3.5,
            "year2007": 4.2
        }, {
            "mes": "Octubre",
            "year1": 2.6,
            "year2005": 2.3,
            "year2006": 3.5,
            "year2007": 4.2
        }, {
            "mes": "Noviembre",
            "year1": 1.4,
            "year2005": 2.1,
            "year2006": 3.5,
            "year2007": 4.2
        }, {
            "mes": "Diciembre",
            "year1": 2.6,
            "year2005": 4.9,
            "year2006": 3.5,
            "year2007": 4.2
        }]

        titulo = ["2005", "2006", "2007"]
        self.render("graficas.html", datos=datos, titulo=titulo, datos3=datos3)
        # self.response.out.write(datos3)
