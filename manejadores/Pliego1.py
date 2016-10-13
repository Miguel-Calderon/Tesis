from modelos import Pliego, Usuarios
from utils import renderutils, formatutils


class PliegoHandler(renderutils.MainHandler):

    def get(self):
        nombre = str(self.request.cookies.get('nombre'))
        if nombre:
            usuario = formatutils.obtener_entity(Usuarios, nombre)
            if usuario:
                self.render("formulariopliego.html")
            else:
                self.redirect("/login")
        else:
            self.redirect("/login")

    def post(self):

        nu_pliego = Pliego(punta_T=float(self.request.get("punta_T")),
                           valle_T=float(self.request.get("valle_T")),
                           resto_T=float(self.request.get("resto_T")),
                           potencia_T=float(self.request.get("potencia_T")),
                           inicio_p=formatutils.objeto_fecha(self.request.get("inicio")),
                           final_p=formatutils.objeto_fecha(self.request.get("final")),
                           id=self.request.get("inicio")+"_"+self.request.get("final"))

        nu_pliego.put()
        self.redirect(self.request.referer)
