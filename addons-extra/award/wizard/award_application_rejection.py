# -*- coding: utf-8 -*-

from odoo import api, fields, models


class AwardApplicationRejection(models.TransientModel):
    _name = 'award.application.rejection'
    _description = 'Get Rejection Reason'

    rejection_id = fields.Many2one('rejection.reason', String='Rejection Reason')
    rejection_remarks = fields.Text(String='Rejection remarks')

    def action_rejection_reason(self):
        application = self.env['award.application.form'].browse(self.env.context.get('active_ids'))
        application.write({'rejection_id':self.rejection_id.id,'rejection_remarks':self.rejection_remarks})
        application.action_cancel()
