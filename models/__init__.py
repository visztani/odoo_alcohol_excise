from . import sale_order
from . import sale_order_line
from . import purchase_order
from . import purchase_order_line
from . import stock_picking
from . import product_template
from . import stock_warehouse
from . import partner
from . import excisesetup
from . import stock_move
from . import excise_move
from . import stock_move_line

_logger.info('ExciseMove model loaded.')

@api.model
def create(self, vals):
    _logger.info('Creating excise.move record with values: %s', vals)
    return super(excise_move, self).create(vals)

def unlink(self, vals):
    _logger.info('deleting excise.move record with values: %s', vals)
    return super(excise_move, self).unlink(vals)