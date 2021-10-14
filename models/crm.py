from odoo import models, fields, api
from datetime import datetime

class Crm_lead(models.Model):
    _inherit = 'crm.lead'

    create_date = fields.Date(string='Create Date', default=datetime.today(), required=True)
    kalkulasi = fields.Many2one('res.users', string='Kalkulasi')