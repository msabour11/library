from odoo import fields,models
class SaleOrder(models.Model):
    _inherit = 'sale.order'
    phone_number = fields.Char(string='Phone')