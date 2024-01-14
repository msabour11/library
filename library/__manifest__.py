# -*- coding: utf-8 -*-
{
    'name': "ZLibrary",
    'summary': "A brief summary of your module",
    'description': "A more detailed description of your module",
    'author': "Mohamed Sabour",
    'category': 'Productivity',
    'version': '16.0.1.0',
    'depends': ['base','mail','sale'],
    'application': True,
    'installable': True,
    'data': [
        'data/data.xml',
        'data/cron.xml',
        'security/security_groups.xml',
        'security/ir.model.access.csv',
        'security/record_rules.xml',
        'views/base_menus.xml',
        'views/book_view.xml',
        'views/publisher_view.xml',
        'views/sale_order_view.xml',
        'reports/book_print.xml',
        'reports/publisher_report.xml',
        'wizard/add_publisher_wizard_view.xml'
    ],
}
