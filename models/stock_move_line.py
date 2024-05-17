from odoo import fields, models, api

class StockMoveLine(models.Model):
    _inherit = "stock.move.line"
    excise_move_ids = fields.One2many('excise.move', 'stock_move_line_id', string='Excise Moves')
    

    @api.model
    def create(self,values):    
        sml = super().create(values)
        if not sml.move_id._requires_excise_move():
            print ()"_____12____")
            return sml
        emvalues = {
            'name' : sml.move_id.name,
            'stock_move_line_id' : sml.id,            
            'stock_move_id' : sml.move_id.id,
            'company_id' : sml.company_id,
            'product_id' : sml.product_id.id,       
            #'move_qty' : sml.reserved_qty,
            #'excise_hlf' : sml.product_id.excise_hlf,
            'excise_knkod' : sml.product_id.excise_knkod,
            'excise_fajtakod' : sml.product_id.excise_fajtakod,
            'move_jogcimkod' : sml.picking_id.excise_jogcimkod,
            'move_adomennyisegkod' : sml.picking_id.excise_adomennyiseg_kod,
            'move_ahk' : sml.picking_id.excise_ahk,

        }
        if sml.qty_done == 0:
            _qty = sml.reserved_qty
        else:
            _qty = sml.qty_done
        excise_result = self.env['excise.category']._calc_excise(sml.product_id,_qty)
        emvalues.update(excise_result)
        if 'excise_categories' in excise_result:
            del emvalues['excise_categories']
            for cat in excise_result['excise_categories']:
                emvalues.update(cat)
                self.env['excise.move'].sudo().create(emvalues)    
        else:
            self.env['excise.move'].sudo().create(emvalues)
        return sml

    '''
    @api.model
    def write(self,values):
        super().write(values)
        if len(self) == 0:
            return True
        if not self.move_id._requires_excise_move():
            return True                       
        if self.qty_done == 0:
            _qty = self.reserved_qty
        else:
            _qty = self.qty_done
        for em in self.excise_move_ids:
            if em.move_qty != _qty:                             
                excise_result = self.env['excise.category']._calc_excise(self.product_id,_qty)
                em.move_qty = _qty
                em.excise_move_volume = excise_result['excise_move_volume']
                em.excise_alcohol = excise_result['excise_alcohol']
                for cat in excise_result['excise_categories']:
                    if cat['excise_category'] == em.excise_category.id:
                        em.excise_amount_tax = cat['excise_amount_tax']
        return True
    '''

    @api.model
    def write(self, values):
        for move_line in self:
            if move_line.qty_done == 0:
                _qty = move_line.reserved_qty
            else:
                _qty = move_line.qty_done
            excise_result = self.env['excise.category']._calc_excise(move_line.product_id, _qty)
            super(StockMoveLine, move_line).write(values)
            for em in move_line.excise_move_ids:
                if em.move_qty != _qty:
                    em.move_qty = _qty
                    em.excise_move_volume = excise_result['excise_move_volume']
                    em.excise_alcohol = excise_result['excise_alcohol']
                    for cat in excise_result['excise_categories']:
                        if cat['excise_category'] == em.excise_category.id:
                            em.excise_amount_tax = cat['excise_amount_tax']
        return True