# -*- coding: utf-8 -*-

{
    'name': 'Module_1',
    'version': '1.1',
    'summary': 'Đồ án của Long',
    'sequence': 3,
    'author': 'ITPlus, Long',
    'description': """
        8/6/21 Long khởi tạo theo hướng dẫn của thầy Minh
    """,
    'category': 'Other',
    'website': '',
    'depends': [],
    'data': [
        'wizard/goithau_remove_reason_view.xml',
        'views/goithau_view.xml',
        'views/user_view.xml',
        'views/donvi_view.xml',
        'views/thongtin_dauthau_view.xml',
        'security/security.xml',
        'security/ir.model.access.csv'
    ],
    'installable': True,
    'application': True,
}
