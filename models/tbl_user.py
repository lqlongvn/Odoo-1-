from odoo import models, fields, api

class Tbl_user(models.Model):
    _name = 'tbl_user'

    user_name = fields.Char(string='User Name')
    phone = fields.Char(string='User Phone')
    email = fields.Char(string='Email')
    passw = fields.Char(string='Password')
    status = fields.Integer(string='Status')
    chuthich = fields.Char(string='Chú Thích')
    state = fields.Selection(
        selection=[('0', 'Admin'), ('1', 'Trưởng đơn vị'), ('2', 'User nhập liệu của đơn vị'), ('3', 'User đã hủy')], string='State')

    # donvi = fields.Integer(string='Thuộc đơn vị')
    donvi_id = fields.Many2one(comodel_name='donvi', string='Đơn vị')

    active = fields.Boolean(default=True, string='Active')

    def button_user(self):
        pass
        # self.active = not self.active