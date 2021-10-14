{
    'name': 'Prima Print Application',
    'version': '14.0.1.1.0',
    'category': 'Application',
    'summary': "Custom Module Odoo ERP untuk Prima Print",
    'author': 'Satu Soft',
    'website': 'http://www.satusoft.com',
    'description': """
        
    """,
    
    'depends': ['base', 'crm', 'sale', 'account', 'delivery', 'sale_crm', 'sale_management', 'purchase', 'stock', 'mrp', 
                'project', 'abs_sales_order_task', 'quality_control_mrp_oca', 'stock_picking_cancel_cs',
                'purchase_supplier_discount_invoice', 'account_parent', 'inventory_barcode_scanning', 'sale_isolated_quotation',
                'stock_force_date_app', 'stock_picking_invoice_link', 'ms_report_stock'
                ],
    
    'data': [
        'views/sale_view.xml',
        'views/inventory_view.xml',
        'views/crm_view.xml',
        'views/qc_view.xml',
        'views/manufacturing_view.xml',
        'views/purchase_view.xml',
        'reports/qo_report.xml',
        'reports/qo_report_doc.xml',
        'reports/so_report.xml',
        'reports/so_report_doc.xml',
        'reports/inv2_report.xml',
        'reports/inv2_report_doc.xml',
        'reports/inv_report.xml',
        'reports/inv_report_doc.xml',
        'reports/do_report.xml',
        'reports/do_report_doc.xml',
        'reports/po_report.xml',
        'reports/po_report_doc.xml',
        'reports/qc_report.xml',
        'reports/qc_report_doc.xml',
        'reports/mrp_report.xml',
        'reports/mrp_report_doc.xml',
        'reports/sjl_report.xml',
        'reports/sjl_report_doc.xml',

    ],
    'images': ['static/description/icon.png'],
    'application': True,
    'installable': True,
    'auto_install': False,
}
