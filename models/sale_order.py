from odoo import models, fields, api


class Sale_order(models.Model):
    _inherit = "sale.order"

    quotations_id = fields.Many2many('crm.lead', string="Quotations ID")
