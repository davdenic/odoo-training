from odoo import api, fields, models
from odoo.exceptions import ValidationError
from datetime import date

class Mission(models.Model):
    _name = "space_mission.mission"
    _description = "Space mission"

    name = fields.Char('Mission name', required=True)
    active = fields.Boolean(default=True)

    launch_date = fields.Date()
    return_date = fields.Date()

    spaceship_id = fields.Many2one("spaceship")
    crew_ids = fields.Many2many("res.contact")