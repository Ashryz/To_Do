from odoo import fields, models


class Patient(models.Model):
    _name = "hms.patient"
    _rec_name = "firstname"

    firstname = fields.Char()
    lastname = fields.Char()
    birthdate = fields.Date()
    age = fields.Integer()
    address = fields.Text()
    cr_ratio = fields.Float()
    blood_type = fields.Selection([
        ('a-', 'A-'),
        ('a-', 'A+'),
        ('b-', 'B-'),
        ('b+', 'B+'),
        ('o-', 'O-'),
        ('o+', 'O+'),
        ('ab-', 'AB-'),
        ('ab+', 'AB+')
    ])
    pcr = fields.Boolean()
    image = fields.Binary()
    state = fields.Selection([
        ('undetermined', 'Undetermined'),
        ('good', 'Good'),
        ('fair', 'Fair'),
        ('serious', 'Serious'),
    ])
    department_id = fields.Many2one("hms.department")
    department_capacity = fields.Integer(related="department_id.capacity")
    doctor_ids = fields.Many2many("hms.doctor")
