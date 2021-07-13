from odoo import models, fields, api

class Donvi(models.Model):
    _name = 'donvi'


    name = fields.Char(string='Tên rút gọn của Đơn vị')
    # ten_rutgon_donvi = fields.Char(string='Tên rút gọn của Đơn vị')
    ma_donvi = fields.Integer(string='Mã Đơn vị')
    ten_daydu_donvi = fields.Char(string='Tên đầy đủ  của Đơn vị')

    user_ids = fields.One2many(comodel_name='tbl_user', inverse_name='donvi_id', string='User')
    goithau_ids = fields.One2many(comodel_name='goithau', inverse_name='donvi_id', string='Gói thầu')

    def button_donvi(self):
        pass

    goithau_count = fields.Integer(compute='get_goithau_count', string='Gói Thầu ', store=False)

    def get_goithau_count(self):
        self.goithau_count = 8
        return self.goithau_count

    tbluser_count = fields.Integer(compute='get_tbluser_count', string='User ', store=False)

    def get_tbluser_count(self):
        self.tbluser_count = 6
        return self.goithau_count

