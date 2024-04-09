from odoo import _, fields, models, api

class SaleOrderLine(models.Model):

    _inherit = 'sale.order.line'

    excise_sale_order_line_biztositek = fields.Boolean(string='Biztosíték?', related='product_id.excise_guarantee_needed', readonly=True)
    excise_line_fajtakod = fields.Char(string='Fajtakód', related='product_id.excise_fajtakod', readonly=True)
    excise_line_knkod = fields.Char(string='KN kód', related='product_id.excise_knkod', readonly=True)
    total_hlf = fields.Float(string='HLF Line', compute='_compute_total_hlf', store=True)

    @api.depends('product_id', 'product_uom_qty', 'product_id.excise_hlf') # type: ignore
    def _compute_total_hlf(self):
        for line in self:
            line.total_hlf = line.product_uom_qty * line.product_id.excise_hlf