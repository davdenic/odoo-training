from odoo import api, fields, models
from odoo.exceptions import ValidationError
from datetime import date

class Spaceship(models.Model):
    _name = "space_mission.spaceship"
    _description = "Space mission Spaceship"

    name = fields.Char('Ship name', required=True)
    active = fields.Boolean(default=True)
    type = fields.Selection(selection=[('freighter', 'Freighter'), 
                                       ('transport', 'Transport'), 
                                       ('scout_ship', 'Scout Ship'), 
                                       ('fighter', 'Fighter')
                                      ],
                           default="scout_ship")
    model = fields.Char(required=True)
    build_date = fields.Date()
    captain = fields.Char()
    required_crew = fields.Integer()
    length = fields.Float()
    width = fields.Float()
    height = fields.Float()
    engine_number = fields.Char()
    fuel_type = fields.Selection(selection=[('solid_fuel', 'Solid Fuel'), ('liquid_fuel', 'Liquid Fuel')],
                           default="solid_fuel")
    mission_ids = fields.One2many("space_mission.mission", "spaceship_id")

    @api.constrains('build_date')
    def _check_build_date(self):
        for spaceship in self:
            if(spaceship.build_date > date.today()):
                raise ValidationError('The build date cannot be in the future')

    
    @api.constrains('length', 'width')
    def _check_size(self):
        for spaceship in self:
            if(spaceship.width > spaceship.length):
                raise ValidationError('The width should be smaller than the length')