from modelos import Fecha, Acometida, Factura, YearT
from utils import renderutils, formatutils
from google.appengine.ext import ndb


class FacturaHandler(renderutils.MainHandler):
    # def get(self):
        # todas = Acometida.query()
        # fecha = formatutils.obtener_entity(Fecha, "2004-04")
        # truck = formatutils.obtener_entity(YearT, 2015)
        # resultado = formatutils.calculo_costo(fecha, [99, 1.0, 0.0], "punta")
        #self.response.out.write(truck)
        # self.response.out.write(fecha.mes)
        # for toda in todas:
        #   self.response.out.write(toda.key)
        #   self.render("formulariofactura.html")

    def post(self):

        fecha_key = ndb.Key(Fecha, self.request.get("fecha"))
        fecha = fecha_key.get()
        todas = Acometida.query(Acometida.final > fecha.fin)
        total_mes = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

        for toda in todas:
            # en la lista se almacena primero la energia, luego el dinero y por ultimo el valor calculado
            punta = self.obtener_valores_punta(toda)
            valle = self.obtener_valores_valle(toda)
            resto = self.obtener_valores_resto(toda)
            potencia = self.obtener_valores_pot(toda)
            fp_tr = self.obtener_fp_tr(toda)
            # **********************************************************************************
            # se coloca en las listas el dato calculado
            punta_L = formatutils.calculo_costo(fecha, punta, "punta")
            valle_L = formatutils.calculo_costo(fecha, valle, "valle")
            resto_L = formatutils.calculo_costo(fecha, resto, "resto")
            pot_L = formatutils.calculo_costo(fecha, potencia, "potencia")
            # **********************************************************************************
            total_aco = formatutils.total_acometida(punta_L, valle_L, resto_L, pot_L)
            # suma_total= [kw/h total, $ eneria total, punta[Energia,Dinero,Calculo], valle[Energia,Dinero,Calculo],
            #              resto[Energia,Dinero,calculo], potencia[kw, $pot, #calculado]]
            total_guardar = [total_aco[0], total_aco[1], pot_L[0], pot_L[1]]
            total_mes = formatutils.total_mes(total_aco, total_mes)
            # acometida_key = ndb.Key(Acometida, toda.nombre)
            acometida_id = self.request.get("fecha")+toda.nombre
            nu_factura = Factura(Fecha_Key=self.request.get("fecha"),
                                 Fecha_dt=fecha.inicio,
                                 Aco_Key=toda.nombre,
                                 id=acometida_id,
                                 Punta_Lista=punta_L,
                                 Valle_Lista=valle_L,
                                 Resto_Lista=resto_L,
                                 Potencia_Lista=pot_L,
                                 ftotal=total_guardar,
                                 f_pot_tr=fp_tr)
            nu_factura.put()

        recientes = formatutils.meses_recientes(fecha.inicio, total_mes)
        recientes.put()

        year_entity = formatutils.obtener_entity(YearT, fecha.inicio.year)
        if year_entity:
            new_entity = formatutils.actualizar_year(fecha.inicio, total_mes, year_entity)
            new_entity.put()
            self.redirect(self.request.referer)
        else:
            year_entity = formatutils.crear_year(fecha.inicio, total_mes)
            year_entity.put()
            self.redirect(self.request.referer)
