from odoo import fields, models, api


class GoithauRemoveReason(models.TransientModel):
    _name = 'goithau.remove.reason'

    goithau_remove_reason = fields.Selection(
        selection=[('1', 'Thông tin khai báo sai/thiếu'), ('2', 'Gói thầu chưa được cấp vốn'), ('3', 'Gói thầu đã quá thời hạn triển khai')], string='Reason')

    def update_goithau_remove_reason(self):
        goithau_id = self.env.context.get('active_id', False)
        goithau_record = self.env['goithau'].browse(goithau_id)
        goithau_record.write({'goithau_remove_state': self.goithau_remove_reason})
        goithau_record.write({'state': '3'})
        return True
