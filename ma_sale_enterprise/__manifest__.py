# -*- coding: utf-8 -*-

{
    'name': "Sale Dashboard",
    'version': "1.0",
    'category': "Sales/Sales",
    'summary': "Contains a Dashboard View for Sale Management",
    'description': """
                Contains a Dashboard View for Sale Management as entreprise edition
    """,

     "author": "Mediterranean Apps",
    "price": "25",
    "currency": "EUR",
    "support": "mediterranean.apps@gmail.com",   
    'depends': ['sale', 'ma_web_dashboard'],
    'data': [
        'report/sale_report_views.xml',
        'views/sale_enterprise_templates.xml',
    ],
    'demo': [
    ],
    "images": [
        'static/description/dashboard.png',
      
    ],
    'installable': True,
    'application': False,
    'auto_install': ['sale'],
    'license': 'OPL-1',
}
