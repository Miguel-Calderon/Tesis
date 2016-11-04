#!/usr/bin/env python
#
# Copyright 2007 Google Inc.
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import webapp2

from manejadores import Fecha, Factura1, Pliego1, Graficas1, tabla1, Front1, Login, Acometida1
from utils import renderutils, formatutils
# from modelos import YearT


class HomeHandler(renderutils.MainHandler):
    def get(self):
        self.render("formularioyear.html")

    """def post(self):
        Energia_Total = float(self.request.get("text"))
        Costo_Energia = float(self.request.get("text1"))
        Punta_Energia = float(self.request.get("text2"))
        Punta_Dinero = float(self.request.get("text3"))
        Valle_Energia = float(self.request.get("text4"))
        Valle_Dinero = float(self.request.get("text5"))
        Resto_Energia = float(self.request.get("text6"))
        Resto_Dinero = float(self.request.get("text7"))
        Potencia_E = float(self.request.get("text8"))
        Potencia_Dinero = float(self.request.get("text9"))
        nombre = self.request.get("name")
        seleccion = str(self.request.get("select"))

        lista = [Energia_Total, Costo_Energia, Punta_Energia, Punta_Dinero, 0.0, Valle_Energia, Valle_Dinero, 0.0,
                 Resto_Energia, Resto_Dinero, 0.0, Potencia_E, Potencia_Dinero, 0.0]

        lista2 = [0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0, 0.0]

        year_entity = formatutils.obtener_entity(YearT, int(nombre))

        if not year_entity:
            year_entity = YearT(id=int(nombre),
                                nombre=nombre,
                                Enero=lista2,
                                Febrero=lista2,
                                Marzo=lista2,
                                Abril=lista2,
                                Mayo=lista2,
                                Junio=lista2,
                                Julio=lista2,
                                Agosto=lista2,
                                Septiembre=lista2,
                                Octubre=lista2,
                                Noviembre=lista2,
                                Diciembre=lista2,
                                Total_anual=lista2)

        if seleccion == "enero":
            year_entity.Enero = lista
        elif seleccion == "febrero":
            year_entity.Febrero = lista
        elif seleccion == "marzo":
            year_entity.Marzo = lista
        elif seleccion == "abril":
            year_entity.Abril = lista
        elif seleccion == "mayo":
            year_entity.Mayo = lista
        elif seleccion == "junio":
            year_entity.Junio = lista
        elif seleccion == "julio":
            year_entity.Julio = lista
        elif seleccion == "agosto":
            year_entity.Agosto = lista
        elif seleccion == "septiembre":
            year_entity.Septiembre = lista
        elif seleccion == "octubre":
            year_entity.Octubre = lista
        elif seleccion == "noviembre":
            year_entity.Noviembre = lista
        elif seleccion == "diciembre":
            year_entity.Diciembre = lista
        elif seleccion == "total":
            year_entity.Total_anual = lista

        year_entity.put()
        self.redirect(self.request.referer)"""

app = webapp2.WSGIApplication([
    ('/', Front1.FrontHandler),
    ('/home', HomeHandler),
    ('/fecha', Fecha.FechaHandler),
    ('/pliego', Pliego1.PliegoHandler),
    ('/factura', Factura1.FacturaHandler),
    ('/acometida', Acometida1.AcometidaHandler),
    ('/graficas', Graficas1.GraficaHandler),
    ('/tabla', tabla1.TablaMenuHandler),
    ('/login', Login.LogInHandler),
    ('/logout', Login.LogOutHandler)
], debug=True)
