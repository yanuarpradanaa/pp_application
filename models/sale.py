from odoo import api, fields, models
from datetime import datetime

class saleOrder(models.Model):
	_inherit = 'sale.order'

	is_done = fields.Boolean("DO Lunas?")
	# dicek = fields.Boolean('Sudah Dicek')
	kalk_date = fields.Date(string='Tanggal Kalkulasi', default=datetime.today(), required=True)
	note = fields.Text(string='Note',default="""- Harga belum termasuk PPN.\n- Harga sewaktu-waktu dapat berubah.\n- Jumlah pengiriman adalah +/-5% dari PO.""")


class saleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    specification = fields.Text('Specification')