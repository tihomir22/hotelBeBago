# -*- coding: utf-8 -*-
{
    'name': "HotelsBeBago",

    'summary': """
        Short (1 phrase/line) summary of the module's purpose, used as
        subtitle on modules listing or apps.openerp.com""",

    'description': """
        Long description of module's purpose
    """,

    'author': "My Company",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/master/odoo/addons/base/module/module_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base','sale'],

    # always loaded
    'data': [
        'views/city.xml',
        'views/hotel.xml',
        'views/habitacion.xml',
        'views/reserva.xml',
        'views/reserva_wizard.xml',
        'views/hotelfotos.xml',
        'views/hotelrooms.xml',
        'views/comentarios.xml',
        'views/seleccion_wizard.xml',
        'views/clientes.xml',
        'views/sale_order_line.xml',
        'views/views.xml',
        'views/templates.xml',
        'views/servicis.xml',
	'demo/archivoDemoPhotosHotel.xml',
	'demo/archivoDemoRoomPhotos.xml',
	'demo/archivoDemoServicis.xml',
	'demo/archivoDemoHotel.xml',
	'demo/archivoDemoCity.xml',
	'demo/archivoDemoRooms.xml',
	'demo/archivoDemoComentarios.xml',
	'demo/demoProducto.xml'
	
	
	
	
	
	
	
	
	
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
