from odoo import fields, models

class Partner(models.Model):
    _inherit = 'res.partner'

    excise_partner_active = fields.Boolean('Track Excise',default=False)
    excise_partner_warehouse_no = fields.Char('Warehouse No.', help='number issued by tax authority to suspend excise liablity')
    excise_partner_nyilvantartasi_szam = fields.Char('Nyilvántartási szám', help='Nyilvántartási szám')
    excise_partner_b2c = fields.Boolean('B2C Partner', help='Partner is a B2C partner')
    excise_partner_b2b = fields.Boolean('B2B Partner', help='Partner is a B2B partner')
