# -*- coding: utf-8 -*-
{
    'name': "open_academy",

    'summary': """
        Modulo de prueba para aprender a trabajar con la herramienta de odoo""",

    'description': """
        Long description of module's purpose
    """,

    'author': "Brayan Sanchez",
    'website': "http://www.yourcompany.com",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base', 'board'],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'views/views.xml',
        'views/templates.xml',
        
        'data/slide_channel_data.xml',
        'data/slide_channel_data_v13.xml',
        'security/security.xml',
        'views/openacademy.xml',
        'views/partner.xml',
        'views/session_board.xml',
        'reports.xml',
    ],
    # only loaded in demonstration mode
    'demo': [
        'demo/demo.xml',
    ],
}
