# -*- coding: utf-8 -*-

from odoo import models, fields, api,tools
import random
#ver la importación de tools de odoo, arriba importada
from odoo.exceptions import ValidationError
import logging
#from datetime import datetime, timedelta
import datetime




_logger = logging.getLogger(__name__)


class city(models.Model):
    _name = 'hotels_be_bago.city'
    name = fields.Char()
    description = fields.Text()
    ubication = fields.Char(String="Ubication")
    country = fields.Many2one("res.country", "Pais")
    hotellist = fields.One2many("hotels_be_bago.hotel","ciudad")

class hotel(models.Model):
    _name = 'hotels_be_bago.hotel'
    name = fields.Char()
    galeriaFotos = fields.Many2many("hotels_be_bago.hotelfotos")
    fotoprincipal=fields.Binary(compute='_recuperar_foto',store=True)
    description = fields.Text()
    ciudad=fields.Many2one("hotels_be_bago.city","Ciudad")
    pais=fields.Char(string='Pais del hotel',related='ciudad.country.name')
    roomlist=fields.One2many("hotels_be_bago.habitacion","hotel")
    estrellas = fields.Selection([('1', '⭐'), ('2', '⭐⭐'), ('3', '⭐⭐⭐'), ('4', '⭐⭐⭐⭐'), ('5', '⭐⭐⭐⭐⭐')])
    valoraciomedia=fields.Selection([('1', '⭐'), ('2', '⭐⭐'), ('3', '⭐⭐⭐'), ('4', '⭐⭐⭐⭐'), ('5', '⭐⭐⭐⭐⭐')],compute='_calcular_media',store=True)
    listaServicios = fields.Many2many("hotels_be_bago.servicis")
    comentarios = fields.One2many('hotels_be_bago.comentarios','hoteles')

    @api.depends('comentarios')
    def _calcular_media(self):
        for record in self:

            #print(str(record.name + "tiene "+ str(len(record.comentarios))))
            if len(record.comentarios) > 0:
                arrayComentarios=record.comentarios
                sumaValoracion=0
                media=0
                i=0
                for comentario in arrayComentarios:
                    sumaValoracion=int(sumaValoracion)+int(comentario.valoracion)
                    i=i+1
                media=sumaValoracion/i
                record.valoraciomedia=str(int(media))
            else:
                print("No tiene comentarios por lo que la media se queda en default,1")
                record.valoraciomedia='1'

    @api.depends('galeriaFotos')
    def _recuperar_foto(self):
        for record in self:
            if len(record.galeriaFotos) > 0:
               record.fotoprincipal=record.galeriaFotos[0].foto
            else:
                print("Este hotel no tiene fotos...")
    @api.one
    def anyadir_comentario(self):
        reserva=self.env['hotels_be_bago.reserva'].search([('habitaciones.hotel','=',self.id),('fechaFinal','<=',str(datetime.datetime.today()))])
        #el self.env se usa para recuperar una tabla de la bbdd
        #el search es como usn elect
        comentarios=['Me lo he pasado bien','Buenos efectos audivisuales y atencion al cliente','El baño me ha puesto nervioso', 'J**** donde m***** me he metido tio',"Tocará volver"]
        cliente={'clientes':reserva[random.randint(0,len(reserva)-1)].clientes.id,'fotocliente':'','hoteles':self.id,'descripcion':comentarios[random.randint(0,len(comentarios)-1)],'valoracion':str(random.randint(1,5))}
        self.env['hotels_be_bago.comentarios'].create(cliente)

    @api.one
    def anyadir_habitacion(self):
        hotel=self.env['hotels_be_bago.hotel'].search([('id','=',self.id)])
        name="Habitacion " + str(hotel.name) + str(random.randint(1,1000))
        camas=str(random.randint(1,5))
        precios=random.randint(100,1000)
        fotos=self.env['hotels_be_bago.roomfotos'].search([('id','=',random.choice([self.env.ref('hotels_be_bago.roomfoto1').id,self.env.ref('hotels_be_bago.roomfoto2').id,self.env.ref('hotels_be_bago.roomfoto3').id,self.env.ref('hotels_be_bago.roomfoto4').id,self.env.ref('hotels_be_bago.roomfoto5').id]))])
        
        habitacion={'hotel':hotel.id,'name':name,'camas':camas,'precios':precios,'fotos':[(6,0,fotos.ids)]}
        hotel.roomlist.create(habitacion)
        #print(habitacion)


