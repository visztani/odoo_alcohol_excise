from odoo import _, api, fields, models

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    excise_picking_hlf = fields.Float(string='HLF Total', compute='_compute_picking_line_hlf', store=True)
    excise_adomennyiseg_kod = fields.Char(string='Adóm. kód', related='sale_id.excise_adomennyiseg_kod', readonly=True)
    JOGCIMKODOK = [('32203','KI Jöv. kisker - 32203'),('20503','BE tagállamból adófelfügesztéssel - 32203'),('32201','KI Magánszemély - 32201'),('32202','KI Jöv. eng. nagyker - 32202'),('0','Nem jövedéki')]
    excise_jogcimkod = fields.Selection(string='Jogcímkód', related='sale_id.excise_jogcimkod', readonly=True)
    #BEKULDESSTATUSZOKJR = [('0','Nem beküldött'), ('1','Beküldött'), ('2','Javított'), ('3','Rontottnak jelölt')]
    #jovedeki_raktar_NAV_fele_bekuldott_e = fields.Selection(string='NAV felé elküldve?', selection=BEKULDESSTATUSZOKJR)

    @api.depends('move_ids_without_package', 'move_ids_without_package.total_hlf') # type: ignore
    def _compute_picking_line_hlf(self):
        for picking in self:
            picking.excise_picking_hlf = sum(picking.move_ids_without_package.mapped('total_hlf'))