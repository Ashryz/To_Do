from odoo import fields, models, api
from dateutil.relativedelta import relativedelta


class Patient(models.Model):
    _name = "hms.patient"
    _rec_name = "firstname"

    firstname = fields.Char(required=1)
    lastname = fields.Char(required=1)
    birthdate = fields.Date()
    age = fields.Integer(compute='_compute_age')
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
    history_ids = fields.One2many("patient.history", "patient_id")

    def action_add_history(self):
        action = self.env['ir.actions.actions']._for_xml_id('hms_app.patient_history_wizard_action')
        action['context'] = {
            'default_patient_id': self.id,

        }
        return action

    @api.onchange('age')
    def _on_change_age(self):
        if self.age and self.age < 30:
            self.pcr = True
            return {
                'warning': {
                    'title': 'Note',
                    'message': 'PCR has been checked',
                    'type': 'notification',
                },
            }
        else:
            self.pcr = False

    @api.depends("birthdate")
    def _compute_age(self):
        for rec in self:
            if rec.birthdate:
                rec.age = relativedelta(fields.Date.today(), rec.birthdate).years
            else:
                rec.age = False
