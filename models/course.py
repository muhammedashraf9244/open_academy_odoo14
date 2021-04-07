from odoo import models, api, fields


class OpenAcademyCourse(models.Model):

    _name = 'openacademy.course'
    name = fields.Char(string='Course Name', required=True, index=True)
    description = fields.Char(cope=False)
    responsible_id = fields.Many2one('res.users',
                                     ondelete='set null', string="Responsible", index=True,
                                     default=lambda self: self.env.uid)

    session_ids = fields.One2many(
        'openacademy.session', 'course_id', string="Sessions")

    _sql_constraints = [
        ('name_description_check',
         'CHECK(name != description)',
         "The title of the course should not be the description"),

        ('name_unique',
         'UNIQUE(name)',
         "The course title must be unique"),
    ]
