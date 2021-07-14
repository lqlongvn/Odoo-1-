from odoo import models, fields, api

class Donvi(models.Model):
    _name = 'donvi'

    name = fields.Char(string='Tên rút gọn của Đơn vị')
    # ten_rutgon_donvi = fields.Char(string='Tên rút gọn của Đơn vị')
    ma_donvi = fields.Integer(string='Mã Đơn vị')
    ten_daydu_donvi = fields.Char(string='Tên đầy đủ  của Đơn vị')

    def button_donvi(self):
        pass

    goithau_ids = fields.One2many(comodel_name='goithau', inverse_name='donvi_id', string='Gói thầu')
    goithau_count = fields.Integer(compute='get_goithau_count', string='Gói Thầu ', store=False)
    @api.depends('goithau_ids')
    def get_goithau_count(self):
        for donvi in self:
            self.goithau_count = len(donvi.goithau_ids)
        return self.goithau_count

    user_ids = fields.One2many(comodel_name='tbl_user', inverse_name='donvi_id', string='User')
    tbluser_count = fields.Integer(compute='get_tbluser_count', string='User ', store=False)
    @api.depends('user_ids')
    def get_tbluser_count(self):
        for donvi in self:
            self.tbluser_count = len(donvi.user_ids)
        return self.tbluser_count

