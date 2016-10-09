from utils import renderutils, formatutils
from modelos import Usuarios


class LogInHandler(renderutils.MainHandler):
    def get(self):
        nombre = self.request.cookies.get('nombre')
        self.render("signup.html", usuario=nombre)

    def post(self):
        nombre = str(self.request.get("nombre"))
        contra = str(self.request.get("contra"))

        if (nombre == "iniciar") and (contra == "admin"):
            formatutils.iniciar_usuario()

        usuario = formatutils.obtener_entity(Usuarios, nombre)
        if not usuario:
            self.render("signup.html")
        else:
            if usuario.contra == contra:
                self.response.set_cookie(key="nombre", value=nombre)
                self.redirect("/fecha")


class LogOutHandler(renderutils.MainHandler):
    def get(self):
        self.response.set_cookie(key="nombre", value="")
        self.redirect("/login")
