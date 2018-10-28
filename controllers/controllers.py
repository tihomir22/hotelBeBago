# -*- coding: utf-8 -*-
from odoo import http

# class HotelsBeBago(http.Controller):
#     @http.route('/hotels_be_bago/hotels_be_bago/', auth='public')
#     def index(self, **kw):
#         return "Hello, world"

#     @http.route('/hotels_be_bago/hotels_be_bago/objects/', auth='public')
#     def list(self, **kw):
#         return http.request.render('hotels_be_bago.listing', {
#             'root': '/hotels_be_bago/hotels_be_bago',
#             'objects': http.request.env['hotels_be_bago.hotels_be_bago'].search([]),
#         })

#     @http.route('/hotels_be_bago/hotels_be_bago/objects/<model("hotels_be_bago.hotels_be_bago"):obj>/', auth='public')
#     def object(self, obj, **kw):
#         return http.request.render('hotels_be_bago.object', {
#             'object': obj
#         })