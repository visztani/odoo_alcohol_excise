from odoo import _, api, fields, models
import logging

_logger = logging.getLogger(__name__)

class StockPicking(models.Model):
    _inherit = 'stock.picking'

    excise_picking_hlf = fields.Float(string='HLF Total', compute='_compute_picking_line_hlf', store=True)
    excise_adomennyiseg_kod = fields.Char(string='Adóm. kód', compute='_compute_excise_adomennyiseg_kod', store=True)
    JOGCIMKODOK = [('32203','KI Jöv. kisker - 32203'),('20503','BE tagállamból adófelfügesztéssel - 32203'),('32201','KI Magánszemély - 32201'),('32202','KI Jöv. eng. nagyker - 32202'),('0','Nem jövedéki')]
    excise_jogcimkod = fields.Selection(string='Jogcímkód', selection=JOGCIMKODOK ,compute='_compute_excise_jogcimkod', store=True)
    excise_car_no = fields.Char(string='Rendszám', compute='_compute_excise_car_no', store=True)
    excise_partner_whno = fields.Char('Partner Excise WH No.', compute='_compute_excise_partner_whno', store=True)
    excise_ahk = fields.Char('Admin. Ref. Code', compute='_compute_excise_ahk', store=True)
    excise_stock_type = fields.Selection([
        ('0', 'Biztosítékmentes'), 
        ('1', 'Biztosítékköteles'),
        ('3', 'Adózott jöv. termék'),
        ('4', 'Nem jöv. term.')], 
        string='Excise Stock Type',
        compute='_compute_excise_stock_type', 
        store=True, 
        index=True)

    @api.depends('product_id')
    def _compute_excise_stock_type(self):
        for record in self:
            if record.product_id:
                _logger.info('Computing excise stock type for product ID %s', record.product_id.id)
                record.excise_stock_type = record.product_id.excise_stock_type
            else:
                _logger.info('No product associated with this excise move record')

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
    
    @api.depends('sale_id', 'purchase_id')
    def _compute_excise_partner_whno(self):
        for picking in self:
            if picking.purchase_id:
                picking.excise_partner_whno = picking.purchase_id.excise_partner_whno
            else:
                picking.excise_partner_whno = False
    
    @api.depends('sale_id', 'purchase_id')
    def _compute_excise_ahk(self):
        for picking in self:
            if picking.purchase_id:
                picking.excise_ahk = picking.purchase_id.excise_ahk
            else:
                picking.excise_ahk = picking.origin



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