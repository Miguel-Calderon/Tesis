from modelos import Fecha, Acometida, Factura
from utils import renderutils, formatutils
from google.appengine.ext import ndb


class FacturaHandler(renderutils.MainHandler):
    def get(self):
        # todas = Acometida.query()
        fecha = formatutils.obtener_entity(Fecha, "2004-01")
        self.response.out.write(fecha.mes)
        # for toda in todas:
        #   self.response.out.write(toda.key)
        #   self.render("formulariofactura.html")

    def post(self):

        fecha_key = ndb.Key(Fecha, self.request.get("fecha"))
        fecha = fecha_key.get()
        todas = Acometida.query()
        total_mes = [0, 0, 0, 0, 0, 0]

        for toda in todas:
            pico_L = self.obtener_valores_pico(toda)
            valle_L = self.obtener_valores_valle(toda)
            resto_L = self.obtener_valores_resto(toda)
            pot_L = self.obtener_valores_pot(toda)
            total_aco = formatutils.total_acometida(pico_L, valle_L, resto_L, pot_L)
            total_mes = formatutils.total_mes(total_aco, total_mes)
            acometida_key = ndb.Key(Acometida, toda.nombre)
            acometida_id = self.request.get("fecha")+toda.nombre
            nu_factura = Factura(Fecha_Key=fecha_key,
                                 Aco_Key=acometida_key,
                                 id=acometida_id,
                                 Pico_Lista=pico_L,
                                 Valle_Lista=valle_L,
                                 Resto_Lista=resto_L,
                                 Potencia_Lista=pot_L,
                                 ftotal=total_aco)
            nu_factura.put()

        self.response.out.write(total_mes)
        # acometida = self.request.get("Acometida")
        # nu_factura = Factura(pico_E=float(self.request.get("pico_E")),
                             # valle_E=float(self.request.get("valle_E")),
                             # resto_E=float(self.request.get("resto_E")),
                             # potencia_E=float(self.request.get("potencia_E")),
                             # json_E=list(self.request.get("json_E")),
                             # pico_D=float(self.request.get("pico_D")),
                             # valle_D=float(self.request.get("valle_D")),
                             # resto_D=float(self.request.get("resto_D")),
                             # potencia_D=float(self.request.get("potencia_D")),
                             # json_D=list(self.request.get("json_D")),
                             # ftotal=float(self.request.get("ftotal")),
                             # nombre=acometida)  # incluir tratamiento de acometida


