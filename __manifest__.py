{
    'name':'alcohol-excise',
    'description':'Track excise on movements of alcoholic beverages subject to excise',
    'author':'visztani <- James Carr-Saunders',
    'website':'',
    'license':'LGPL-3',
    'category':'Operations',
    'depends':['base','product','stock', 'sale', 'sale_management', 'purchase'],
    'application':True,
    'installable': True,
    'data': [
        'views/excise_category_views.xml',
        'views/product_template_excise.xml',
        'views/excise_menu.xml',
        'views/stock_warehouse_excise.xml',
        'views/stock_picking_excise.xml',
        'views/excise_move_views.xml',
        'views/sale_order_view_excise.xml',
        'views/partner_excise.xml',
        'reports/excise_delivery_slip.xml',
        'reports/excise_delivery_slip_template.xml',
        'security/ir.model.access.csv',
        'data/excise_category_data.xml',
        'data/excise_category_rate_data.xml',

    ],
}