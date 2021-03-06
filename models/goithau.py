from odoo import fields, models, api
from odoo.exceptions import ValidationError

class Goithau(models.Model):
    _name = 'goithau'

    # ma_goithau = fields.Integer(string='ID của Gói thầu')

    donvi_id = fields.Many2one(comodel_name='donvi', string='Đơn vị')
    linhvucdauthau_id = fields.Many2one(comodel_name='linhvucdauthau', string='Lĩnh vực Đấu thầu')
    hinhthucdauthau_id = fields.Many2one(comodel_name='hinhthucdauthau', string='Hình thức Đấu thầu')
    hinhthuclcnt_id = fields.Many2one(comodel_name='hinhthuclcnt', string='Hình thức Lựa chọn Nhà thầu')


    # ten_goithau = fields.Char(string='Tên Gói thầu')
    name = fields.Char(string='Tên Gói thầu')
    diadiem = fields.Char(string='Địa điểm triển khai')
    so_ngay_QDDT = fields.Char(string='Số, ngày QĐ đầu tư', default='')
    Nam_QDDT = fields.Char(string='Năm QĐ đầu tư')
    chudautu = fields.Char(string='Chủ đầu tư')
    gia_du_toan = fields.Char(string='Giá dự toán')
    gia_trung_thau = fields.Char(string='Giá trúng thầu')
    ten_donvi_trung_thau = fields.Char(string='Tên đơn vị trúng thầu')
    thoigian_thuchien_hopdong_theo_QD = fields.Char(string='Th/gian th/hiện Hợp đồng theo QĐ')
    thoigian_thuchien_hopdong_thucte = fields.Char(string='Th/gian th/hiện Hợp đồng thực tế')
    giatri_hoanthanh = fields.Integer(string='Giá trị hoàn thành')
    von_da_thanhtoan = fields.Integer(string='Vốn đã thanh toán')
    con_no_nha_thau = fields.Integer(string='Còn nợ nhà thầu', compute='compute_con_no_nhathau', store=False)
    da_quyet_toan = fields.Integer(string='Đã quyết toán')
    chuthich = fields.Char(string='Chú thích')
    date_BaoCao = fields.Datetime(string='Ngày báo cáo')

    @api.depends('giatri_hoanthanh', 'von_da_thanhtoan')
    def compute_con_no_nhathau(self):
        for goi_thau in self:
            goi_thau.con_no_nha_thau = goi_thau.giatri_hoanthanh - goi_thau.von_da_thanhtoan


    def unlink(self):
        return super(Goithau, self).unlink()


    active = fields.Boolean(default=True, string='Active')
    def cancel_order(self):
        pass
        # self.active = not self.active

    goithau_remove_state = fields.Selection(
        selection=[('0', 'Gói thầu còn giá trị, chưa bị hủy'), ('1', 'Thông tin khai báo sai/thiếu'), ('2', 'Gói thầu chưa được cấp vốn'),
                   ('3', 'Gói thầu đã quá thời hạn triển khai')], string='Lý do hủy gói thầu')

    state = fields.Selection(
        selection=[('0', 'Nhập số liệu'), ('1', 'Trưởng đơn vị duyệt'), ('2', 'Admin duyệt'), ('3', 'Gói thầu đã hủy')],
        default='0', string='State')

    def chuyen_truongdv_duyet(self):
        self.state = '1'

    def truongdonvi_duyet_goithau(self):
        # raise ValidationError('Trưởng đơn vị đã Phê duyệt Gói thầu này!')
        self.state = '2'

    def truongdonvi_reject_goithau(self):
        # raise ValidationError('Trưởng đơn vị đã Phê duyệt Gói thầu này!')
        self.state = '0'

    def admin_duyet_goithau(self):
        self.state = '2'
        pass

    def remove_goithau(self):
        # raise ValidationError('Remove!')
        self.unlink()

    def khoiphuc_goithau(self):
        self.state = '0'

    def btn_huy_goithau(self):
        self.state = '3'
