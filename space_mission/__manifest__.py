{
    'name': 'Odoo Space Mission',
    'summary': """Module for space mission logistic""",
    'description': """Odoo Inc. is trying to visit the Moon. 
    Module to handle space mission logistic:
        - Spaceship
        - Space crew
        """,
    'license': 'OPL-1',
    'author': 'David D.',
    'website': 'www.sozialinfo.ch',
    'category': 'Custom Modules',
    'depends': ['base'],
    'data': [
        "security/space_mission_groups.xml",
        "security/ir.model.access.csv",
        "security/space_mission_security.xml",
        "views/space_mission_menuitems.xml",
        "views/spaceship_views.xml",
    ],
    'demo': [
        'demo/spaceship_demo.xml'
    ],
    'application': True,
}