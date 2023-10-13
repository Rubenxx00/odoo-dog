from odoo import fields, models


class DogBreed(models.Model):
    _name = "dog.breed"
    _description = "Razze dei cani"
    _order = "name"

    name = fields.Char(translate=True)
