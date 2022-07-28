from odoo import fields, models

class FlotaSerrano(models.Model):
#    _name = 'flota.serrano'
#    _description = 'Flota Serrano'
    _inherit = "sale.order"
#    _sql_constraints = [
#        ('name_description_check',
#         'CHECK(name != description)',
#         "The title of the course should not be the description"),

#        ('name_unique',
#         'UNIQUE(name)',
#         "The course title must be unique"),
#    ]
    marca = fields.Char(
        string="Marca",
    )
#    modelo = fields.Char(
#        string="Modelo",
#        required=True,
#    )
#    no_economico = fields.Char(
#        string="No.Económico",
#        required=True,
#    )
#    placa = fields.Char(
#        string="Placas",
#        required=True,
#    )
#    tipo = fields.Char(
#        string="Tipo",
#        required=True,
#    )
#    conductor = fields.Many2one(
#        comodel_name='hr.employee',
#        ondelete='set null',
#        index=True,
#    )
#    no_chasis = fields.Char(
#        string="Chasis",
#        required=True,
#    )
#    f_registro = fields.Char(
#        string="Fecha de Registro",
#        required=True,
#    )
#    empresa = fields.Char(
#        string="Empresa",
#        required=True,
#    )
  
#    def copy(self, default=None):
#        default = dict(default or {})
#        copied_count = self.search_count(
#            [('name', '=like', u"Copy of {}%".format(self.name))])
#        if not copied_count:
#            new_name = u"Copy of {}".format(self.name)
#        else:
#            new_name = u"Copy of {} ({})".format(self.name, copied_count)
#
#        default['name'] = new_name
#        return super(FlotaSerrano, self).copy(default)
