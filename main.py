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


from manejadores import Fecha, Factura1, Pliego1
from modelos import Acometida, Factura,  Pliego
from utils import renderutils, formatutils


class FrontHandler(renderutils.MainHandler):
    def get(self):
        todas = Acometida.query()
        self.render("wizardfactura.html", todas=todas)

        # def post(self):
        #   facultad = self.request.get("facultad")
        #  year = self.request.get("year")
        #  self.render("prueba3.html",year=year)


class HomeHandler(renderutils.MainHandler):
    def get(self):
        self.render("web-app.html")




class AcometidaHandler(renderutils.MainHandler):
    def get(self):
        self.render("formularioacometida.html")

    def post(self):
        nu_acometida = Acometida(nombre=self.request.get("nombre"),
                                 localizacion=self.request.get("lugar"),
                                 id=self.request.get("nombre"))

        nu_acometida.put()

        self.redirect(self.request.referer)


app = webapp2.WSGIApplication([
    ('/', FrontHandler),
    ('/home', HomeHandler),
    ('/fecha', Fecha.FechaHandler),
    ('/pliego', Pliego1.PliegoHandler),
    ('/factura', Factura1.FacturaHandler),
    ('/acometida', AcometidaHandler)
], debug=True)
