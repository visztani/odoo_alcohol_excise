from odoo import fields, models, api
from odoo.exceptions import UserError

class StockMove(models.Model):
    _inherit = "stock.move"

    
    total_hlf = fields.Float(string='HLF Line', compute='_compute_total_hlf', store=True)

    @api.depends('product_id', 'product_uom_qty', 'product_id.excise_hlf') # type: ignore
    def _compute_total_hlf(self):
        for line in self:
            line.total_hlf = line.product_uom_qty * line.product_id.excise_hlf
    
    def _requires_excise_move(self):
        self.ensure_one()
        if not self.product_id.excise_active:
            return False
        if not self.location_id.excise_unpaid and self.location_dest_id.excise_unpaid:
            if self.location_id.usage == 'inventory':  #allow stock adjustments
                return True
            raise UserError("You cannot move excisable product from duty paid to duty unpaid")
        if self.location_id.excise_warehouse_no != self.location_dest_id.excise_warehouse_no:
            return True
        if self.location_id.excise_unpaid and not self.location_dest_id.excise_unpaid:
           return True
        return False
        