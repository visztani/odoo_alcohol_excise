from odoo import fields, models, api
from odoo.exceptions import UserError
import logging

_logger = logging.getLogger(__name__)

class StockMove(models.Model):
    _inherit = "stock.move"

    
    total_hlf = fields.Float(string='HLF Line', compute='_compute_total_hlf', store=True)
    excise_move_fajtakod = fields.Char(string='Fajtakód', related='product_id.excise_fajtakod', readonly=True)
    excise_move_knkod = fields.Char(string='KN kód', related='product_id.excise_knkod', readonly=True)
    excise_move_guarantee = fields.Boolean(string='Biztosíték?', related='product_id.excise_guarantee_needed', readonly=True)
    excise_move_excise_stock_type = fields.Selection([
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
                _logger.info('EM Computing excise stock type for product ID %s', record.product_id.excise_stock_type)
                record.excise_move_excise_stock_type = record.product_id.excise_stock_type
            else:
                _logger.info('EM No product associated with this excise move record')


    @api.depends('product_id', 'product_uom_qty', 'product_id.excise_hlf') # type: ignore
    def _compute_total_hlf(self):
        for line in self:
            line.total_hlf = line.product_uom_qty * line.product_id.excise_hlf
    
    '''
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
    '''

    def _requires_excise_move(self):
        for move in self:
            move.ensure_one()
            if not move.product_id.excise_active:
                return False
            if not move.location_id.excise_unpaid and move.location_dest_id.excise_unpaid:
                #if move.location_id.usage == 'inventory':  # allow stock adjustments
                #    return True
                if move.location_id.usage == 'customer':  # Check if move is from a customer location to another location
                    return True
                raise UserError("You cannot move excisable product from duty paid to duty unpaid. Location type: {move.location_id.usage}")
            if move.location_id.excise_warehouse_no != move.location_dest_id.excise_warehouse_no:
                return True
            if move.location_id.excise_unpaid and not move.location_dest_id.excise_unpaid:
                return True
        return False

    
    

    class StockMoveLine(models.Model):
        _inherit = "stock.move.line"

    
        excise_move_line_total_hlf = fields.Float(string='HLF Line', compute='_compute_total_hlf', store=True)
        excise_move_line_fajtakod = fields.Char(string='Fajtakód', related='product_id.excise_fajtakod', readonly=True)
        excise_move_line_knkod = fields.Char(string='KN kód', related='product_id.excise_knkod', readonly=True)
        excise_move_line_guarantee = fields.Boolean(string='Biztosíték?', related='product_id.excise_guarantee_needed', readonly=True)

        @api.depends('product_id', 'qty_done', 'product_id.excise_hlf') # type: ignore
        def _compute_total_hlf(self):
            for line in self:
                line.excise_move_line_total_hlf = line.qty_done * line.product_id.excise_hlf
        