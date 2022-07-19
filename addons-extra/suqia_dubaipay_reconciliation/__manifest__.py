# -*- coding: utf-8 -*-

{
    'name' : 'DubaiPay Reconciliation',
    'version' : '13.0.1.0.0',
    'summary': 'Suqia Dubaipay Reconciliation',
    'description': """This module provide functions to reconcile dubaipay transaction.
    """,
    'author':'S&V',
    'category': 'payment',
    'website': "http://www.sandv.biz",
    'depends' : ['website','report_xml', 'payment_dubaipay'],
    'data': [
        'security/ir.model.access.csv',
        'report/dubaipay_reports.xml',
        'report/dubaipay_reconciliation_templates.xml',
        'wizard/dubaipay_reconciliation_view.xml',
    ],
    'website': 'http://www.sandv.biz',
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'OPL-1',
    'support': 'odoo@sandv.biz'
}
