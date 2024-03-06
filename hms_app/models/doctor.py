from odoo import fields, models


class Doctor(models.Model):
    _name = 'hms.doctor'
    _rec_name = 'firstname'

    firstname = fields.Char()
    lastname = fields.Char()
    image = fields.Binary()
