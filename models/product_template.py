from odoo import fields, models

class ProductTemplate(models.Model):
    _inherit = 'product.template'

    excise_active = fields.Boolean('Track Excise',default=False)
    excise_abv = fields.Float('ABV',help='Alcohol By Volume (% Alcohol')
    excise_hlf = fields.Float('HLF',help='Hectolitre Percent Alcohol by Volume')
    excise_category = fields.Many2one('excise.category','Excise Category')
    excise_volume = fields.Float('Excisable Volume (L)', help='Volume for the basis of the Excise calculation')
    excise_knkod = fields.Char('KN Code',help='Közös Nómenklatúra (Common Nomenclature) Code')
    excise_fajtakod = fields.Char('Fajtakód',help='Fajtakód')
    excise_guarantee_needed = fields.Boolean('Guarantee Needed',default=False,help='Excise Guarantee Needed')
    excise_guarantee_needed = fields.Selection([
        ('0', 'Biztosítékmentes'), ('1', 'Biztosítékköteles'),
        ('3', 'Adózott jöv. termék'),
        ('4', 'Nem jöv. term.')], string='Stock Type',
        index=True)
    
class ProductProduct(models.Model):
    _inherit = 'product.product'

    
    def _get_default_excise_volume(self):
        return self.env['product.template'].browse([self.product_tmpl_id]).excise_volume
        
    excise_volume = fields.Float('Excisable Volume (L)', help='Volume for the basis of the Excise calculation', 
                                    default=lambda self: self._get_default_excise_volume())
                                  #default=lambda self: self.product_tmpl_id.excise_volume)


    def _get_excise_volume(self):
        self.ensure_one()
        if self.excise_volume != 0:
            return self.excise_volume
        return self.product_tmpl_id.excise_volume