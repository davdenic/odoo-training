from odoo import fields, models

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
    fuel_type = fields.Selection(selection=[('solid_fuel', 'Solid Fuel'), ('liquid_fuel', 'Liquid Fuel'),
                           default="solid_fuel"])
    