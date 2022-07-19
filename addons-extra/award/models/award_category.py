# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError
from datetime import datetime, timedelta, date


class AwardCategory(models.Model):
    _name = "award.category"
    _description = "Award Category"

    name = fields.Char(string='Award Category', required=True, copy=False)
    question_id = fields.Many2one('survey.question',string='Survey Question')
    label_id = fields.Many2one('survey.label',string='Category Label Question')
    sub_category_ids = fields.Many2many('award.sub.category',string='Sub Category')

class AwardSubCategory(models.Model):
    _name = "award.sub.category"
    _description = "Award Sub Category"

    name = fields.Char(string='Name', required=True, copy=False)
    label_id = fields.Many2one('survey.label',string='Survey Question')

class RejectionReason(models.Model):
    _name = "rejection.reason"
    _description = "Award Rejection Reason"

    name = fields.Char(string='Name', required=True, copy=False)