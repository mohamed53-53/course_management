# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

from odoo.exceptions import ValidationError
from dateutil import relativedelta

from datetime import date


class Student(models.Model):
    _name = "student"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Student"
    _rec_name = "name"

    name = fields.Char("Name", tracking=True)
    phone = fields.Char("Phone")
    email = fields.Char("Email")
    photo = fields.Binary(
        "Photo", help="Attach student photo"
    )
    courses_id = fields.Many2one('courses', string="Courses")
    courses_ids = fields.One2many("courses", "student_id", string="Students",compute="_get_courses_ids")


    def _get_courses_ids(self):
        for rec in self:
            lines = []
            courses = rec.env["student.lines"].search([('student_id.name','=',rec.name)])
            rec.courses_ids = False
            for course in courses:
                lines.append(course.courses_id.id)
            rec.update({
                'courses_ids': lines,
            })


    _sql_constraints = [('unique_phone', 'unique (phone)',
                         'phone must be unique !')]





