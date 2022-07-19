# -*- coding: utf-8 -*-

{
    'name' : 'Award Form',
    'version' : '13.0.1.0.0',
    'summary': 'Award Application Form',
    'description': """This module manage Award applications.
    """,
    'author':'S&V',
    'category': 'Website',
    'depends' : ['survey','survey_extras','website','report_xml'],
    'data': [
        'security/award_security.xml',
        'security/ir.model.access.csv',
        'data/ir_sequence_data.xml',
        'data/award_appplication_form_data.xml',
        'data/category_data.xml',
        'report/award_application_reports.xml',
        'report/award_application_pdf_templates.xml',
        'wizard/award_application_rejection_views.xml',
        'views/portal_templates.xml',
        'views/survey_templates.xml',
        'views/award_form_views.xml',
        'views/award_category_views.xml',
    ],
    'website': 'http://www.sandv.biz',
    'installable': True,
    'application': True,
    'auto_install': False,
    'license': 'OPL-1',
    'support': 'odoo@sandv.biz'

}
