# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

from odoo.exceptions import ValidationError
from dateutil import relativedelta

from datetime import date


class Attendance(models.Model):
    _name = "attendance"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Attendance"



    date = fields.Date(string="Date", default=fields.Date.context_today)
    courses_id = fields.Many2one('courses', string="Courses")
    student_ids = fields.One2many(related='courses_id.student_ids', string="Students")


