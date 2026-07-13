
from odoo import models, fields
from odoo.exceptions import UserError, ValidationError

class CrmLead(models.Model):
    _inherit = 'crm.lead'

    confirmed_revenue = fields.Monetary(
        string='Confirmed Revenue',
        currency_field='company_currency',
    )

 
    referral_partner_id = fields.Many2one(
        comodel_name='res.partner',
        string='Referral Partner',
       
    )

    
    internal_remarks = fields.Text(
        string='Internal Remarks',
    )

    def action_set_won(self):
        for lead in self:
            if not lead.confirmed_revenue or lead.confirmed_revenue <= 0:
                raise ValidationError((
                    'Confirmed Revenue must be set and greater than zero '
                    'before "%s" can be marked as Won.'
                ) % lead.name)
        return super().action_set_won()

    def unlink(self):
        for lead in self:
            if lead.stage_id.is_won:
                raise UserError((
                    'Lead "%s" is already marked as Won and cannot be deleted.'
                ) % lead.name)
        return super().unlink()