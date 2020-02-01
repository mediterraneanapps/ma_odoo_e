# -*- coding: utf-8 -*-
{
    'name': "Base Web Dashboard",
    'category': '',
    'version': '1.0',
    'description':
        """
Odoo Dashboard View.
========================

This module defines the Dashboard view, a new type of reporting view. This view
can embed graph and/or pivot views, and displays aggregate values.
        """,

    "author": "Mediterranean Apps",
    "price": "125",
    "currency": "EUR",
    "support": "mediterranean.apps@gmail.com",    
    'depends': ['web'],
    'data': [
        'views/assets.xml',
    ],
    'qweb': [
        "static/src/xml/dashboard.xml",
    ],
    'license': 'OPL-1',
}
