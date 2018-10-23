# -*- coding: utf-8 -*-

from odoo import models, fields, api

class city(models.Model):

     _name = 'hotels_be_bago.city'
     name = fields.Char()
     description = fields.Text()
     ubication = fields.Char(String="Ubication")
     country = fields.Many2one("res.country", "Pais")
     hotellist = fields.Many2many("hotels_be_bago.hotel")

     class hotel(models.Model):
         _name = 'hotels_be_bago.hotel'
         name = fields.Char()
         galeriaFotos = fields.Many2many("hotels_be_bago.fotos")
         description = fields.Text()
         roomlist = fields.Many2many("hotels_be_bago.habitacion")
         valoraciones = fields.Integer()
         listaServicios = fields.Many2many("hotels_be_bago.reserva")

     class habitacion(models.Model):
         _name = 'hotels_be_bago.habitacion'
         hotel = fields.Many2many("hotels_be_bago.hotel", "Hotel")
         name = fields.Char()
         camas = fields.Integer()
         fotos = fields.Many2many("hotels_be_bago.fotos")
         precios = fields.Integer()
         descripcion = fields.Text()

     class reserva(models.Model):
         _name = 'hotels_be_bago.reserva'
         fechaInicio = fields.Date()
         fechaFinal = fields.Date()
         habitaciones = fields.Many2one("papito.habitacion", "Habitacion a reservar")
         clientes = fields.Many2one("res.partner", "Nombre del cliente")

     class fotos(models.Model):
         _name = 'hotels_be_bago.fotos'
         name = fields.Char("Nombre de la foto")
         foto = fields.Binary("Seleccione una foto para agregar")

     class servicis(models.Model):
         _name = 'hotels_be_bago.servicis'
         name = fields.Char("Nombre del servicio")
         tipo = fields.Selection([('1', 'Higiene personal'), ('2', 'Higiene animal'), ('3', 'Cuidado del vehiculo'),
                                  ('3', 'Cuidado del vehiculo'), ('4', 'Descanso'), ('5', 'Comidas y refrigerios')])
         imageser = fields.Binary("Seleccione una foto para el servicio")