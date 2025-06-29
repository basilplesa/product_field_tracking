{
    'name': 'Product Field Tracking',
    'version': '16.0.1.1.0',
    'category': 'Inventory',
    'summary': 'Seguimiento automático de campos clave del producto',

    'author': 'XP Solution',
    'website': 'https://xpsolution.odoo.com',
    'license': 'LGPL-3',

    'depends': [
        'product',
        'mail',
    ],

    'data': [
        'views/res_config_settings_view.xml',
    ],

    'installable': True,
    'application': False,

'description': """\
    """,
}
