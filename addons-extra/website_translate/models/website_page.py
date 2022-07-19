# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo.addons.http_routing.models.ir_http import slugify
from odoo import api, fields, models


class Page(models.Model):
    _inherit = 'website.page'
    _description = 'Page'

    title_name = fields.Char(string="Title Name", translate=True)
    

class Website(models.Model):

    _inherit = "website"
    _description = "Website"

    name = fields.Char('Website Name', required=True, translate=True)