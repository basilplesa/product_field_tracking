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

    'description': """
Este módulo registra en el chatter del producto los cambios realizados en campos clave como nombre, referencia, precio, costo y código de barras.

Funcionalidades:
- Registro automático de cambios en el chatter.
- Configuración de campos desde Ajustes generales del sistema.
- Indicación del usuario, campo editado, valor anterior y nuevo.

Campos configurables:
- Nombre
- Referencia interna
- Precio de venta
- Costo
- Código de barras

Requiere Odoo Enterprise 16 y los módulos `product` y `mail`.
"""
}