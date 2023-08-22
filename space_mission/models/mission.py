from odoo import api, fields, models
from odoo.exceptions import ValidationError
from odoo.tools import date_utils
from datetime import date
#import logging
#_logger = logging.getLogger(__name__)

class Mission(models.Model):
    _name = "space_mission.mission"
    _description = "Space mission Mission"

    name = fields.Char('Mission', required=True)

    mission_number = fields.Char(default="M-000", copy=False, required=True, readonly=True)
    
    active = fields.Boolean(default=True)

    launch_date = fields.Date()
    return_date = fields.Date()
    duration = fields.Integer(compute="_compute_mission_duration", 
                                inverse="_inverse_mission_duration", 
                                readonly=False)

    spaceship_id = fields.Many2one("space_mission.spaceship")
    crew_ids = fields.Many2many("res.partner")

    fuel = fields.Integer()
    engines = fields.Integer()    

    @api.model_create_multi
    def create(self, vals_list):
        for vals in vals_list:
            if vals.get('mission_number', ('M-000')) == 'M-000':
                vals['mission_number'] = self.env['ir.sequence'].next_by_code('mission.number')
        return super().create(vals_list)


    @api.constrains('launch_date', 'return_date')
    def _check_return_date(self):
        for record in self:
            if(record.launch_date > record.return_date):
                raise ValidationError('The return date cannot be before the launch date')

    @api.depends('launch_date', 'return_date')
    def _compute_mission_duration(self):
        #_logger.info(self.name)
        for record in self:
            if(record.launch_date and record.return_date):
                record.duration = (record.return_date - record.launch_date).days + 1

    def _inverse_mission_duration(self):
        for record in self:
            if(record.launch_date and record.duration):
                record.return_date = date_utils.add(record.launch_date, days=record.duration + 1)
        
        