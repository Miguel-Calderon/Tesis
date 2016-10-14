from utils import renderutils
from modelos import Factura, Pliego


class TablaMenuHandler(renderutils.MainHandler):
    def get(self):
        self.render("menutabla.html")

    def post(self):
        acometida = str(self.request.get("seleccion"))
        orientacion = {"Agronomia": Factura.query(Factura.Aco_Key == "Agronomia"),
                       "Complejo_Deportivo": Factura.query(Factura.Aco_Key == "Complejo_Deportivo"),
                       "Humanidades": Factura.query(Factura.Aco_Key == "Humanidades"),
                       "Derecho": Factura.query(Factura.Aco_Key == "Derecho"),
                       "Fosa": Factura.query(Factura.Aco_Key == "Fosa"),
                       "Medicina": Factura.query(Factura.Aco_Key == "Medicina")}

        if acometida =="Pliego_Tarifario":
            pliegotarifa = Pliego.query().order(Pliego.inicio_p)
            self.render("tablap.html", lista=pliegotarifa)
        else:
            self.render("tabla.html", lista=orientacion[acometida], acometida=acometida)
