from odoo import models, fields, api

class QcCustom(models.Model):
        _inherit = 'qc.inspection'

        jenis_kertas = fields.Char('Jenis Kertas')
        grammatur = fields.Char('Grammatur')
        panjang = fields.Integer('Panjang')
        lebar = fields.Integer('Lebar')
        tinggi = fields.Integer('Tinggi')
        qty_bundle = fields.Integer('Qty Per Bundle')
        
        description = fields.Text(string='Description')
        qty_sample = fields.Float(string='Qty Sample', default=1.00)
        so_ref = fields.Many2one('sale.order', 'SO Reference', store=True)
        product_ref = fields.Many2one('product.product', 'Product', store=True)