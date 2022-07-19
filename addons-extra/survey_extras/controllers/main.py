# -*- coding: utf-8 -*-
import werkzeug
import json
import base64

import odoo.http as http
from odoo.http import request

from odoo.addons.survey.controllers.main import Survey

# from odoo.addons.website.models.website import slug


class WebsiteSurveyExtend(Survey):
    # Printing routes
    @http.route(['/survey/print/<model("survey.survey"):survey>',
                 '/survey/print/<model("survey.survey"):survey>/<string:token>'],
                type='http', auth='public', website=True)
    def print_survey(self, survey, token=None, **post):
        '''Display an survey in printable view; if <token> is set, it will
        grab the answers of the user_input_id that has <token>.'''

        survey_question = request.env['survey.question']
        user_input = request.env['survey.user_input']
        user_input_line = request.env['survey.user_input_line']

        question_ids = survey_question.sudo().search([('question_type', '=', 'binary'), ('survey_id', '=', survey.id)])
        user_input_id = user_input.sudo().search([('token', '=', token), ('survey_id', '=', survey.id)])

        user_input_line_binary = []
        for question in question_ids:
            user_input_line = user_input_line.search([
                ('user_input_id', '=', user_input_id.id),
                ('survey_id', '=', survey.id),
                ('question_id', '=', question.id),
                ('answer_type', '=', 'upload_file')
            ])
            user_input_line_binary.append(user_input_line)
        return request.render('survey.survey_print',
                              {'survey': survey,
                               'token': token,
                               'page_nr': 0,
                               'quizz_correction': True if survey.quizz_mode and token else False,
                               'user_input_line_binary': user_input_line_binary})



# class SurveyLeadController(http.Controller):

        
#     @http.route('/survey/partner/<survey_id>', type="http", auth="public", website=True)
#     def survey_partner(self, survey_id, **kw):
#         """Associate to partner from email"""
 
#         values = {}
#         for field_name, field_value in kw.items():
#             values[field_name] = field_value
#             my_partner = request.env['res.partner'].sudo().search([('email','=',values['email'])])[0]

#             survey_answer = request.env['survey.user_input'].sudo().search([('token','=',values['token'] )])
#             survey_answer.partner_id = my_partner.id

#             #Add the new partner to a campaign
#             for act in survey_answer.survey_id.campaign_id.activity_ids:
#                 if act.start:
#                     wi = request.env['marketing.campaign.workitem'].sudo().create({'campaign_id': survey_answer.survey_id.campaign_id.id, 'activity_id': act.id, 'res_id': my_partner.id})
#                     wi.process()
#                     request.env['mail.mail'].process_email_queue()
#         return werkzeug.utils.redirect("/")