from utils import renderutils
from modelos import Factura


class TablaHandler(renderutils.MainHandler):
    def get(self):
        lista = Factura.query(Factura.Aco_Key == "Agronomia")
        self.render("tabla.html", lista=lista)
