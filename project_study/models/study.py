# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.
from odoo import api, fields, models, tools, _


class ProjectStudy(models.Model):
    _name = 'project.study'
    _description='player'
    REE = [('todo', 'TODO'),
           ('in-progress', 'IN-PROGRESS'),
           ('review', 'REVIEW'),
           ('done', 'DONE')]
    name = fields.Char(string="name")
    date = fields.Date(string="Date")
    dateLine = fields.Many2one('res.users', String='dateLine')
    description = fields.Html(String='description')
    status = fields.Selection(selection=REE, string='status', default='todo')
    note = fields.Text(String='Note')
