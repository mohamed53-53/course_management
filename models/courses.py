# -*- coding: utf-8 -*-

from odoo import models, fields, api, _

from odoo.exceptions import ValidationError
from dateutil import relativedelta

from datetime import date


class courses(models.Model):
    _name = "courses"
    _inherit = ['mail.thread', 'mail.activity.mixin']
    _description = "Coursers"
    _rec_name = "name"

    name = fields.Char("Name", tracking=True)
    start_date = fields.Date(string="Start Date", default=fields.Date.context_today)
    end_date = fields.Date(string="End Date",)
    duration_per_day = fields.Integer('Duration Per Day',)
    course_content = fields.Text(string="Course Content")
    course_capacity = fields.Integer('Course Capacity', )
    available_seats = fields.Integer('Available Seats', compute="compute_available_seats")
    student_id = fields.Many2one('student', string="Student")
    instructor_id = fields.Many2one('res.users', string="Instructor")
    student_ids = fields.One2many("student.lines", "courses_id", string="Students")

    @api.constrains('start_date', 'end_date')
    def check_date(self):
        if self.start_date > self.end_date:
            raise ValidationError('End Date Must Be Later Than Start Date')

    @api.onchange("student_ids")
    def compute_available_seats(self):
        for rec in self:
            if rec.student_ids:
                count = rec.course_capacity - len(rec.student_ids)
                if count != 0:
                    rec.available_seats = count
                else:
                    rec.available_seats = 0
            else:
                rec.available_seats = rec.course_capacity
            print(rec.student_ids)

    @api.onchange("student_ids")
    def onchange_student_ids(self):
        if self.available_seats < 0:
            raise ValidationError('No Available Seats')

    @api.onchange("student_ids")
    def _check_duplicate_students(self):
        students = []
        for rec in self:
            for line in rec.student_ids:
                if line.student_id.id in students:
                    raise ValidationError('Duplicate Student found in Student Lines.')
                students.append(line.student_id.id)
                print(students)


class AppointmentPharmacyLines(models.Model):
    _name = "student.lines"

    student_id = fields.Many2one('student')

    courses_id = fields.Many2one('courses', string="Courses")







