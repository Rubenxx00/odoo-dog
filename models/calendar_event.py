from odoo import models, fields

class CalendarEvent(models.Model):
    _inherit = 'calendar.event'

    dog_id = fields.Many2one('dog', string='Dog', ondelete='cascade')
