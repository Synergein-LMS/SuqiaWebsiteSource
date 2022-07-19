# -*- coding: utf-8 -*-

import logging
import werkzeug

from odoo import http, _
from odoo.addons.auth_signup.controllers.main import AuthSignupHome
from odoo.exceptions import UserError, ValidationError
from odoo.http import request
import re

_logger = logging.getLogger(__name__)

try:
    from validate_email import validate_email
except ImportError:
    _logger.debug("Cannot import `validate_email`.")


class SignupVerifyEmail(AuthSignupHome):
    @http.route()
    def web_auth_signup(self, *args, **kw):
        return self.passwordless_signup(http.request.params)

    def do_signup(self, qcontext):
        """ Shared helper that creates a res.partner out of a token """
        values = {key: qcontext.get(key) for key in ('login', 'name', 'password')}
        password_regex = ['^', '(?=.*?[a-z])', '(?=.*?[A-Z])', '(?=.*?\\d)', '(?=.*?\\W)', '.{8,}$']
        if not re.search(''.join(password_regex), values.get('password')):
            raise UserError(_(self.password_match_message()))
        if values.get('password') != qcontext.get('confirm_password'):
            raise UserError(_("Passwords do not match."))
        supported_lang_codes = [code for code, _ in request.env['res.lang'].get_installed()]
        lang = request.context.get('lang', '').split('_')[0]
        if lang in supported_lang_codes:
            values['lang'] = lang
        self._signup_with_values(qcontext.get('token'), values)
        request.env.cr.commit()

    def password_match_message(self):
        message = []
        message.append('* ' + _('Password must be 8 characters or more \n'))
        message.append('* ' + _('Lowercase letter \n'))
        message.append('* ' + _('Uppercase letter \n'))
        message.append('* ' + _('Numeric digit \n'))
        message.append('* ' + _('Special character'))
        if len(message):
            message = [_('Must contain the following:')] + message
        return '\r'.join(message)

    def passwordless_signup(self, values):
        qcontext = self.get_auth_signup_qcontext()

        if not values.get("login"):
            return http.request.render("auth_signup.signup", qcontext)

        if not (values.get("login") or values.get("password") or values.get("confirm_password")):
            qcontext["error"] = _("Required field are missing.")
            return http.request.render("auth_signup.signup", qcontext)
        # Check field values are valid
        if not validate_email(values.get("login", "")):
            qcontext["error"] = _("That does not seem to be an email address.")
            return http.request.render("auth_signup.signup", qcontext)
        elif values.get('login') != qcontext.get('confirm_email'):
            qcontext["error"] =  _("Email and Confirm Email does't match.")
            return http.request.render("auth_signup.signup", qcontext)
        password_regex = ['^', '(?=.*?[a-z])', '(?=.*?[A-Z])', '(?=.*?\\d)', '(?=.*?\\W)', '.{8,}$']
        if not re.search(''.join(password_regex), values.get('password')):
            qcontext["error"] =  _(self.password_match_message())
            return http.request.render("auth_signup.signup", qcontext)
        elif values.get("password") != values.get("confirm_password"):
            qcontext["error"] = _("Password and Confirm Password does't match.")
            return http.request.render("auth_signup.signup", qcontext)
        elif not values.get("email"):
            values["email"] = values.get("login")

        sudo_users = (http.request.env["res.users"].with_context(create_user=True).sudo())
        full_name = qcontext.get('name') +' '+qcontext.get('middlename') + ' '+qcontext.get('lastname')
        values['name']=full_name
        values['phone']=values.get("contact_number")
        values.pop('middlename')
        values.pop('lastname')
        values.pop('confirm_email')
        values.pop('g-recaptcha-response')
        try:
            values.pop('confirm_password')
            values.pop('contact_number')
            values.pop('redirect')
            values.pop('token')
            sudo_users.activate_signup(values, qcontext.get("token"))
            sudo_users.account_active(values.get("login"))
        except Exception as error:
            _logger.exception(error)
            http.request.env.cr.rollback()
            qcontext["error"] = _("Something went wrong, please try again later.")
            return http.request.render("auth_signup.signup", qcontext)

        welcome_msg = """Thank you for registering for the Award. A verification link has been sent to your email to complete the registration process and activate your account. 
                        If you did not receive a verification link, please email us at award@suqia.ae """
        qcontext["message"] = _(welcome_msg)
        qcontext["title"] = _('Registration Success')
        return werkzeug.utils.redirect('/registration-success')
        # return http.request.render("auth_signup.reset_password", qcontext)

    @http.route('/web/activate', type='http', auth='public', website=True)
    def web_signup_account_active(self, *args, **kw):
        qcontext = self.get_auth_signup_qcontext()

        if not qcontext.get('token'):
            raise werkzeug.exceptions.NotFound()

        if 'error' not in qcontext and request.httprequest.method == 'GET':
            try:
                User = request.env['res.users'].sudo().search(
                    [('login', '=', qcontext.get('login')), ('active', '=', False)])
                if User.partner_id.signup_token == qcontext['token']:
                    User.partner_id.signup_token = False
                    User.partner_id.signup_type = False
                    User.partner_id.signup_expiration = False
                    User.active = True

                    qcontext["message"] = _("Your account activated.")
                    return werkzeug.utils.redirect('/account-activated')
                    # return werkzeug.utils.redirect('/web/login')
                else:
                    qcontext['error'] = _("Invalid or expired token number.")
            except Exception as e:
                qcontext['error'] = _(e.message)

            return http.request.render("auth_signup.signup", qcontext)
