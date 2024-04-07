from odoo import _, fields, models, api

class SaleOrderLine(models.Model):

    _inherit = 'sale.order.line'

    total_hlf = fields.Float(string='Line Total HLF', compute='_compute_total_hlf', store=True)

    @api.depends('product_id', 'product_uom_qty', 'product_id.excise_hlf') # type: ignore
    def _compute_total_hlf(self):
        for line in self:
            line.total_hlf = line.product_uom_qty * line.product_id.excise_hlf