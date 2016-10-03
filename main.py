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
from manejadores import Fecha, Factura1, Pliego1, Graficas1, tabla1, Front1
from modelos import Acometida
from utils import renderutils


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
    ('/', Front1.FrontHandler),
    ('/home', HomeHandler),
    ('/fecha', Fecha.FechaHandler),
    ('/pliego', Pliego1.PliegoHandler),
    ('/factura', Factura1.FacturaHandler),
    ('/acometida', AcometidaHandler),
    ('/graficas', Graficas1.GraficaHandler),
    ('/tabla', tabla1.TablaHandler)
], debug=True)
