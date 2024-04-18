from odoo import _, fields, models, api

class PurchaseOrder(models.Model):
    _inherit = 'purchase.order'

    excise_purchase_order_hlf = fields.Float(string='HLF Total', compute='_compute_order_line_hlf', store=True)
    excise_adomennyiseg_kod = fields.Char(string='Adóm. kód')
    JOGCIMKODOK = [('32203','KI Jöv. kisker - 32203'),('20503','BE tagállamból adófelfügesztéssel - 32203'),('32201','KI Magánszemély - 32201'),('32202','KI Jöv. eng. nagyker - 32202'),('0','Nem jövedéki')]
    excise_jogcimkod = fields.Selection(string='Jogcímkód', selection=JOGCIMKODOK)
    #BEKULDESSTATUSZOKJR = [('0','Nem beküldött'), ('1','Beküldött'), ('2','Javított'), ('3','Rontottnak jelölt')]
    #jovedeki_raktar_NAV_fele_bekuldott_e = fields.Selection(string='NAV felé elküldve?', selection=BEKULDESSTATUSZOKJR)
    excise_car_no = fields.Char('Rendszám', default='kocsi1')
    excise_partner_whno = fields.Char('Partner Excise WH No.', related='partner_id.property_stock_supplier.excise_warehouse_no', readonly=True, store=True);
    excise_ahk = fields.Char('Admin. Ref. Code')

    @api.depends('order_line', 'order_line.total_hlf') # type: ignore
    def _compute_order_line_hlf(self):
        for order in self:
            order.excise_purchase_order_hlf = sum(order.order_line.mapped('total_hlf')) 