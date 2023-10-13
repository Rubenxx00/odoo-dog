from odoo import models, fields

class Dog(models.Model):
    _name = 'dog'
    _description = 'Cane'
    _inherit = ["mail.thread", "mail.activity.mixin"]

    name = fields.Char('Nome', required=True)
    breed_id = fields.Many2one("dog.breed", string="Razza")
    color = fields.Char('Colore')
    dermatitis = fields.Boolean('Dermatite', default=False)
    notes = fields.Text('Note')
    gender = fields.Selection(
        string="Sesso",
        selection=[
            ("female", "Femmina"),
            ("male", "Maschio")
        ]
    )
    image = fields.Binary(
        attachment=True, help="Foto dell'animale"
    )


    # associate the dog with the owner (contact)
    owner_id = fields.Many2one('res.partner', string='Proprietario')
    
