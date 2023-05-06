# -*- coding: utf-8 -*-
{
    'name': "Sales Discount Limit",
    'summary': """
        Sales discount limit based on sales equipment""",
    'description': """
        Sales discount limit on sales order lines, based on limit assigned to sales team
    """,
    'author': "Gt Alchemy Development",
    'license': 'LGPL-3',
    'support': 'developmentalchemygx@gmail.com',
    'category': 'Sales',
    'version': '1.1',
    'price': 3.00,
    'currency': 'USD',
    'depends': ['base', 
                'sale',
                'sales_team',
                'sale_management',
                'crm'],
    'data': [
        'data/sale_params.xml',
        'security/discount_line_sale.xml',
        'views/sale_order_views.xml',
    ],
    'images': ['static/description/banner.png'],
}