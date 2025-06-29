from odoo import models, fields, api

class ResConfigSettings(models.TransientModel):
    _inherit = 'res.config.settings'

    track_name = fields.Boolean(string='Nombre del producto')
    track_default_code = fields.Boolean(string='Referencia interna')
    track_list_price = fields.Boolean(string='Precio de venta')
    track_standard_price = fields.Boolean(string='Costo')
    track_barcode = fields.Boolean(string='Código de barras')

    def set_values(self):
        super().set_values()
        config = self.env['ir.config_parameter'].sudo()
        config.set_param('product_field_tracking.track_name', self.track_name)
        config.set_param('product_field_tracking.track_default_code', self.track_default_code)
        config.set_param('product_field_tracking.track_list_price', self.track_list_price)
        config.set_param('product_field_tracking.track_standard_price', self.track_standard_price)
        config.set_param('product_field_tracking.track_barcode', self.track_barcode)

    @api.model
    def get_values(self):
        res = super().get_values()
        config = self.env['ir.config_parameter'].sudo()
        res.update(
            track_name=config.get_param('product_field_tracking.track_name') == 'True',
            track_default_code=config.get_param('product_field_tracking.track_default_code') == 'True',
            track_list_price=config.get_param('product_field_tracking.track_list_price') == 'True',
            track_standard_price=config.get_param('product_field_tracking.track_standard_price') == 'True',
            track_barcode=config.get_param('product_field_tracking.track_barcode') == 'True',
        )
        return res