from odoo import fields, models

class SaleOrder(models.Model):
    _inherit = 'sale.order'

    excise_sale_order_hlf = fields.Float(string='HLF Total', compute='_compute_order_line_hlf', store=True)
    excise_adomennyiseg_kod = fields.Char(string='Adóm. kód')
    JOGCIMKODOK = [('32203','KI Jöv. kisker - 32203'),('20503','BE tagállamból adófelfügesztéssel - 32203'),('32201','KI Magánszemély - 32201'),('32202','KI Jöv. eng. nagyker - 32202'),('0','Nem jövedéki')]
    excise_jogcimkod = fields.Selection(string='Jogcímkód', selection=JOGCIMKODOK)
    #BEKULDESSTATUSZOKJR = [('0','Nem beküldött'), ('1','Beküldött'), ('2','Javított'), ('3','Rontottnak jelölt')]
    #jovedeki_raktar_NAV_fele_bekuldott_e = fields.Selection(string='NAV felé elküldve?', selection=BEKULDESSTATUSZOKJR)

    @api.depends('order_line', 'order_line.total_hlf') # type: ignore
    def _compute_order_line_hlf(self):
        for order in self:
            order.excise_sale_order_hlf = sum(order.order_line.mapped('total_hlf')) 