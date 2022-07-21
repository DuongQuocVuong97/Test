from odoo import models, fields
from odoo.exceptions import ValidationError


class Crm_lead(models.Model):
    _inherit = "crm.lead"

    request_ids = fields.Many2one("crm.lead", string="Request ID", ondetele="set null")
    name = fields.Char(string='Title', required=True)
    description = fields.Text()
    opportunity_id = fields.Many2one('crm.lead', required=True, index=True)
    product_id = fields.Many2one('product.template', required=True, index=True)
    date = fields.Date(string="Date", default=fields.Date.today(), required=True)
    qty = fields.Float('Quantity', required=True, digits='Product UoS', default=1)
    total_qty = fields.Many2many('sale.order.line')
    qty_ordered = fields.Float(string="Quantity Ordered", compute='_qty_ordered')

    def unlink(self):
        for r in self:
            if r.stage_id == 'New':
                return super(Crm_lead, self).unlink()
            else:
                raise ValidationError("You cannot delete %s as it is in %s status" % (self.name, self.stage_id))

    def write(self, vals):
        for r in self:
            if r.stage_id == 'New':
                return super(Crm_lead, self).write(vals)
            else:
                raise ValidationError("You cannot write %s as it is %s status" % (self.name, self.stage_id))