class habitacion(models.Model):
    _name = 'hotels_be_bago.habitacion'
    hotel = fields.Many2one("hotels_be_bago.hotel", "Hotel")
    name = fields.Text()
    camas = fields.Selection([('1', 'Cama Solitaria'), ('2', 'Cama Matrimonio'), ('3', 'Cama Familiar'),
                                  ('4', 'Cama Infantil con matrimonio'), ('5', 'Distribución numerosa')])
    fotoprincipalRoom = fields.Binary(compute='_recuperar_foto_rooms', store=True)
    fotos = fields.Many2many("hotels_be_bago.roomfotos" , store=True)
    precios = fields.Integer(default=20)
    reserva=fields.One2many("hotels_be_bago.reserva","habitaciones")
    disponibilidad=fields.Char(string="Estado",compute='_getestado',readOnly=True)
    descripcion = fields.Text(
            default="Una agradable habitación presidencial. Perfecta para descansar y hacer todo tipo de travesuras.")

    @api.depends('fotos')
    def _recuperar_foto_rooms(self):
        for record in self:
            if len(record.fotos) > 0:
                record.fotoprincipalRoom = record.fotos[0].foto
            else:
                print("Este room no tiene fotos...")

    @api.depends('reserva')
    def _getestado(self):
        for record in self:
            #print(len(record.reserva))
            if(len(record.reserva)>0):
                for valorreserva in record.reserva:
                    if(valorreserva.fechaFinal < str(datetime.datetime.today())):
                        record.disponibilidad="Libre"
                    else:
                        record.disponibilidad="Ocupado"
            else:
                record.disponibilidad="Libre"



class reserva(models.Model):
    _name = 'hotels_be_bago.reserva'
    name=fields.Char(string="Nombre de la reserva",compute='_generar_nombre',readonly=False)
    fechaInicio = fields.Date()
    fechaFinal = fields.Date()
    habitaciones = fields.Many2one("hotels_be_bago.habitacion", "Habitacion a reservar")
    clientes = fields.Many2one("res.partner", "Nombre del cliente")
    nombrehotel = fields.Many2one(string='Nombre del hotel', related='habitaciones.hotel', readonly=False, store=True)

    @api.multi
    @api.depends('habitaciones','fechaInicio','fechaFinal','clientes')
    def _generar_nombre(self):
        for record in self:
            if record.habitaciones and record.fechaInicio and record.fechaFinal and record.clientes:
                    record.name=record.habitaciones.name+' '+record.clientes.name+' '+record.fechaInicio+' '+record.fechaFinal

    @api.onchange('fechaInicio','fechaFinal')
    def _manyana(self):
        for record in self:
            if record.fechaFinal and record.fechaInicio:

                fmt='%Y-%m-%d'
                dateInicio=datetime.datetime.strptime(str(record.fechaInicio),fmt)
                dateFinal=datetime.datetime.strptime(str(record.fechaFinal),fmt)
                if dateFinal < dateInicio:
                    record.fechaFinal = dateInicio + datetime.timedelta(days=1)
                    print(record.fechaFinal)
                    return {
                        'warning': {
                            'title': "Algo ha ocurrido mal",
                            'message': "No puedes insertar un dia antes de la fecha de inicio",
                        }
                    }
                else:
                    print(" No hay error!")


            elif record.fechaInicio:
                fmt = '%Y-%m-%d'
                data = datetime.datetime.strptime(str(record.fechaInicio), fmt)
                record.fechaFinal = data + datetime.timedelta(days=1)


               # print(data)

    @api.constrains('fechaInicio', 'fechaFinal')
    def _comprobar_reserva(self):
        for record in self:
            variable = self.search_count([('id', '!=', record.id), ('fechaFinal', '>=', record.fechaInicio), ('fechaInicio','<=', record.fechaFinal)])
            variable2=self.search([('id', '!=', record.id), ('fechaFinal', '>=', record.fechaInicio), ('fechaInicio','<=', record.fechaFinal)])
            for valor in variable2:
                print(self.name)
                print(valor.name)

            if variable > 0:
                raise ValidationError("Se solapan dos habitaciones \n" + self.name + " con  \n"+valor.name)




class hotelfotos(models.Model):
    _name = 'hotels_be_bago.hotelfotos'
    name = fields.Char("Nombre de la foto")
    foto = fields.Binary("Seleccione una foto para agregar")

class roomfotos(models.Model):
    _name = 'hotels_be_bago.roomfotos'
    name = fields.Char("Nombre de la foto")
    foto = fields.Binary("Seleccione una foto para agregar")

class servicis(models.Model):
    _name = 'hotels_be_bago.servicis'
    name = fields.Char("Nombre del servicio")
    tipo = fields.Selection([('1', 'Higiene personal'), ('2', 'Higiene animal'), ('3', 'Cuidado del vehiculo'),
                                 ('4', 'Descanso'), ('5', 'Comidas y refrigerios')])
    imageser = fields.Binary("Seleccione una foto para el servicio")

class comentarios(models.Model):
    _name='hotels_be_bago.comentarios'
    clientes = fields.Many2one("res.partner", "Nombre del cliente")
    fotocliente=fields.Binary(related='clientes.image',store=True)
    namecliente = fields.Char(related='clientes.name')
    hoteles=fields.Many2one('hotels_be_bago.hotel','Hotel')
    descripcion=fields.Text(string="Descripcion")
    valoracion = fields.Selection([('1', '⭐'), ('2', '⭐⭐'), ('3', '⭐⭐⭐'), ('4', '⭐⭐⭐⭐'), ('5', '⭐⭐⭐⭐⭐')],default='5')


