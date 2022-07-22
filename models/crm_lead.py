from odoo import models, fields, api
from odoo.exceptions import ValidationError


class Crm_lead(models.Model):
    _inherit = "crm.lead"

    request_ids = fields.One2many('crm.customer.request', 'opportunity_id', string="Request ID")
    name = fields.Char(string='Title', required=True)
    description = fields.Text()
    opportunity_id = fields.Many2one('crm.lead', required=True, index=True)
    product_id = fields.Many2one('product.template', required=True, index=True)
    date = fields.Date(string="Date", default=fields.Date.today(), required=True)
    qty = fields.Float(string='Quantity', required=True, default=1)
    qty_ordered = fields.Float(string="Quantity Ordered", compute='_qty_ordered')
    total_qty = fields.Float(string="Sales", compute="_compute_total_qty", readonly=True)

    @api.depends("qty")
    def _compute_total_qty(self):
        total = 0
        for r in self.qty:
            total += r.qty
        self.total_qty = total

    # state = fields.Selection([
    #     ('new', 'New'),
    #     ('qualified', 'Qualified'),
    #     ('proposition', 'Proposition'),
    #     ('won', 'Won'),
    # ], string='Status', readonly=True, default='New')

    # def unlink(self):
    #     for r in self:
    #         if r.stage_id == 'new':
    #             return super(Crm_lead, self).unlink()
    #         else:
    #             raise ValidationError("You cannot delete %s as it is in %s status" % (self.name, self.stage_id))

    # def write(self, vals):
    #     for r in self:
    #         if r.stage_id == 'New':
    #             return super(Crm_lead, self).write(vals)
    #         else:
    #             raise ValidationError("You cannot write %s as it is %s status" % (self.name, self.stage_id))
