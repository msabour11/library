from odoo import fields, models, api
from odoo.exceptions import UserError
from datetime import datetime,timedelta


class Book(models.Model):
    _name = 'library.book'
    _description = 'Book'
    _inherit = ['mail.thread', 'mail.activity.mixin']

    _order = "name"
    _sql_constraints = [
        ('name_unique', 'unique (name)', 'The book name must be unique.'),
    ]
    name = fields.Char('Title', required=True, index=1, copy=1, tracking=1)
    isbn = fields.Char('ISBN')
    date_published = fields.Date(default=fields.Date.today())
    image = fields.Binary('Cover')
    active = fields.Boolean('Active?', default=True)
    publisher_id = fields.Many2one('library.publisher', string='publisher')
    state = fields.Selection([('new', 'New'), ('published', 'Published'), ('draft', 'Draft')],
                             default='draft')
    ref = fields.Char('Reference', copy=0, readonly=1, default='New')
    line_ids = fields.One2many('book.line','book_id')

    @api.constrains('name')
    def check_name(self):
        for record in self:
            if record.name == 'book':
                raise UserError("The name 'book' is not allowed.")

    def action_publish(self):
        for record in self:
            record.state = 'published'

    def action_new(self):
        for record in self:
            record.state = 'new'

    def action_draft(self):
        for record in self:
            record.state = 'draft'

    # create sequence
    @api.model
    def create(self, vals):
        res = super(Book, self).create(vals)
        res.ref = self.env['ir.sequence'].sudo().next_by_code('book_ref')
        return res

    def mark_state_as_new(self):
        for record in self:
            record.state = 'new'
    # methods to archive books that old than 10 years
    def archive_book(self):
        today = fields.Date.today()
        estimate_cron = today - timedelta(days=365 * 10)
        print(f"Estimate Cron: {estimate_cron}")

        book_to_archive = self.search([('date_published', '<', estimate_cron)])
        print(f"Books to Archive: {book_to_archive}")

        for book in book_to_archive:
            print(f"Archiving book {book.id}")
            book.active = False



    # def action_preview_sale_order(self):
    #     self.ensure_one()
    #     return {
    #         'type': 'ir.actions.act_url',
    #         'target': 'self',
    #         'url': self.get_portal_url(),
    #     }

    def open_publisher_wizard(self):
        print(self)
        return {
            'name': 'add Publisher',
            'type': 'ir.actions.act_window',
            'view_mode': 'form',
            'res_model': 'add.publisher.wizard',
            'target': 'new',
            'context': {'publisher_context_id': self.id},
        }




class BookLine(models.Model):
    _name = 'book.line'
    name = fields.Char('Title', required=True)
    date=fields.Date(default=fields.Date.today())
    note = fields.Char('Note')
    book_id = fields.Many2one('library.book')
    price=fields.Float('Price')

