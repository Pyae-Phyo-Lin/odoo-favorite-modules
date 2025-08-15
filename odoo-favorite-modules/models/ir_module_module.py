from odoo import fields, models

class IrModuleModule(models.Model):
    _inherit = "ir.module.module"

    favo_module = fields.Boolean(
        string='Favourite',
        help='If checked, this module will appear at the top in Apps View.',
        default=False
    )


    def action_toggle_favo(self):
        for record in self:
            record.favo_module = not record.favo_module