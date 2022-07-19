# -*- coding: utf-8 -*-

from odoo import api, fields, models, _
from odoo.exceptions import UserError


class DubaipayReconciliation(models.TransientModel):
    _name = 'dubaipay.reconciliation'
    _description = 'Dubaipay Reconciliation'

    from_date = fields.Date(String='Transaction From Date')
    to_date = fields.Date(String='Transaction To Date')
    status = fields.Selection([
        ('0', 'Success'),
        ('1', 'Failure')],
        String='Transaction Status'
    )

    def generate_xml_report_values(self):
        transaction_vals = {}
        transactions_list = []
        domain = [('date', '>=', self.from_date), ('date', '<=', self.to_date)]
        if int(self.status) == 0:
            domain += [('state', '=', 'done')]
        else:
            domain += [('state', '=', 'cancel')]
        payment_transactions = self.env['payment.transaction'].search(domain)
        if not payment_transactions:
            raise UserError(_("No transactions found during this period"))
        for transaction in payment_transactions:
            transaction_date = transaction.date.strftime('%d/%m/%Y %H:%M:%S')
            transactions_list.append({
                'SPTRN': transaction.reference,
                'TransDate': transaction_date,
                'Amount': transaction.amount,
                'DEGTRN': transaction.acquirer_reference,
                'Status': transaction.dubaipay_status_code,
                'PaymentMethod': transaction.dubaipay_payment_method or False
            })
        transaction_vals.update({'transaction_details': transactions_list})
        return transaction_vals

    def download_xml_file(self):
        self.generate_xml_report_values()
        return self.env.ref(
            'suqia_dubaipay_reconciliation.action_reconciliation_xml_report').report_action(self)
