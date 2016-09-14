import jinja2
import os
import webapp2

template_dir = os.path.join(os.path.dirname(__file__), '..', 'templates')
jinja_env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_dir), autoescape=True)


class MainHandler(webapp2.RequestHandler):
    def write(self, *a, **kw):
        self.response.out.write(*a, **kw)

    @staticmethod
    def render_str(template, **params):
        t = jinja_env.get_template(template)
        return t.render(params)

    def render(self, template, **kw):
        self.write(self.render_str(template, **kw))

    def obtener_valores_punta(self, toda):
        punta_E = float(self.request.get(toda.nombre+"_punta"))
        punta_D = float(self.request.get(toda.nombre + "_puntad"))
        # en la lista se almacena primero la energia, luego el dinero y por ultimo el valor calculado
        punta_L = [punta_E, punta_D, 0]
        return punta_L

    def obtener_valores_valle(self, toda):
        valle_E = float(self.request.get(toda.nombre+"_valle"))
        valle_D = float(self.request.get(toda.nombre + "_valled"))
        # en la lista se almacena primero la energia, luego el dinero y por ultimo el valor calculado
        valle_L = [valle_E, valle_D, 0]
        return valle_L

    def obtener_valores_resto(self, toda):
        resto_E = float(self.request.get(toda.nombre+"_resto"))
        resto_D = float(self.request.get(toda.nombre + "_restod"))
        # en la lista se almacena primero la energia, luego el dinero y por ultimo el valor calculado
        resto_L = [resto_E, resto_D, 0]
        return resto_L

    def obtener_valores_pot(self, toda):
        potencia = float(self.request.get(toda.nombre+"_potencia"))
        potencia_D = float(self.request.get(toda.nombre+"_potenciad"))
        # en la lista se almacena primero la energia, luego el dinero y por ultimo el valor calculado
        potencia_L = [potencia, potencia_D, 0]
        return potencia_L

    def obtener_fp_tr(self, toda):
        factor_potencia = float(self.request.get(toda.nombre+"_fp"))
        trafo = float(self.request.get(toda.nombre+"trafo"))
        lista = [factor_potencia, trafo]
        return lista
