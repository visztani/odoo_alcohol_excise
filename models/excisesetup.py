from odoo import api, fields, models

class excise_category(models.Model):
    #https://www.gov.uk/government/publications/rates-and-allowance-excise-duty-alcohol-duty/alcohol-duty-rates-from-24-march-2014
    _name = 'excise.category'
    _description = 'Excise Category'

    name = fields.Text('Description', index=True, required=True)
    tech_name = fields.Text('Technical Description')

    excise_product_code = fields.Selection([
            ('T200', 'T200 — Cigarettes'),
            ('T300', 'T300 — Cigars and cigarillos'),
            ('T400', 'T400 — Fine-cut tobacco for the rolling of cigarettes'),
            ('T500', 'T500 — Other smoking tobacco'),
            ('B000', 'B000 — Beer'),
            ('W200', 'W200 — Still wine'),
            ('W300', 'W300 — Sparkling wine'),
            ('I000', 'I000 — Alcohol — intermediate products'),
            ('S200', 'S200 — Spirituous beverages'),
            ('S300', 'S300 — Ethyl alcohol'),
            ('S400', 'S400 — Partially denatured alcohol'),
            ('S500', 'S500 — Other products containing ethyl alcohol'),
            ('E200', 'E200 — Vegetable and animal oils (energy products)'),
            ('E300', 'E300 — Mineral oils (energy products)'),
            ('E410', 'E410 — Leaded petrol'),
            ('E420', 'E420 — Unleaded petrol'),
            ('E430', 'E430 — Gasoil, unmarked'),
            ('E440', 'E440 — Gasoil, marked'),
            ('E450', 'E450 — Kerosene, unmarked'),
            ('E460', 'E460 — Kerosene, marked'),
            ('E470', 'E470 — Heavy fuel oil'),
            ('E480', 'E480 — Bulk CN 2710 11 21 / 25 / 19 29'),
            ('E490', 'E490 — CN 2710 11 - 19 69, not specified above'),
            ('E500', 'E500 — Liquefied petroleum gases (LPG)'),
            ('E600', 'E600 — Saturated acyclic hydrocarbons'),
            ('E700', 'E700 — Cyclic hydrocarbons'),
            ('E800', 'E800 — Methanol (methyl alcohol)'),
            ('E910', 'E910 — Acyclic hydrocarbons mix – FAME'),
            ('E920', 'E920 — Acyclic hydrocarbons mix – others'),
        ], string="Excise Product Code", help="Standardized EU excise product code (e.g. B000 for Beer)")

        fajtakod = fields.Char ('Fajtakód', required = True)

    rate_per = fields.Selection([
        ('hectoabv','Rate per hectolitre per cent of alcohol in the beer'),
        ('hectoprod','Rate per hectolitre of product'),   
        ('litrealco','Rate per litre of pure alcohol')
    ])
    rate = fields.Monetary(compute='_compute_current_rate', string='Current Rate', digits=0,
                    help='The rate of the currency to the currency of rate 1.')

    add_cat = fields.Many2one('excise.category','Additional Category')
    date = fields.Date(compute='_compute_date')
    rate_ids = fields.One2many('excise.category.rate', 'category_id', string='Rates')
    company_id = fields.Many2one('res.company', string='Company', readonly=True, index=True)
    currency_id = fields.Many2one('res.currency', string="Currency")

    @api.depends('rate_ids.rate') 
    def _compute_current_rate(self):
        date = self._context.get('date') or fields.Date.today()
        excise_rates = self._get_rates(date)
        for cat in self:
            cat.rate = excise_rates.get(cat.id) or 0

    def _get_rates(self,  date):
        self.env['excise.category.rate'].flush_recordset(['rate', 'category_id', 'name'])
        query = """SELECT ec.id,
                    COALESCE((SELECT ecr.rate FROM excise_category_rate ecr
                        WHERE category_id = ec.id AND ecr.name <= %s
                        ORDER BY "name" DESC
                        LIMIT 1), 1.0) AS ecr
                    FROM excise_category ec
                WHERE ec.id IN %s"""
        self._cr.execute(query, (date,  tuple(self.ids)))
        category_rates = dict(self._cr.fetchall())
        return category_rates

    @api.depends('rate_ids.name')
    def _compute_date(self):
        for category in self:
            category.date = category.rate_ids[:1].name

    @api.model
    def _calc_excise(self,product,quantity):
        alcohol_vol = quantity * product._get_excise_volume() * product.excise_abv / 100
        values = {
            'move_qty' : quantity,
            'excise_abv' : product.excise_abv,
            'excise_move_volume' : quantity * product._get_excise_volume(),
            'excise_alcohol': alcohol_vol,
        }
        excise_categories = [] #list
        cat_values = {
            'company_id' : product.excise_category.company_id.id,
            'currency_id' : product.excise_category.currency_id.id,
            'excise_category' : product.excise_category.id,
            'excise_rate' :product.excise_category.rate,
        }
        if product.excise_category.rate_per == 'hectoabv':
            cat_values['excise_amount_tax'] = alcohol_vol * product.excise_category.rate
        elif product.excise_category.rate_per == 'hectoprod':
            cat_values['excise_amount_tax'] = quantity * product._get_excise_volume() * product.excise_category.rate
        elif product.excise_category.rate_per == 'litrealco':
            cat_values['excise_amount_tax'] = alcohol_vol * product.excise_category.rate
        excise_categories.append(cat_values)
        if product.excise_category.add_cat:
            cat_values = {
                'company_id' : product.excise_category.company_id.id,
                'currency_id' : product.excise_category.currency_id.id,
                'excise_category' : product.excise_category.add_cat.id,
                'excise_rate' :product.excise_category.add_cat.rate,
            }
            if product.excise_category.add_cat.rate_per == 'hectoabv':
                cat_values['excise_amount_tax'] = alcohol_vol * product.excise_category.add_cat.rate
            elif product.excise_category.add_cat.rate_per == 'hectoprod':
                cat_values['excise_amount_tax'] = quantity * product._get_excise_volume() * product.excise_category.add_cat.rate
            elif product.excise_category.add_cat.rate_per == 'litrealco':
                cat_values['excise_amount_tax'] = alcohol_vol * product.excise_category.add_cat.rate
            excise_categories.append(cat_values)
        values['excise_categories'] = excise_categories
        

        return values




class excise_category_rate(models.Model):
    _name = 'excise.category.rate'
    _description = 'Excise Rate'

    name = fields.Date(string='Start Date', required=True, index=True,
                           default=lambda self: fields.Date.today())
    category_id = fields.Many2one('excise.category', string='Category', readonly=True)
    rate = fields.Monetary('Rate')
    adomertek_kod = fields.Char('Rate Code', required=True, index=True)

    currency_id = fields.Many2one('res.currency', string="Currency", compute='_compute_currency', readonly = True)

    @api.depends('category_id')
    def _compute_currency(self):
        for ecr in self:
            ecr.currency_id = ecr.category_id.currency_id
