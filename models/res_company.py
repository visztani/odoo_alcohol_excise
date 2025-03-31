from odoo import models, fields

class ResCompany(models.Model):
    _inherit = 'res.company'

    company_frame_license = fields.Char(string="Excise Frame License", translate=True)
