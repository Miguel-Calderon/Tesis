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
import json
# import numpy
from manejadores import Fecha
from modelos import Acometida, Factura,  Pliego
from utils import renderutils




class FrontHandler(renderutils.MainHandler):
    def get(self):
        self.render("formulariofecha.html")

        # def post(self):
        #   facultad = self.request.get("facultad")
        #  year = self.request.get("year")
        #  self.render("prueba3.html",year=year)


class HomeHandler(renderutils.MainHandler):
    def get(self):
        self.render("web-app.html")


class PliegoHandler(renderutils.MainHandler):
    def get(self):
        self.render("formulariopliego.html")

    def post(self):
        cadena = self.request.get("meses_A")
        lista = json.loads(cadena)
        cadena2 = self.request.get("json_T")
        lista2 = json.loads(cadena2)
        nu_pliego = Pliego(pico_T=float(self.request.get("pico_T")),
                           valle_T=float(self.request.get("valle_T")),
                           resto_T=float(self.request.get("resto_T")),
                           potencia_T=float(self.request.get("potencia_T")),
                           json_T=lista2,
                           meses_A=lista)

        nu_pliego.put()
        self.redirect(self.request.referer)


class FacturaHandler(renderutils.MainHandler):
    def get(self):
        self.render("formulariofactura.html")

    def post(self):
        acometida = self.request.get("Acometida")
        nu_factura = Factura(pico_E=float(self.request.get("pico_E")),
                             valle_E=float(self.request.get("valle_E")),
                             resto_E=float(self.request.get("resto_E")),
                             potencia_E=float(self.request.get("potencia_E")),
                             json_E=list(self.request.get("json_E")),
                             pico_D=float(self.request.get("pico_D")),
                             valle_D=float(self.request.get("valle_D")),
                             resto_D=float(self.request.get("resto_D")),
                             potencia_D=float(self.request.get("potencia_D")),
                             json_D=list(self.request.get("json_D")),
                             ftotal=float(self.request.get("ftotal")),
                             nombre=acometida)  # incluir tratamiento de acometida

        nu_factura.put()


class AcometidaHandler(renderutils.MainHandler):
    def get(self):
        self.render("formularioacometida.html")

    def post(self):
        nu_acometida = Acometida(nombre=self.request.get("nombre"),
                                 localizacion=self.request.get("lugar"))

        nu_acometida.put()


app = webapp2.WSGIApplication([
    ('/', FrontHandler),
    ('/home', HomeHandler),
    ('/respuesta', Fecha.FechaHandler),
    ('/pliego', PliegoHandler),
    ('/factura', FacturaHandler),
    ('/acometida', AcometidaHandler)
], debug=True)
