from odoo import models, fields, api
from odoo.addons.base.models.decimal_precision import dp
from odoo.exceptions import ValidationError


class crm_customer_request(models.Model):
    _name = "crm.customer.request"
    _description = 'CRM Customer Request'

    name = fields.Char(string='Title', required=True)
    description = fields.Text()

    opportunity_id = fields.Many2one('crm.lead', required=True, index=True)
    product_id = fields.Many2one('product.template', required=True, index=True)
    date = fields.Date(string="Date", default=fields.Date.today(), required=True)
    qty = fields.Float('Quantity', required=True, digits='Product UoS', default=1)
    total_qty = fields.Many2many('sale.order')
    qty_ordered = fields.Float(string="Quantity Ordered", compute='_qty_ordered')

    @api.depends("total_qty")
    def _qty_ordered(self):
        for r in self:
            r.qty_ordered = r.total_qty.amount_total

