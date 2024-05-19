from odoo import fields, models, api
import logging

_logger = logging.getLogger(__name__)

class StockMoveLine(models.Model):
    _inherit = "stock.move.line"
    excise_move_ids = fields.One2many('excise.move', 'stock_move_line_id', string='Excise Moves')

    @api.model
    def create(self, values):
        _logger.info('Entering create method with values: %s', values)
        sml = super().create(values)
        _logger.info('Stock Move Line created with ID: %s', sml.id)

        if not sml.move_id._requires_excise_move():
            _logger.info('Excise move not required for Stock Move Line ID: %s', sml.id)
            return sml

        emvalues = {
            'name': sml.move_id.name,
            'stock_move_line_id': sml.id,
            'stock_move_id': sml.move_id.id,
            'company_id': sml.company_id.id,
            'product_id': sml.product_id.id,
            'excise_knkod': sml.product_id.excise_knkod,
            'excise_fajtakod': sml.product_id.excise_fajtakod,
            'move_jogcimkod': sml.picking_id.excise_jogcimkod,
            'move_adomennyisegkod': sml.picking_id.excise_adomennyiseg_kod,
            'move_ahk': sml.picking_id.excise_ahk,
            'move_excise_stock_type': sml.product_id.excise_stock_type,
        }

        if sml.qty_done == 0:
            _qty = sml.reserved_qty
        else:
            _qty = sml.qty_done

        excise_result = self.env['excise.category']._calc_excise(sml.product_id, _qty)
        _logger.info('Excise result calculated: %s', excise_result)
        emvalues.update(excise_result)

        if 'excise_categories' in excise_result:
            del emvalues['excise_categories']
            for cat in excise_result['excise_categories']:
                emvalues.update(cat)
                _logger.info('Creating excise move with values LINE 46: %s', emvalues)
                self.env['excise.move'].sudo().create(emvalues)
        else:
            _logger.info('Creating excise move with values LINE 49: %s', emvalues)
            self.env['excise.move'].sudo().create(emvalues)

        return sml

    @api.model
    def write(self, values):
        _logger.info('Entering write method with values: %s', values)
        for move_line in self:
            if move_line.qty_done == 0:
                _qty = move_line.reserved_qty
            else:
                _qty = move_line.qty_done
            excise_result = self.env['excise.category']._calc_excise(move_line.product_id, _qty)
            _logger.info('Excise result calculated for write: %s', excise_result)

            super(StockMoveLine, move_line).write(values)
            _logger.info('Stock Move Line with ID %s updated', move_line.id)

            for em in move_line.excise_move_ids:
                if em.move_qty != _qty:
                    _logger.info('Updating excise move ID %s with new qty: %s', em.id, _qty)
                    em.move_qty = _qty
                    em.excise_move_volume = excise_result['excise_move_volume']
                    em.excise_alcohol = excise_result['excise_alcohol']
                    for cat in excise_result['excise_categories']:
                        if cat['excise_category'] == em.excise_category.id:
                            em.excise_amount_tax = cat['excise_amount_tax']
        return True

    @api.model
    def _create_excise_move(self, sml):
        _logger.info('Creating excise move for Stock Move Line: %s', sml)
        emvalues = {
            'name': sml.move_id.name,
            'stock_move_line_id': sml.id,
            'stock_move_id': sml.move_id.id,
            'company_id': sml.company_id.id,
            'product_id': sml.product_id.id,
            'excise_knkod': sml.product_id.excise_knkod,
            'excise_fajtakod': sml.product_id.excise_fajtakod,
            'move_jogcimkod': sml.picking_id.excise_jogcimkod,
            'move_adomennyisegkod': sml.picking_id.excise_adomennyiseg_kod,
            'move_ahk': sml.picking_id.excise_ahk,
            'move_excise_stock_type': sml.product_id.excise_stock_type,
            
        }

        if sml.qty_done == 0:
            _qty = sml.reserved_qty
        else:
            _qty = sml.qty_done

        excise_result = self.env['excise.category']._calc_excise(sml.product_id, _qty)
        _logger.info('Excise result for create: %s', excise_result)
        emvalues.update(excise_result)

        if 'excise_categories' in excise_result:
            del emvalues['excise_categories']
            for cat in excise_result['excise_categories']:
                emvalues.update(cat)
                _logger.info('Creating excise move with values: %s', emvalues)
                self.env['excise.move'].sudo().create(emvalues)
        else:
            _logger.info('Creating excise move with values: %s', emvalues)
            self.env['excise.move'].sudo().create(emvalues)

    def _update_excise_move(self, sml):
        _logger.info('Updating excise move for Stock Move Line: %s', sml)
        _qty = sml.qty_done if sml.qty_done else sml.reserved_qty
        excise_result = self.env['excise.category']._calc_excise(sml.product_id, _qty)
        _logger.info('Excise result for update: %s', excise_result)

        for em in sml.excise_move_ids:
            if em.move_qty != _qty:
                _logger.info('Updating excise move ID %s with new qty: %s', em.id, _qty)
                em.move_qty = _qty
                em.excise_move_volume = excise_result['excise_move_volume']
                em.excise_alcohol = excise_result['excise_alcohol']
                for cat in excise_result['excise_categories']:
                    if cat['excise_category'] == em.excise_category.id:
                        em.excise_amount_tax = cat['excise_amount_tax']
