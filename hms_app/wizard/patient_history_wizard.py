from odoo import fields, models


class PatientHistory(models.TransientModel):
    _name = "patient.history"
    _description = "Patient History Wizard"

    patient_id = fields.Many2one("hms.patient", readonly=1)
    current_date = fields.Datetime(related="patient_id.create_date", readonly=1)
    description = fields.Text()

    def action_add_history(self):
       pass
