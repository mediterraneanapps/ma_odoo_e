# -*- coding: utf-8 -*-

{
    'name': 'Theme Web Enterprise',
    'category': 'Themes/Backend',
    'version': '1.0',
    'description':
        """
Theme Enterprise Web Client.
===========================

This module modifies the web addon to provide Enterprise design and responsiveness.
        """,
    "author": "Mediterranean Apps",
    "price": "49",
    "currency": "EUR",
    "support": "mediterranean.apps@gmail.com",
    'depends': ['web'],
    'auto_install': True,
    'data': [
        'views/webclient_templates.xml',
    ],
   "images": [
        'static/description/panel_screen.PNG',
      
    ],
    'qweb': [
        "static/src/xml/*.xml",
    ],
     "license": "OPL-1",
}
