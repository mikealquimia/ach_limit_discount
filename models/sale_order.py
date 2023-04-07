# -*- coding: utf-8 -*-

from odoo import models, fields, api, _
from odoo.exceptions import AccessError, UserError

class SaleOrderLine(models.Model):
    _inherit = 'sale.order.line'

    @api.onchange('product_id', 'price_unit', 'product_uom', 'product_uom_qty', 'tax_id')
    def _onchange_discount(self):
        data_crm_team = self.env['crm.team'].search([])
        count = 0
        limit = 0
        for team in data_crm_team:
            for member in team.member_ids:
                if member.id == self.env.user.id:
                    count += 1
                    if team.limit_discount > limit or limit == 0:
                        limit = team.limit_discount
        if count == 0:
            raise UserError(_('You do not belong to any sales team or sales channel, ask the administrator to verify your user')) 
        for rec in self:
            if rec.discount > limit:
                note = "The sales team or sales channel to which you belong has a discount limit of:\n" + str(limit) + "% \n It is not possible to assign the assigned discount"
                raise UserError(str(note))
        res = super(SaleOrderLine, self)._onchange_discount()
        return res
    
    @api.onchange('discount')
    def _onchange_discount_specific_limit(self):
        data_crm_team = self.env['crm.team'].search([])
        count = 0
        limit = 0
        for team in data_crm_team:
            for member in team.member_ids:
                if member.id == self.env.user.id:
                    count += 1
                    if team.limit_discount > limit or limit > 0:
                        limit = team.limit_discount
        if count == 0:
            raise UserError(_('You do not belong to any sales team or sales channel, ask the administrator to verify your user')) 
        for rec in self:
            if rec.discount > limit:
                note = "The sales team or sales channel to which you belong has a discount limit of:\n" + str(limit) + "% \n It is not possible to assign the assigned discount"
                raise UserError(str(note))
            
    @api.model
    def _init_settings(self):
        try:
            config = self.env['res.config.settings'].sudo()
            config.set_values()
            config.get_values()
        except:
            print('ERROR')