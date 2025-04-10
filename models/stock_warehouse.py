from odoo import fields, models, api


class Warehouse(models.Model):
    _inherit = 'stock.warehouse'

    excise_warehouse_no = fields.Char('Excise Warehouse No.', help='number issued by tax authority to suspend excise liablity')
    # excise_car_number = fields.Char('Rendszám')
    excise_customs_office_name = fields.Char('Customs Office Name', help='Name of the customs office')
    excise_customs_office_reference_number = fields.Char('Customs Office Reference Number', help='Reference number issued by the customs authority')

class Location(models.Model):
    _inherit = 'stock.location'

    excise_unpaid = fields.Boolean('Duty Unpaid',help='Location stores stock wtihout excise', compute='_compute_excise_unpaid')
    excise_paid_manual = fields.Boolean('Duty Paid location', help='Location is a duty paid location within a duty unpaid warehouse')
    excise_warehouse_no = fields.Char('Excise Warehouse No.', help='number issued by tax authority to suspend excise liablity', compute='_compute_whseno')

    @api.depends('excise_paid_manual')
    def _compute_excise_unpaid(self):
        for loc in self:
            if loc.excise_paid_manual:
                loc.excise_unpaid = False
                return
            loc.excise_unpaid =  loc.warehouse_id.excise_warehouse_no


    
    def _compute_whseno(self):
        for loc in self:
            loc.excise_warehouse_no =  loc.warehouse_id.excise_warehouse_no