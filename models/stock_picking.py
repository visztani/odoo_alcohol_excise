'''
from odoo import _, api, fields, models


class StockPicking(models.Model):
    _inherit = 'stock.picking'

    excise_picking_hlf = fields.Float(string='HLF Total', compute='_compute_picking_line_hlf', store=True)
    excise_adomennyiseg_kod = fields.Char(string='Adóm. kód', compute='_compute_excise_adomennyiseg_kod', store=True, required=False)
    JOGCIMKODOK = [('32203','KI Jöv. kisker - 32203'),('20503','BE tagállamból adófelfügesztéssel - 32203'),('32201','KI Magánszemély - 32201'),('32202','KI Jöv. eng. nagyker - 32202'),('0','Nem jövedéki')]
    excise_jogcimkod = fields.Selection(string='Jogcímkód', selection=JOGCIMKODOK, compute='_compute_excise_jogcimkod', store=True, required=False)
    excise_car_no = fields.Char(string='Rendszám', compute='_compute_excise_car_no', store=True, required=False)

    @api.depends('move_ids_without_package', 'move_ids_without_package.total_hlf')
    def _compute_picking_line_hlf(self):
        for picking in self:
            picking.excise_picking_hlf = sum(picking.move_ids_without_package.mapped('total_hlf'))

    @api.depends('sale_id', 'purchase_id')
    def _compute_excise_adomennyiseg_kod(self):
        for picking in self:
            if picking.sale_id:
                picking.excise_adomennyiseg_kod = picking.sale_id.excise_adomennyiseg_kod
            elif picking.purchase_id:
                picking.excise_adomennyiseg_kod = picking.purchase_id.excise_adomennyiseg_kod
            else:
                picking.excise_adomennyiseg_kod = False
            picking._update_required_fields()

    @api.depends('sale_id', 'purchase_id')
    def _compute_excise_jogcimkod(self):
        for picking in self:
            if picking.sale_id:
                picking.excise_jogcimkod = picking.sale_id.excise_jogcimkod
            elif picking.purchase_id:
                picking.excise_jogcimkod = picking.purchase_id.excise_jogcimkod
            else:
                picking.excise_jogcimkod = False
            picking._update_required_fields()

    @api.depends('sale_id', 'purchase_id')
    def _compute_excise_car_no(self):
        for picking in self:
            if picking.sale_id:
                picking.excise_car_no = picking.sale_id.excise_car_no
            elif picking.purchase_id:
                picking.excise_car_no = picking.purchase_id.excise_car_no
            else:
                picking.excise_car_no = False
            picking._update_required_fields()

    def _update_required_fields(self):
        for picking in self:
            if picking.sale_id:
                excise_active = picking.sale_id.order_line.filtered(lambda line: line.product_id.excise_active)
            elif picking.purchase_id:
                excise_active = picking.purchase_id.order_line.filtered(lambda line: line.product_id.excise_active)
            else:
                excise_active = False
            
            if excise_active:
                picking.excise_adomennyiseg_kod.required = True
                picking.excise_jogcimkod.required = True
                picking.excise_car_no.required = True
            else:
                picking.excise_adomennyiseg_kod.required = False
                picking.excise_jogcimkod.required = False
                picking.excise_car_no.required = False


'''
from odoo import _, api, fields, models

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    excise_picking_hlf = fields.Float(string='HLF Total', compute='_compute_picking_line_hlf', store=True)
    excise_adomennyiseg_kod = fields.Char(string='Adóm. kód', compute='_compute_excise_adomennyiseg_kod', store=True, required=True)
    JOGCIMKODOK = [('32203','KI Jöv. kisker - 32203'),('20503','BE tagállamból adófelfügesztéssel - 32203'),('32201','KI Magánszemély - 32201'),('32202','KI Jöv. eng. nagyker - 32202'),('0','Nem jövedéki')]
    excise_jogcimkod = fields.Selection(string='Jogcímkód', selection=JOGCIMKODOK ,compute='_compute_excise_jogcimkod', store=True, required=True)
    excise_car_no = fields.Char(string='Rendszám', compute='_compute_excise_car_no', store=True)

    @api.depends('move_ids_without_package', 'move_ids_without_package.total_hlf')
    def _compute_picking_line_hlf(self):
        for picking in self:
            picking.excise_picking_hlf = sum(picking.move_ids_without_package.mapped('total_hlf'))

    @api.depends('sale_id', 'purchase_id')
    def _compute_excise_adomennyiseg_kod(self):
        for picking in self:
            if picking.sale_id:
                picking.excise_adomennyiseg_kod = picking.sale_id.excise_adomennyiseg_kod
            elif picking.purchase_id:
                picking.excise_adomennyiseg_kod = picking.purchase_id.excise_adomennyiseg_kod
            else:
                picking.excise_adomennyiseg_kod = False

    @api.depends('sale_id', 'purchase_id')
    def _compute_excise_jogcimkod(self):
        for picking in self:
            if picking.sale_id:
                picking.excise_jogcimkod = picking.sale_id.excise_jogcimkod
            elif picking.purchase_id:
                picking.excise_jogcimkod = picking.purchase_id.excise_jogcimkod
            else:
                picking.excise_jogcimkod = False

    @api.depends('sale_id', 'purchase_id')
    def _compute_excise_car_no(self):
        for picking in self:
            if picking.sale_id:
                picking.excise_car_no = picking.sale_id.excise_car_no
            elif picking.purchase_id:
                picking.excise_car_no = picking.purchase_id.excise_car_no
            else:
                picking.excise_car_no = False



# 2024.04.18. 
'''
from odoo import _, api, fields, models

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    excise_picking_hlf = fields.Float(string='HLF Total', compute='_compute_picking_line_hlf', store=True)
    excise_adomennyiseg_kod = fields.Char(string='Adóm. kód', related='sale_id.excise_adomennyiseg_kod', readonly=True, required=True)
    JOGCIMKODOK = [('32203','KI Jöv. kisker - 32203'),('20503','BE tagállamból adófelfügesztéssel - 32203'),('32201','KI Magánszemély - 32201'),('32202','KI Jöv. eng. nagyker - 32202'),('0','Nem jövedéki')]
    excise_jogcimkod = fields.Selection(string='Jogcímkód', related='sale_id.excise_jogcimkod', readonly=True, store=True, required=True)
    #BEKULDESSTATUSZOKJR = [('0','Nem beküldött'), ('1','Beküldött'), ('2','Javított'), ('3','Rontottnak jelölt')]
    #jovedeki_raktar_NAV_fele_bekuldott_e = fields.Selection(string='NAV felé elküldve?', selection=BEKULDESSTATUSZOKJR)
    excise_car_no = fields.Char('Rendszám', related = 'sale_id.excise_car_no', readonly=True, store=True, required=True)

    @api.depends('move_ids_without_package', 'move_ids_without_package.total_hlf') # type: ignore
    def _compute_picking_line_hlf(self):
        for picking in self:
            picking.excise_picking_hlf = sum(picking.move_ids_without_package.mapped('total_hlf'))
'''