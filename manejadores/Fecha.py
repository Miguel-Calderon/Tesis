from modelos import Fecha
from utils import renderutils


class FechaHandler(renderutils.MainHandler):
    def post(self):
        nu_fecha = Fecha(mes=self.request.get("mes"),
                         year=self.request.get("year"),
                         date=self.request.get("fecha"),
                         id=self.request.get("fecha"))
        # fecha = self.request.get("fecha")
        # mes = self.request.get("mes")
        # year = self.request.get("year")
        # self.response.out.write(fecha)
        # self.response.out.write(mes)
        # self.response.out.write(year)
        # nu_fecha.key = ndb.Key("Fecha", self.request.get("fecha"))
        # fecha_key =
        nu_fecha.put()
        # self.response.out.write()
        self.redirect(self.request.referer)
