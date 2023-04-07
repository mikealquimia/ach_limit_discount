# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import AccessError, UserError

class CrmTeam(models.Model):
    _inherit = 'crm.team'

    limit_discount = fields.Float(string="Discount limit")

    @api.onchange('limit_discount')
    def _onchange_limit_discount(self):
        for rec in self:
            if rec.limit_discount > 100:
                raise UserError(_('You cannot assign a discount limit greater than 100%')) 
            if rec.limit_discount < 0:
                raise UserError(_('You cannot assign a discount limit less than 0%')) 
                