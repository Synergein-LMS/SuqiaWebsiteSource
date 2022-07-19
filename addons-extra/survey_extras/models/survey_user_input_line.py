# -*- coding: utf-8 -*-
from odoo import _,api, fields, models
import logging
# _logger = logging.getLogger(__name__)
import base64

import os
import tempfile
import binascii

class SurveyUserInputLineBinary(models.Model):

    _inherit = "survey.user_input_line"
    
    binary_data = fields.Binary(string="Binary Data")
    answer_type = fields.Selection(selection_add=[('binary', 'File Select')] )

    @api.model
    def save_line_binary(self, user_input_id, question, post, answer_tag):
        vals = {
            'user_input_id': user_input_id,
            'question_id': question.id,
            'page_id': question.page_id.id,
            'survey_id': question.survey_id.id,
            'skipped': False,
        }
        if question.constr_mandatory:
            file = post[answer_tag]
        else:
            file = post[answer_tag] if post[answer_tag] else None
        
        if answer_tag in post:
            vals.update({'answer_type': 'binary', 'binary_data': file})
        else:
            vals.update({'answer_type': None, 'skipped': True})
        # post.update({answer_tag:post[answer_tag]})
        old_uil = self.search([
            ('user_input_id', '=', user_input_id),
            ('survey_id', '=', question.survey_id.id),
            ('question_id', '=', question.id)
        ])
        if old_uil:
            old_uil.write(vals)
        else:
            old_uil.create(vals)
        return True
    




    # @api.model
    # def save_line_binary(self, user_input_id, question, post, answer_tag):
    #     vals = {
    #         'user_input_id': user_input_id,
    #         'question_id': question.id,
    #         'page_id': question.page_id.id,
    #         'survey_id': question.survey_id.id,
    #         'skipped': False,
    #     }
    #     if answer_tag in post:
    #         answer = ""
            
    #         if post[answer_tag] != '':
    #             answer = base64.encodestring(post[answer_tag].read() )
            
    #         vals.update({'answer_type': 'binary', 'binary_data': answer})
    #     else:
    #         vals.update({'answer_type': None, 'skipped': True})
    #     old_uil = self.search([('user_input_id', '=', user_input_id),
    #                                     ('survey_id', '=', question.survey_id.id),
    #                                     ('question_id', '=', question.id)]
    #                           )
    #     if old_uil:
    #         self.write(vals)
    #     else:
    #         self.create(vals)
    #     return True