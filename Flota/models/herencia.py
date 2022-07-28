from odoo import fields, models

class DatosViaje(models.Model):
    _inherit = 'flota.serrano'
    kilometraje = fields.int(
        string="Kilometraje",
        Required=True,
    )
    disel = fields.int(
        string="disel",
       Required=True,
    )