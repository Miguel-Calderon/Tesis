from modelos import Factura
from utils import renderutils


class FacturaHandler(renderutils.MainHandler):
    def get(self):
        self.render("formulariofactura.html")

    def post(self):
        acometida = self.request.get("Acometida")
        nu_factura = Factura(pico_E=float(self.request.get("pico_E")),
                             valle_E=float(self.request.get("valle_E")),
                             resto_E=float(self.request.get("resto_E")),
                             potencia_E=float(self.request.get("potencia_E")),
                             json_E=list(self.request.get("json_E")),
                             pico_D=float(self.request.get("pico_D")),
                             valle_D=float(self.request.get("valle_D")),
                             resto_D=float(self.request.get("resto_D")),
                             potencia_D=float(self.request.get("potencia_D")),
                             json_D=list(self.request.get("json_D")),
                             ftotal=float(self.request.get("ftotal")),
                             nombre=acometida)  # incluir tratamiento de acometida

        nu_factura.put()
