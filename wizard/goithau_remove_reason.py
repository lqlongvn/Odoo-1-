from odoo import fields, models, api


class GoithauRemoveReason(models.TransientModel):
    _name = 'goithau.remove.reason'

    goithau_remove_reason = fields.Selection(
        selection=[('1', 'Thông tin khai báo sai/thiếu'), ('2', 'Gói thầu chưa được cấp vốn'), ('3', 'Gói thầu đã quá thời hạn triển khai')], string='Reason')

    def update_goithau_remove_reason(self):
        pass