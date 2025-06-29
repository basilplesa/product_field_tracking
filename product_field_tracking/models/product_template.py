from odoo import models, fields, _
from odoo.tools import float_compare

class ProductTemplate(models.Model):
    _inherit = "product.template"

    def write(self, vals):
        campos_config = {
            'name': 'track_name',
            'default_code': 'track_default_code',
            'list_price': 'track_list_price',
            'standard_price': 'track_standard_price',
            'barcode': 'track_barcode',
        }

        config = self.env['ir.config_parameter'].sudo()
        campos = {
            campo: etiqueta
            for campo, etiqueta in {
                'name': 'Nombre de producto',
                'default_code': 'Referencia interna',
                'list_price': 'Precio de venta',
                'standard_price': 'Costo',
                'barcode': 'Código de barras',
            }.items()
            if config.get_param(f'product_field_tracking.{campos_config[campo]}') == 'True'
        }

        mensajes_por_producto = {}

        for rec in self:
            mensajes = []

            for campo, etiqueta in campos.items():
                if campo in vals:
                    antiguo = rec[campo]
                    nuevo = vals[campo]

                    if isinstance(antiguo, float):
                        if float_compare(antiguo, nuevo, precision_digits=2) != 0:
                            mensajes.append(f"<b>{etiqueta}</b> cambió de '{antiguo:.2f}' a <b>{nuevo:.2f}</b>")
                    else:
                        if antiguo != nuevo:
                            mensajes.append(f"<b>{etiqueta}</b> cambió de '{antiguo}' a <b>{nuevo}</b>")

            if mensajes:
                mensajes_por_producto[rec.id] = mensajes

        res = super().write(vals)

        for rec in self:
            if rec.id in mensajes_por_producto:
                usuario = self.env.user.name
                ahora = fields.Datetime.now().strftime("%d/%m/%Y %H:%M")
                encabezado = f"<b>Cambio registrado por:</b> {usuario} - {ahora}"
                cuerpo = "<br/>".join([encabezado, ""] + mensajes_por_producto[rec.id])
                rec.message_post(body=cuerpo, subtype_xmlid="mail.mt_note")

        return res