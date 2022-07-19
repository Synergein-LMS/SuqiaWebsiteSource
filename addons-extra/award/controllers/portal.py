# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.

from odoo import fields, http, tools,  _
from odoo.exceptions import AccessError, MissingError
from odoo.http import request, route
from odoo.addons.portal.controllers.portal import CustomerPortal, pager as portal_pager, get_records_pager
from odoo.osv import expression
from odoo.addons.portal.controllers.mail import _message_post_helper
import base64
import re


class CustomersPortal(CustomerPortal):

    
    def _prepare_portal_layout_values(self):
        values = super(CustomersPortal, self)._prepare_portal_layout_values()
#            ***********Applications Count***********
        partner = request.env.user.partner_id
        application_obj = request.env['award.application.form']
        survey_obj = request.env['survey.user_input']
        application_count = application_obj.sudo().search_count([('partner_id', 'child_of', [partner.id])])
        survey = survey_obj.sudo().search([('partner_id', 'child_of', [partner.id]), ('state','!=','done'), ('test_entry','=',False)], order="id desc")
        if len(survey) > 1:
            survey = survey_obj.sudo().search([('partner_id', 'child_of', [partner.id]), ('state','!=','done'), ('test_entry','=',False)], order="id desc")[0]
            # survey = survey_obj.sudo().search([('partner_id', 'child_of', [partner.id]), ('state','=','skip'), ('test_entry','=',False)], order="id desc")[0]
        values.update({
            'application_count': application_count,
            'survey': survey,
        })    
        return values

    
    @http.route(['/my/application', '/my/application/page/<int:page>'], type='http', auth="user", website=True)
    def portal_my_application(self, page=1, date_begin=None, date_end=None, sortby=None, **kw):
        values = self._prepare_portal_layout_values()
        partner = request.env.user.partner_id
        application_obj = request.env['award.application.form']


        domain = [
            ('partner_id', 'child_of', [partner.id])
        ]

        searchbar_sortings = {
            'id': {'label': _('Order Date'), 'order': 'id desc'},
            'name': {'label': _('Reference'), 'order': 'name'},
        }
        
        # default sortby order
        if not sortby:
            sortby = 'name'
        sort_order = searchbar_sortings[sortby]['order']
        
        archive_groups = self._get_archive_groups('award.application.form', domain)

        domain += [(1, '=', 1)]
        # count for pager
        application_count = application_obj.sudo().search_count(domain)
        # make pager
        pager = portal_pager(
            url="/my/application",
            url_args={'date_begin': date_begin, 'date_end': date_end, 'sortby': sortby},
            total=application_count,
            page=page,
            step=self._items_per_page
        )
        # search the count to display, according to the pager data
        application = application_obj.sudo().search(domain, order=sort_order, limit=self._items_per_page, offset=pager['offset'])
        request.session['my_application_history'] = application.ids[:100]
        # body = _('Applications viewed by User %s') % application.partner_id.name
        body = ''
        _message_post_helper('res.partner', application.sudo().partner_id.id, body, message_type='notification', subtype="mail.mt_note")

        values.update({
            'date': date_begin,
            'application': application.sudo(),
            'page_name': 'Applications',
            'pager': pager,
            'archive_groups': archive_groups,
            'default_url': '/my/application',
            'searchbar_sortings': searchbar_sortings,
            'sortby': sortby,
        })
        return request.render("award.portal_my_application", values)

    def details_form_validate(self, data):
        error = dict()
        error_message = []

        # Validation
        for field_name in self.MANDATORY_BILLING_FIELDS:
            if not data.get(field_name):
                error[field_name] = 'missing'

        # name Validation
        if not re.match("^[\s+A-Za-z0-9_-]*$", data.get("name")):
            error["name"] = 'error'
            error_message.append(_('Invalid Input!'))

        # phone Validation
        if not re.match("^[\s+0-9_-]*$", data.get("phone")):
            error["phone"] = 'error'
            error_message.append(_('Invalid Input!'))

        # Street Validation
        if not re.match("^[\s+A-Za-z0-9_-]*$", data.get("street")):
            error["street"] = 'error'
            error_message.append(_('Invalid Input!'))

        # city Validation
        if not re.match("^[\s+A-Za-z0-9_-]*$", data.get("city")):
            error["city"] = 'error'
            error_message.append(_('Invalid Input!'))

        # zipcode Validation
        if not re.match("^[\s+0-9_-]*$", data.get("zipcode")):
            error["zipcode"] = 'error'
            error_message.append(_('Invalid Input!'))

        # company_name Validation
        if not re.match("^[\s+A-Za-z0-9_-]*$", data.get("company_name")):
            error["company_name"] = 'error'
            error_message.append(_('Invalid Input!'))

        if not re.match("^[\s+A-Za-z0-9_-]*$", data.get("vat")):
            error["vat"] = 'error'
            error_message.append(_('Invalid Input!'))
            
        # email validation
        if data.get('email') and not tools.single_email_re.match(data.get('email')):
            error["email"] = 'error'
            error_message.append(_('Invalid Email! Please enter a valid email address.'))


        # vat validation
        partner = request.env.user.partner_id
        if data.get("vat") and partner and partner.vat != data.get("vat"):
            if partner.can_edit_vat():
                if hasattr(partner, "check_vat"):
                    if data.get("country_id"):
                        data["vat"] = request.env["res.partner"].fix_eu_vat_number(int(data.get("country_id")), data.get("vat"))
                    partner_dummy = partner.new({
                        'vat': data['vat'],
                        'country_id': (int(data['country_id'])
                                       if data.get('country_id') else False),
                    })
                    try:
                        partner_dummy.check_vat()
                    except ValidationError:
                        error["vat"] = 'error'
            else:
                error_message.append(_('Changing VAT number is not allowed once document(s) have been issued for your account. Please contact us directly for this operation.'))

        # error message for empty required fields
        if [err for err in error.values() if err == 'missing']:
            error_message.append(_('Some required fields are empty.'))

        unknown = [k for k in data if k not in self.MANDATORY_BILLING_FIELDS + self.OPTIONAL_BILLING_FIELDS]
        if unknown:
            error['common'] = 'Unknown field'
            error_message.append("Unknown field '%s'" % ','.join(unknown))

        return error, error_message

    