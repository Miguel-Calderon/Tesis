from modelos import Fecha, Acometida, Usuarios
from utils import renderutils, formatutils


class FechaHandler(renderutils.MainHandler):
    def get(self):
        nombre = str(self.request.cookies.get('nombre'))
        if nombre:
            usuario = formatutils.obtener_entity(Usuarios, nombre)
            if usuario:
                self.render("formulariofecha.html")
        else:
            self.redirect("/login")

    def post(self):
        fecha = self.request.get("fecha")
        nu_fecha = Fecha(inicio=formatutils.objeto_fecha(self.request.get("inicio")),
                         fin=formatutils.objeto_fecha(self.request.get("final")),
                         mes=fecha,
                         id=fecha)

        nu_fecha.put()

        todas = Acometida.query()
        self.render("wizardfactura.html", todas=todas, temp_fecha=fecha)
