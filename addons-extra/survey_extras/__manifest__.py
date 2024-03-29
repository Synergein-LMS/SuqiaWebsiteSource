{
    'name': "Enhanced Survey & CSAT Template",
    'version': "13.0.1.0",
    'author': "S&V",
    'category': "Extra Tools",
    'summary': """Customer Satisfaction Survey (CSAT), Conditional Questions, File Attachment & Regular Expression Input Pattern""",
    'license':'LGPL-3',
    'website': 'https://www.sandv.biz',
    'images' : ['static/description/banner.png'],
    'data': [
        'security/ir.model.access.csv',
        'views/survey_question_views.xml',
        'views/survey_extra_templates.xml',
        'views/survey_user_input_line_views.xml',
        'views/survey_survey_views.xml',
        'views/survey_label_category_views.xml',
    ],
    'demo': [],
    'depends': ['survey'],
    'installable': True,
    'application': True,
    'license': 'OPL-1',
    'price': 71,
    'currency': 'EUR',
    'support': 'odoo@sandv.biz'
}
