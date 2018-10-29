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
         ciudad = fields.Many2one("hotels_be_bago.city", "City");
         galeriaFotos = fields.Many2many("hotels_be_bago.hotelfotos")
         description = fields.Text()
         roomlist = fields.Many2many("hotels_be_bago.habitacion")
         valoraciones = fields.Selection([('1', '⭐'), ('2', '⭐⭐'), ('3', '⭐⭐⭐'), ('4', '⭐⭐⭐⭐'), ('5', '⭐⭐⭐⭐⭐')])
         listaServicios = fields.Many2many("hotels_be_bago.reserva")

     class habitacion(models.Model):
         _name = 'hotels_be_bago.habitacion'
         #hotel = fields.Many2many("hotels_be_bago.hotel", "Hotel")
         hotel=fields.Many2one("hotels_be_bago.hotel","Hotel");
         name = fields.Char()
         camas = fields.Selection([('1', 'Cama Solitaria'), ('2', 'Cama Matrimonio'), ('3', 'Cama Familiar'), ('4', 'Cama Infantil con matrimonio'), ('5', 'Distribución numerosa')])
         fotos = fields.Many2many("hotels_be_bago.roomfotos")
         precios = fields.Integer(default=20)
         descripcion = fields.Text(default="Una agradable habitación presidencial. Perfecta para descansar y hacer todo tipo de travesuras.")

     class reserva(models.Model):
         _name = 'hotels_be_bago.reserva'
         fechaInicio = fields.Date()
         fechaFinal = fields.Date()
         habitaciones = fields.Many2one("papito.habitacion", "Habitacion a reservar")
         clientes = fields.Many2one("res.partner", "Nombre del cliente")

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








