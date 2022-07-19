# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import UserError
from datetime import datetime, timedelta, date
from io import BytesIO
from psycopg2 import ProgrammingError
import xlwt,  base64, re


class AwardApplicationForm(models.Model):
    _name = "award.application.form"
    _inherit = ['portal.mixin', 'mail.thread', 'mail.activity.mixin']
    _description = "Award Form Details"
    _order = 'id desc'

    name = fields.Char(string='Application Reference', required=True, copy=False, readonly=True,index=True, default=lambda self: _('New'))
    partner_id = fields.Many2one('res.partner', string='Applicant', readonly=True, default=lambda self: self.env.user.partner_id.id)
    application_id = fields.Many2one('survey.user_input', string='Application Form', readonly=False)
    survey_id = fields.Many2one('survey.survey', string='Survey Name', readonly=True)
    token = fields.Char(string='Token', readonly=True, required=True)
    created_date = fields.Datetime(string='Created Date', readonly=True, index=True, copy=False, default=fields.Datetime.now)
    last_updated_by = fields.Many2one('res.users', string='Last Updated by', readonly=True, tracking=2)
    last_updated_date = fields.Date(string='Last Updated Date', readonly=True, tracking=2)
    category_id = fields.Many2one('award.category', string='Category Type')
    sub_category_id = fields.Many2one('award.sub.category', string='Sub Category Type')
    country_id = fields.Many2one('res.country', string='User Country')
    project_country_id = fields.Many2one('res.country', string='Project Country')
    reviewer_line = fields.One2many('award.reviewer.line','award_id', string='Reviewer Line')
    rejection_id = fields.Many2one('rejection.reason', String='Rejected Reason')
    rejection_remarks = fields.Text(String='Rejected Remarks')
    state = fields.Selection([
        ('draft', 'Screening'),
        ('first_review', 'Stage 1 Review'),
        ('second_review', 'Stage 2 Review'),
        ('final_review', 'Final Review'),
        ('finalist', 'Awarded'),
        ('cancel', 'Rejected'),
        ], string='Status', readonly=True, copy=False, tracking=3, index=True, default='draft')

    @api.model
    def create(self, vals):
        if vals.get('name', _('New')) == _('New'):
                vals['name'] = self.env['ir.sequence'].next_by_code('award.application.form') or _('New')
        return super(AwardApplicationForm, self).create(vals)

    @api.onchange('category_id')
    def onchange_category_id(self):
        self.sub_category_id = False
        sub_catg = self.category_id.sub_category_ids.ids
        if sub_catg:
            return {'domain':{'sub_category_id':[('id', 'in', sub_catg)]}}
        else:
            return {'domain':{'sub_category_id':[('id', '=', False)]}}

    def action_first_review(self):
        self.last_updated_by = self.env.user.id
        self.last_updated_date = fields.Date.today()
        return self.write({'state': 'first_review'})

    def action_second_review(self):
        self.last_updated_by = self.env.user.id
        self.last_updated_date = fields.Date.today()
        return self.write({'state': 'second_review'})

    def action_final_review(self):
        self.last_updated_by = self.env.user.id
        self.last_updated_date = fields.Date.today()
        return self.write({'state': 'final_review'})

    def action_finalist(self):
        self.last_updated_by = self.env.user.id
        self.last_updated_date = fields.Date.today()
        return self.write({'state': 'finalist'})

    def action_cancel(self):
        self.last_updated_by = self.env.user.id
        self.last_updated_date = fields.Date.today()
        return self.write({'state': 'cancel'})

    def action_print_answers(self):
        self.ensure_one()
        return {
            'type': 'ir.actions.act_url',
            'name': "View Answers",
            'target': 'new',
            'url': '/survey/print/%s?answer_token=%s' % (self.survey_id.access_token, self.token)
        }

    def get_answer_type_fields(self, answers):
        if answers.answer_type == 'text':
            return answers.value_text
        if answers.answer_type == 'number':
            return answers.value_number
        if answers.answer_type == 'date':
            return answers.value_date
        if answers.answer_type == 'datetime':
            return answers.value_datetime
        if answers.answer_type == 'free_text':
            return answers.value_free_text
        if answers.answer_type == 'suggestion':
            return answers.value_suggested.value
        if answers.answer_type == 'binary':
            return "Reference attached in ERP"

    def prepare_answes_printout(self):
        list_value=[]
        final_dict = {}
        value = {}
        for questions in self.survey_id.question_and_page_ids:
            if not questions.is_page:
                for answers in self.application_id.user_input_line_ids:

                    if questions.title == answers.question_id.title:
                        application_answer = self.get_answer_type_fields(answers)
                        list_value.append({'qn':questions.title, 'ans': application_answer})
        final_dict.update({'value':list_value})
        return final_dict

    def print_pdf_report(self):
        return self.env.ref('award.action_report_application_pdf').report_action(self)


class AwardReviewerLine(models.Model):
    _name = "award.reviewer.line"
    _description = "Award Reviewer Line"

    name = fields.Text(string='Remarks', required=True)
    review_datetime = fields.Datetime(string='Date and Time', readonly=True, default=fields.Datetime.now)
    user_id = fields.Many2one('res.users',string='User', readonly=True, default=lambda self: self.env.user.id)
    award_id = fields.Many2one('award.application.form',string="Award Application Form", readonly=True)


class SurveyUserInput(models.Model):
    _inherit = "survey.user_input"
    _description = 'Survey User Input Line'

    def _mark_done(self):
        res = super(SurveyUserInput, self)._mark_done()
        award_details = self.env['award.application.form'].sudo().create({
                                        'partner_id':self.partner_id.id,
                                        'application_id':self.id,
                                        'survey_id' : self.survey_id.id,
                                        'token' : self.token
                                        })
        for line in self.user_input_line_ids:
            if line.binary_data and line.answer_type == 'binary':
                attachement_id = self.env['ir.attachment'].create({
                    'name': line.question_id.title,
                    'type': 'binary',
                    'datas': line.binary_data,
                    'res_model': 'award.application.form',
                    'res_id': award_details.id,
                    'res_name': award_details.name,
                })
            if line.question_id.title == 'Country':
                country_id = self.env['res.country'].search([('name','=',line.value_suggested.value)])
                if country_id:
                    award_details.update({'country_id':country_id.id})
            if line.question_id.title == 'Project Country':
                project_country_id = self.env['res.country'].search([('name','=',line.value_suggested.value)])
                if project_country_id:
                    award_details.update({'project_country_id':project_country_id.id})
            category_search = self.env['award.category'].search(['|',('question_id.id','=',line.question_id.id),('label_id.id','=',line.value_suggested.id)])
            sub_catg = self.env['award.sub.category'].search([('label_id.id','=',line.value_suggested.id)])

            if category_search:
                award_details.update({'category_id':category_search.id})
            if sub_catg:
                award_details.update({'sub_category_id':sub_catg.id})

        return res