from odoo import fields, models, api
from odoo.exceptions import ValidationError

class Goithau(models.Model):
    _name = 'goithau'

    ma_goithau = fields.Integer(string='ID của Gói thầu')
    # donvi = fields.Integer(string='ID của Đơn vị')
    donvi_id = fields.Many2one(comodel_name='donvi', string='Đơn vị')

    # ma_linh_vuc_dau_thau = fields.Integer(string='Mã Lĩnh vực đấu thầu')
    linhvucdauthau_id = fields.Many2one(comodel_name='linhvucdauthau', string='Lĩnh vực Đấu thầu')

    # ma_hinh_thuc_dauthau = fields.Integer(string='Mã Hình thức Đấu thầu')
    hinhthucdauthau_id = fields.Many2one(comodel_name='hinhthucdauthau', string='Hình thức Đấu thầu')

    # ma_hinh_thuc_lcnt = fields.Integer(string='Mã Hình thức Lựa chọn Nhà thầu')
    hinhthuclcnt_id = fields.Many2one(comodel_name='hinhthuclcnt', string='Hình thức Lựa chọn Nhà thầu')



    ten_goithau = fields.Char(string='Tên Gói thầu')
    diadiem = fields.Char(string='Địa điểm triển khai')
    so_ngay_QDDT = fields.Char(string='Số, ngày QĐ đầu tư')
    Nam_QDDT = fields.Char(string='Năm QĐ đầu tư')
    chudautu = fields.Char(string='Chủ đầu tư')
    gia_du_toan = fields.Char(string='Giá dự toán')
    gia_trung_thau = fields.Char(string='Giá trúng thầu')
    ten_donvi_trung_thau = fields.Char(string='Tên đơn vị trúng thầu')
    thoigian_thuchien_hopdong_theo_QD = fields.Char(string='Thời gian thực hiện Hợp đồng theo QĐ')
    thoigian_thuchien_hopdong_thucte = fields.Char(string='Thời gian thực hiện Hợp đồng thực tế')
    giatri_hoanthanh = fields.Integer(string='Giá trị hoàn thành')
    von_da_thanhtoan = fields.Integer(string='Vốn đã thanh toán')
    da_quyet_toan = fields.Integer(string='Đã quyết toán')
    con_no_nha_thau = fields.Integer(string='Còn nợ nhà thầu')
    chuthich = fields.Char(string='Chú thích')
    date_BaoCao = fields.Datetime(string='Ngày báo cáo')

    def unlink(self):
        return super(Goithau, self).unlink()


    active = fields.Boolean(default=True, string='Active')
    def cancel_order(self):
        pass
        # self.active = not self.active

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