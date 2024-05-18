import logging
from odoo import _, api, fields, models
from odoo.exceptions import UserError


_logger = logging.getLogger(__name__)

class excise_move(models.Model):
    _name = 'excise.move'
    _description = 'Excise Line'

    name = fields.Text('Description', index=True, required=True)
    stock_move_id = fields.Many2one(
        'stock.move', 'Stock Move',
        check_company=True,index=True)
    stock_move_line_id = fields.Many2one(
        'stock.move.line', 'Stock Move Line',
        check_company=True,index=True)
    date = fields.Datetime(
        'Date', default=fields.Datetime.now, index=True, required=True,
        readonly= True,related='stock_move_id.date',store=True)
    company_id = fields.Many2one('res.company', string='Company', readonly=True, index=True)
    currency_id = fields.Many2one('res.currency', string="Currency",readonly=True)
    product_id = fields.Many2one('product.product', 'Product', check_company=True, domain="[('type', '!=', 'service'), '|', ('company_id', '=', False), ('company_id', '=', company_id)]")
    move_qty = fields.Float('Movement Quantity', default=0.0, digits='Product Unit of Measure', copy=False)
    move_state = fields.Selection([
        ('draft', 'New'), ('cancel', 'Cancelled'),
        ('waiting', 'Waiting Another Move'),
        ('confirmed', 'Waiting Availability'),
        ('partially_available', 'Partially Available'),
        ('assigned', 'Available'),
        ('done', 'Done')], string='Status',
        copy=False, default='draft', index=True, readonly=True,
        related='stock_move_id.state',store=True)   
    move_reference = fields.Char(related='stock_move_id.reference', string="Reference", store=True)
    move_location_id = fields.Many2one('stock.location', 'Source Location',
                related='stock_move_id.location_id', readonly=True)
    #move_source_id = fields.Many2one('res.company', 'Source Address ',
    #            related='stock_move_id.company_id', readonly=True)
    move_location_dest_id = fields.Many2one('stock.location', 'Destination Location',
                related='stock_move_id.location_dest_id', readonly=True)
    #move_partner_id = fields.Many2one('res.partner', 'Destination Address ',
    #            related='stock_move_id.partner_id', readonly=True)
    move_source_address = fields.Many2one('res.partner', string='Source Address', compute='_compute_addresses', store=True)
    move_destination_address = fields.Many2one('res.partner', string='Destination Address', compute='_compute_addresses', store=True)


    excise_abv = fields.Float('ABV',help='Average By Volume (% Alcohol)',readonly=True)
    excise_move_volume = fields.Float('Excisable Volume (L)', help='Volume being moved for the basis of the Excise calculation')
    excise_alcohol = fields.Float('Volume of alcohol (L)',readonly=True)
    excise_category = fields.Many2one('excise.category','Excise Category',readonly=True)
    excise_rate = fields.Monetary('Rate',readonly=True)
    excise_amount_tax = fields.Monetary(string='Excise Amount', readonly=True)
    excise_payable = fields.Monetary(string='Total Excise Amount.',help='Total excise payable after releifs (e.g. small brewers allowance)',readonly=True)

    # új mező (pl.move_jogcimkod) esetén itt kell készíteni egy újat, ezt a nevet kell megadni a reportban (excise_move_views.xml: <field name="move_fajtakod"/>) és
    # ennek a mezőnek kell értéket adni a stock_move_line.py-ban az emvaluesban: 'move_jogcimkod' : sml.picking_id.excise_jogcimkod,
    # 'move_jogcimkod' : sml.picking_id.excise_jogcimkod, sml -> az egész stock move line objektum, picking_id-> a példányosított stock.picking, amin az excise_jogcimkod szerepel.

    excise_hlf = fields.Float('HLF', help='HLF', readonly=True)
    excise_knkod = fields.Char('KN kód', help='KN', readonly=True)
    excise_fajtakod = fields.Char('Fajtakód', help='Fajtakod', readonly=True)
    move_jogcimkod = fields.Char('Jogcímkód', readonly=True)
    move_adomennyisegkod = fields.Char('Adóm. kód', readonly=True)
    move_ahk = fields.Char('ARC', readonly=True)

    @api.depends('move_location_id', 'move_location_dest_id', 'stock_move_id')
    def _compute_addresses(self):
        for record in self:
            if record.move_location_id.usage == 'internal':
                record.move_source_address = record.stock_move_id.company_id.partner_id.id
            else:
                record.move_source_address = record.stock_move_id.partner_id.id
            
            if record.move_location_dest_id.usage == 'internal':
                record.move_destination_address = record.stock_move_id.company_id.partner_id.id
            else:
                record.move_destination_address = record.stock_move_id.partner_id.id


    @api.model
    def unlink(self, values):
        print("DELETE.................................") # consolra kinyomtatja
        _logger.info('Attempt to delete excise.move record.') # logba beleírja
        raise UserError(_('You cannot delete an excise move record.')) # alsóvonás a fordíthatóság miatt van, hozzá kell adni az elesén: from odoo import _, api, fields, models
        #return super(excise_move, self).unlink()