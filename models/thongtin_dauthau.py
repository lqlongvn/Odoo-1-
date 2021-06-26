from odoo import models, fields, api

# linhvuc_dauthau
# hinhthuc_lcnt
# hinhthuc_dauthau


class Linhvuc_Dauthau(models.Model):
    _name = 'linhvucdauthau'

    # ten_lv_dauthau = fields.Char(string='Tên Lĩnh vực đấu thầu')
    name = fields.Char(string='Tên Lĩnh vực đấu thầu')
    ma_lv_dauthau = fields.Integer(string='Mã Lĩnh vực đấu thầu')
    goithau_ids = fields.One2many(comodel_name='goithau', inverse_name='linhvucdauthau_id', string='Gói thầu')

class Hinhthuc_Dauthau(models.Model):
    _name = 'hinhthucdauthau'

    # ten_ht_dauthau = fields.Char(string='Tên Hình thức Đấu thầu')
    name = fields.Char(string='Tên Hình thức Đấu thầu')
    ma_ht_dauthau = fields.Integer(string='Mã Hình thức Đấu thầu')
    goithau_ids = fields.One2many(comodel_name='goithau', inverse_name='hinhthucdauthau_id', string='Gói thầu')


class Hinhthuc_LCNT(models.Model):
    _name = 'hinhthuclcnt'

    # ten_hinhthuc_lcnt = fields.Char(string='Tên Hình thức Lựa chọn Nhà thầu')
    name = fields.Char(string='Tên Hình thức Lựa chọn Nhà thầu')
    ma_hinhthuc_lcnt = fields.Integer(string='Mã Hình thức Lựa chọn Nhà thầu')
    goithau_ids = fields.One2many(comodel_name='goithau', inverse_name='hinhthuclcnt_id', string='Gói thầu')

