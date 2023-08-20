from odoo import api, fields, models
from odoo.exceptions import ValidationError
from datetime import date

class Mission(models.Model):
    _name = "space_mission.mission"
    _description = "Space mission Mission"

    name = fields.Char('Mission', required=True)

    mission_number = fields.Char(default="M-000", copy=False, required=True, readonly=True)
    
    active = fields.Boolean(default=True)

    launch_date = fields.Date()
    return_date = fields.Date()

    spaceship_id = fields.Many2one("space_mission.spaceship")
    crew_ids = fields.Many2many("res.partner")

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('mission_number', ('M-000')) == 'M-000':
                vals['mission_number'] = self.env['ir.sequence'].next_by_code('mission.number')
        return super().create(vals_list)


    @api.constrains('launch_date', 'return_date')
    def _check_return_date(self):
        for mission in self:
            if(mission.launch_date > mission.return_date):
                raise ValidationError('The return date cannot be before the launch date')