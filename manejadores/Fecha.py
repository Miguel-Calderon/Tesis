from modelos import Fecha, Acometida
from utils import renderutils, formatutils


class FechaHandler(renderutils.MainHandler):
    def get(self):
        self.render("formulariofecha.html")

    def post(self):
        fecha = self.request.get("fecha")
        nu_fecha = Fecha(inicio=formatutils.objeto_fecha(self.request.get("inicio")),
                         fin=formatutils.objeto_fecha(self.request.get("final")),
                         mes=fecha,
                         id=fecha)
        # fecha = self.request.get("fecha")
        # mes = self.request.get("mes")
        # year = self.request.get("year")
        # self.response.out.write(fecha)
        # self.response.out.write(mes)
        # self.response.out.write(year)
        # nu_fecha.key = ndb.Key("Fecha", self.request.get("fecha"))
        # fecha_key =
        # nu_fecha.put()
        # self.response.out.write()
        todas = Acometida.query()
        self.render("wizardfactura.html", todas=todas, temp_fecha=fecha)
        #self.render("formulariopliego.html", temp_fecha=fecha)




#   mes={1:"Enero",
#        2:"Febrero",
#        3:"Marzo",
#        4:"Abril",
#        5:"Mayo",
#        6:"Junio",
#        7:"Julio",
#            }
#
#
#   mes[entra digito y devuelve cadena equivalente del diccionario]
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
#
