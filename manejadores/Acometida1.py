from utils import renderutils, formatutils
from modelos import Acometida, Usuarios


class AcometidaHandler(renderutils.MainHandler):
    def get(self):
        nombre = str(self.request.cookies.get('nombre'))
        if nombre:
            usuario = formatutils.obtener_entity(Usuarios, nombre)
            if usuario:
                self.render("formularioacometida.html")
        else:
            self.redirect("/login")

    def post(self):
        final = self.request.get("lugar")
        if final:
            final = formatutils.objeto_fecha(final)
        else:
            final = formatutils.objeto_fecha("2150-01-01")

        nu_acometida = Acometida(nombre=self.request.get("nombre"),
                                 final=final,
                                 id=self.request.get("nombre"))

        nu_acometida.put()

        self.redirect(self.request.referer)
