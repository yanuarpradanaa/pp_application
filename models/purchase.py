from odoo import api, fields, models

class saleOrder(models.Model):
	_inherit = 'purchase.order'

	sj_luar = fields.Boolean("Surat Jalan Luar")
	delivery_status = fields.Selection([('kirim', 'Kirim'), ('kembali', 'Kembali'), ('done', 'Done')], 'Delivery Status')

	sjl_line = fields.One2many('purchase.order.line', 'order_id', string='SJL Lines', copy=True)


class purchaseOrderLine(models.Model):
	_inherit = 'purchase.order.line'
	
	product_category = fields.Char(string="Category", related="product_id.categ_id.name")

	jml_druk = fields.Char("Jml Druk")
	
	finishing = fields.Selection([('Kirim', 'Kirim'),
								('Waterbase', 'Waterbase'),
								('Waterbase Kilap', 'Waterbase Kilap'),
								('Laminating Gloss', 'Laminating Gloss'),
								('Laminating Doff', 'Laminating Doff'),
								('UV', 'UV'),
								('Spot UV', 'Spot UV'),
								('Spot Pasir', 'Spot Pasir'),
								('OPV', 'OPV'),
								('Laminating Doff + Spot UV', 'Laminating Doff + Spot UV'),
								('Laminasi Duplex', 'Laminasi Duplex'),
								('Laminasi Eflute', 'Laminasi Eflute'),
								('Emboss', 'Emboss'),
								('Klise Emboss', 'Klise Emboss'),
								('Hot Print', 'Hot Print'),
								('Klise Hot Print', 'Klise Hot Print'),
								('Plong', 'Plong'),
								('Pisau Plong', 'Pisau Plong'),
								('Pretel', 'Pretel'),
								('Lem Manual', 'Lem Manual'),
								('Laminasi Karton', 'Laminasi Karton'),
								('Print Digital', 'Print Digital'),
								('Packing','Packing'),
								('Acc', 'Acc'),
								('Vernish Doff', 'Vernish Doff'),
								('Cetak Toko', 'Cetak Toko'),
								('Service', 'Service'),
								('Potong', 'Potong'),
								])
	sides = fields.Selection([('1 Sisi', '1 Sisi'), ('2 Sisi', '2 Sisi')])
	ukuran = fields.Char("Ukuran(PxL)")
	unit = fields.Selection([('pcs','pcs'),
							('druk','druk'),
							('koli','koli'),
							('lbr','lbr'),
							('sap','sap')
							])
