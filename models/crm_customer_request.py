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
    qty_sale_order = fields.Many2one('sale.order.line', string="Sale Order Quantity")
    total_qty = fields.Float(string="Sales", compute="_compute_total_qty", readonly=True)

    @api.depends("qty", "qty_sale_order")
    def _qty_ordered(self):
        for r in self:
            r.qty_ordered = r.qty * r.qty_sale_order.product_uom_qty

    @api.depends("qty")
    def _compute_total_qty(self):
        total = 0
        for r in self.qty:
            total += r.qty
        self.total_qty = total



