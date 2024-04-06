from odoo import fields, models

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    excise_sale_order_hlf = fields.Float(string='HLF Total', compute='_compute_order_line_hlf', store=True)

    @api.depends('order_line', 'order_line.total_hlf')
    def _compute_order_line_hlf(self):
        for order in self:
            order.excise_sale_order_hlf = sum(order.order_line.mapped('total_hlf')) 