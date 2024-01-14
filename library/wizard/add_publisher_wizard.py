from odoo import models,fields
class PublisherWizard(models.TransientModel):
    _name = 'add.publisher.wizard'
    _description = 'add publisher wizard'

    publisher_id = fields.Many2one('library.publisher', string='publisher')


    def action_add_publisher(self):
        context=self.env.context
        print(context)
        get_publisher_id=context.get('publisher_context_id',False)
        record=self.env['library.book'].browse(get_publisher_id)
        record.publisher_id=self.publisher_id.id


