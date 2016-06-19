from google.appengine.ext import ndb


class Fecha(ndb.Model):
    mes = ndb.StringProperty()
    inicio = ndb.DateProperty()
    fin = ndb.DateProperty()
    

class Acometida(ndb.Model):
    nombre = ndb.StringProperty()
    localizacion = ndb.StringProperty()


class Factura(ndb.Model):
    nombre = ndb.StringProperty()
    pico_E = ndb.FloatProperty()
    valle_E = ndb.FloatProperty()
    resto_E = ndb.FloatProperty()
    potencia_E = ndb.FloatProperty()
    json_E = ndb.JsonProperty()
    pico_D = ndb.FloatProperty()
    valle_D = ndb.FloatProperty()
    resto_D = ndb.FloatProperty()
    potencia_D = ndb.FloatProperty()
    json_D = ndb.JsonProperty()
    ftotal = ndb.FloatProperty()
    fecha_I = ndb.IntegerProperty()


class Pliego(ndb.Model):
    pico_T = ndb.FloatProperty()
    valle_T = ndb.FloatProperty()
    resto_T = ndb.FloatProperty()
    potencia_T = ndb.FloatProperty()
    json_T = ndb.FloatProperty(repeated=True)
    meses_A = ndb.IntegerProperty(repeated=True)



