from odoo import api, fields, models

class Inventory(models.Model):
	_inherit = 'product.template'

	product_code = fields.Char('Produk Code')

# class InventoryProduct(models.Model):
# 	_inherit = 'product.product'

# 	# product_code = fields.Char(related='product_variant_ids.product_code',string="Description")

# 	product_code = fields.Char(string="Produk Code")
