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
                    limit = team.limit_discount
        if count == 0:
            raise UserError(_('Ested no pertenece a ningun equipo de ventas o canal de ventas, solicite verificar su usario al administrador')) 
        if count > 1:
            raise UserError(_('Ested pertenece a mas de un equipo de ventas o canal de ventas, solicite verificar su usuario al administrador'))
        for rec in self:
            if rec.discount > limit:
                raise UserError(_('El equipo de ventas o canal de ventas al que usted pertenece tiene un limite de descuento de:\n %s %\n No es posible asignar el descuento asginado') % limit)
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
                    limit = team.limit_discount
        if count == 0:
            raise UserError(_('Ested no pertenece a ningun equipo de ventas o canal de ventas, solicite verificar su usario al administrador')) 
        if count > 1:
            raise UserError(_('Ested pertenece a mas de un equipo de ventas o canal de ventas, solicite verificar su usuario al administrador'))
        for rec in self:
            if rec.discount > limit:
                raise UserError(_('El equipo de ventas o canal de ventas al que usted pertenece tiene un limite de descuento de: %s, no es posible asignar el descuento asginado') % limit)
