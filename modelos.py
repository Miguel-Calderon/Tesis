from google.appengine.ext import ndb


class Fecha(ndb.Model):
    mes = ndb.StringProperty()
    inicio = ndb.DateProperty()
    fin = ndb.DateProperty()
    

class Acometida(ndb.Model):
    nombre = ndb.StringProperty()
    localizacion = ndb.StringProperty()


class Factura(ndb.Model):
    Fecha_Key = ndb.KeyProperty()
    Pliego_A = ndb.KeyProperty()
    Aco_Key = ndb.KeyProperty()
    Punta_Lista = ndb.FloatProperty('P', repeated=True)
    Valle_Lista = ndb.FloatProperty('V', repeated=True)
    Resto_Lista = ndb.FloatProperty('R', repeated=True)
    Potencia_Lista = ndb.FloatProperty('Po', repeated=True)
    ftotal = ndb.FloatProperty('F', repeated=True)
    f_pot_tr = ndb.FloatProperty('FP', repeated=True)
    # pico_E = ndb.FloatProperty()
    # valle_E = ndb.FloatProperty()
    # resto_E = ndb.FloatProperty()
    # potencia_E = ndb.FloatProperty()
    # pico_D = ndb.FloatProperty()
    # valle_D = ndb.FloatProperty()
    # resto_D = ndb.FloatProperty()
    # potencia_D = ndb.FloatProperty()
    # pico_C = ndb.FloatProperty()
    # valle_C = ndb.FloatProperty()
    # resto_C = ndb.FloatProperty()
    # potencia_C = ndb.FloatProperty()


class Pliego(ndb.Model):
    punta_T = ndb.FloatProperty()
    valle_T = ndb.FloatProperty()
    resto_T = ndb.FloatProperty()
    potencia_T = ndb.FloatProperty()
    # el final del pliego es la fecha que inicia el proximo
    inicio_p = ndb.DateProperty()
    final_p = ndb.DateProperty()


class YearT(ndb.Model):
    nombre = ndb.StringProperty()
    Enero = ndb.FloatProperty('E', repeated=True)
    Febrero = ndb.FloatProperty('F', repeated=True)
    Marzo = ndb.FloatProperty('MR', repeated=True)
    Abril = ndb.FloatProperty('AB', repeated=True)
    Mayo = ndb.FloatProperty('MY', repeated=True)
    Junio = ndb.FloatProperty('JN', repeated=True)
    Julio = ndb.FloatProperty('JL', repeated=True)
    Agosto = ndb.FloatProperty('AG', repeated=True)
    Septiembre = ndb.FloatProperty('S', repeated=True)
    Octubre = ndb.FloatProperty('O', repeated=True)
    Noviembre = ndb.FloatProperty('N', repeated=True)
    Diciembre = ndb.FloatProperty('D', repeated=True)
    Total_anual = ndb.FloatProperty('T', repeated=True)