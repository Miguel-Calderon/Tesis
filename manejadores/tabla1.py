from utils import renderutils, formatutils


class TablaHandler(renderutils.MainHandler):
    def get(self):
        self.render("tabla.html")
