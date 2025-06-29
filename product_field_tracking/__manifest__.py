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
<p>Este módulo registra en el <strong>chatter</strong> del producto los cambios realizados en campos clave como nombre, referencia, precio, costo y código de barras.</p>

<h3>Funcionalidades</h3>
<ul>
  <li>Registro automático de cambios en el chatter.</li>
  <li>Configuración de campos desde Ajustes generales del sistema.</li>
  <li>Indicación del usuario, campo editado, valor anterior y nuevo.</li>
</ul>

<h3>Campos configurables</h3>
<ul>
  <li>Nombre</li>
  <li>Referencia interna</li>
  <li>Precio de venta</li>
  <li>Costo</li>
  <li>Código de barras</li>
</ul>

<h3>Requisitos</h3>
<ul>
  <li>Odoo Enterprise 16.0</li>
  <li>Módulos <code>product</code> y <code>mail</code> instalados</li>
</ul>
""",
}