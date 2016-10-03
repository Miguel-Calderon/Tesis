from utils import renderutils


class FrontHandler(renderutils.MainHandler):
    def get(self):
        # todas = Acometida.query()
        # self.render("wizardfactura.html", todas=todas)
        mes = "Enero"
        self.render("template base.html", mes=mes)
        # def post(self):
        #   facultad = self.request.get("facultad")
        #  year = self.request.get("year")
        #  self.render("prueba3.html",year=year)
