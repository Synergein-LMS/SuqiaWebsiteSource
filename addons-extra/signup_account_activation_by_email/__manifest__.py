# -*- coding: utf-8 -*-
#################################################################################
# Author      : Kanak Infosystems LLP. (<https://www.kanakinfosystems.com/>)
# Copyright(c): 2012-Present Kanak Infosystems LLP.
# All Rights Reserved.
#
#
# This program is copyright property of the author mentioned above.
# You can`t redistribute it and/or modify it.
#
#
# You should have received a copy of the License along with this program.
# If not, see <https://www.kanakinfosystems.com/license>
#################################################################################


{
    "name": "Account Activate by email at signup",
    "summary": "Email confirmation to activation link",
    "version": "1.0",
    "category": "Authentication",
    'license': 'OPL-1',
    "author": "Kanak Infosystems LLP.",
    'website': 'https://www.kanakinfosystems.com',
    'images': ['static/description/banner.jpg'],
    "depends": ["website", "auth_signup","contacts"],
    "data": [
        "data/auth_signup_data.xml",
        "views/signup_templates.xml",
    ],
    "external_dependencies": {
        "python": [
            "validate_email",
        ],
    },
    'installable': True,
    'price': 30,
    'currency': 'EUR',
}
