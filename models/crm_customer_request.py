from odoo import models, fields, api


class crm_customer_request(models.Model):
    _name = "crm.customer.request"
    _description = 'CRM Customer Request'

    name = fields.Char(string='Title', required=True)
    description = fields.Text()

    opportunity_id = fields.Many2one('crm.lead', required=True, index=True)
    product_id = fields.Many2one('product.template', required=True, index=True)
    date = fields.Date(string="Date", default=fields.Date.today(), required=True)
    qty = fields.Float(string='Quantity', required=True, digits='Product UoS', default=1)
    qty_ordered = fields.Float(string="Quantity Ordered", compute='_qty_ordered')
    sale_order_line_id = fields.Many2one('sale order')
   