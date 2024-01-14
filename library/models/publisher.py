from datetime import datetime

from odoo import fields, models,api


class Publisher(models.Model):
    _name = 'library.publisher'
    _description = 'Publisher'
    _rec_name = 'last_name'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    first_name = fields.Char('First Name', required=True)
    last_name = fields.Char('Last Name', required=True)
    date_join = fields.Date('Date Join', required=True)
    active = fields.Boolean('Active?', default=True)
    age = fields.Integer('Age',compute='_compute_age')
    national_id = fields.Char('National ID', required=True)
    image = fields.Binary('Image')
    book_ids = fields.One2many('library.book', 'publisher_id', string='Books')
    birth_date=fields.Date(required=True)




    @api.depends('birth_date')
    def _compute_age(self):
        for record in self:
            if record.birth_date:
                now = fields.Date.today()
                record.age = (now - record.birth_date).days//365
            else:
                record.age = 0






