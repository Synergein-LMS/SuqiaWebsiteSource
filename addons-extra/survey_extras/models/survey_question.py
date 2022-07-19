# -*- coding: utf-8 -*-
from odoo import api, fields, models
from odoo.exceptions import ValidationError
import logging
_logger = logging.getLogger(__name__)
import base64
import math

import os
import magic
import binascii

class SurveyQuestionConditional(models.Model):

    _inherit = "survey.question"
    
    conditional = fields.Boolean(string="Conditional")
    conditional_question_id = fields.Many2one('survey.question', string="Condition Question", help="The question which determines if this question is shown")
    conditional_option_id = fields.Many2one('survey.label', string="Condition Option", help="The option which determines if this question is shown")
    question_type = fields.Selection(selection_add=[('binary', 'File Attachment')])
    # size
    attachment_bool = fields.Boolean(string="Attachment must be in specified pattern", default=False)
    attachment_size = fields.Float(string="Attachment Size(Size in MB)", default=0.5)
    attachment_format = fields.Text(string="Attachment Format", Placeholder="['jpeg', 'png', 'pdf']")

    # for pattern in odoo standard textbox
    validation_is_sh_textbox_pattern = fields.Boolean('Input must be in specified pattern')
    validation_sh_textbox_pattern = fields.Char('Textbox Pattern')
    validation_sh_textbox_placeholder = fields.Char('Textbox Placeholder')
    

    def validate_binary(self, post, answer_tag):
        self.ensure_one()
        errors = {}
        # size_in_mb = 0
        answer = post[answer_tag]
        if self.constr_mandatory and not answer:
            errors.update({answer_tag: self.constr_error_msg})

        if answer and self.attachment_bool:
            str_file = str(answer.filename)
            suffix = str_file.split('.')[-1]
            if suffix not in self.attachment_format:
                errors.update({answer_tag: ('File Format should be' + ' ' +(self.attachment_format))})
            if len(str_file.split('.')) > 2:
                errors.update({answer_tag: ('Invalid File')})
            # -------------File Size-------------------
            attach_val = base64.encodestring(answer.read())
            magic_file = magic.Magic().from_buffer(base64.b64decode(attach_val))
            magic_split = magic_file.split(' ')[0]
            if magic_split.lower() not in self.attachment_format:
                errors.update({answer_tag: ('Invalid File')})
            file_size = len(attach_val) * 3 / 4  # base64
            if (file_size / 1024.0 / 1024.0) > self.attachment_size:
                errors.update({answer_tag: 'File is too Large!'})
            post.update({answer_tag:attach_val})
        return errors

    # def validate_binary(self, post, answer_tag):
    #     self.ensure_one()
    #     errors = {}
    #     # size_in_mb = 0
    #     answer = post[answer_tag]
    #     if self.constr_mandatory and not answer:
    #         errors.update({answer_tag: self.constr_error_msg})

    #     if answer and self.attachment_bool:
    #         str_file = str(answer.filename)
    #         suffix = str_file.split('.')[-1]
    #         if suffix not in self.attachment_format:
    #             errors.update({answer_tag: ('File Format should be' + ' ' +(self.attachment_format))})
    #         if len(str_file.split('.')) > 2:
    #             errors.update({answer_tag: ('Invalid File')})
    #         # -------------File Size-------------------
    #         attach_val = base64.encodestring(answer.read())
    #         file_size = len(attach_val) * 3 / 4  # base64
    #         if (file_size / 1024.0 / 1024.0) > self.attachment_size:
    #             errors.update({answer_tag: 'File is too Large!'})
    #         post.update({answer_tag:attach_val})
    #     return errors
