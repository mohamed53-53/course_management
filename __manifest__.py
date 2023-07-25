# -*- coding: utf-8 -*-
{
    'name': "Course Management",
    'sequence': -100,
    'summary': """
        module for managing courses and student enrollments
        """,

    'description': """
        managing courses and student enrollments
    """,

    'author': "My Company",
    'website': "",

    # Categories can be used to filter modules in modules listing
    # Check https://github.com/odoo/odoo/blob/14.0/odoo/addons/base/data/ir_module_category_data.xml
    # for the full list
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': ['base',"mail"],

    # always loaded
    'data': [
        'security/ir.model.access.csv',
        'security/security.xml',
        'views/student.xml',
        'views/courses.xml',
        'views/attendance.xml',
    ],
    # only loaded in demonstration mode

    'installable': True,
    'application': True,
}
