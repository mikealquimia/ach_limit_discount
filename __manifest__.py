# -*- coding: utf-8 -*-
{
    'name': "ach_limit_discount",
    'summary': """
        Limit discount for crm team""",
    'description': """
        Limit discount for crm team
    """,
    'author': "ACH",
    'category': 'Uncategorized',
    'version': '0.1',
    'depends': ['base', 'sale', 'sales_team'],
    'data': [
        'views/sale_order_views.xml',
    ],

}