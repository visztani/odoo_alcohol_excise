from odoo import fields, models, api


class Warehouse(models.Model):
    _inherit = 'stock.warehouse'

    excise_warehouse_no = fields.Char('Excise Warehouse No.', help='number issued by tax authority to suspend excise liablity')
    # excise_car_number = fields.Char('Rendszám')
    excise_customs_office_name = fields.Char('Customs Office Name', help='Name of the customs office')
    excise_customs_office_reference_number = fields.Char('Customs Office Reference Number', help='Reference number issued by the customs authority')

class Location(models.Model):
    _inherit = 'stock.location'

    excise_unpaid = fields.Boolean('Duty Unpaid',help='Location stores stock wtihout excise', compute='_compute_excise_unpaid')
    excise_paid_manual = fields.Boolean('Duty Paid location', help='Location is a duty paid location within a duty unpaid warehouse')
    excise_warehouse_no = fields.Char('Excise Warehouse No.', help='number issued by tax authority to suspend excise liablity', compute='_compute_whseno')
    
    # Partner, aki a raktárhelyen tárolja a terméket
    owner_partner_id = fields.Many2one('res.partner', string="Product Owner", help="Partner who owns the product in this location")

    excise_stock_type = fields.Selection(
        [
            ('0', 'Biztosítékmentes'),
            ('1', 'Biztosítékköteles'),
            ('2', 'Adózott jöv. termék'),
            ('3', 'Nem jöv. term.')
        ],
        string='Excise Stock Type',
        index=True,
        required=True,
    )

    from odoo import fields, models, api

class StockLocation(models.Model):
    _inherit = 'stock.location'

    excise_stock_type = fields.Selection(
        [
            ('0', 'Biztosítékmentes'),
            ('1', 'Biztosítékköteles'),
            ('2', 'Adózott jöv. termék'),
            ('3', 'Nem jöv. term.')
        ],
        string='Excise Stock Type',
        index=True,
        required=True,
        #default='0',  # Default value if not specified
    )

    @api.model
    def create(self, vals):
        if 'location_id' in vals and 'excise_stock_type' not in vals:
            parent = self.env['stock.location'].browse(vals['location_id'])
            if parent and parent.excise_stock_type:
                vals['excise_stock_type'] = parent.excise_stock_type
        return super().create(vals)

    def write(self, vals):
        # Ha a szülő location változik
        if 'location_id' in vals:
            new_parent = self.env['stock.location'].browse(vals['location_id'])
            for location in self:
                if new_parent and not location.excise_stock_type:
                    vals['excise_stock_type'] = new_parent.excise_stock_type
        
        return super().write(vals)

    @api.depends('location_id')
    def _compute_excise_stock_type(self):
        for location in self:
            if location.location_id:
                location.excise_stock_type = location.location_id.excise_stock_type


    @api.depends('excise_paid_manual')
    def _compute_excise_unpaid(self):
        for loc in self:
            if loc.excise_paid_manual:
                loc.excise_unpaid = False
                return
            loc.excise_unpaid =  loc.warehouse_id.excise_warehouse_no


    
    def _compute_whseno(self):
        for loc in self:
            loc.excise_warehouse_no =  loc.warehouse_id.excise_warehouse_no