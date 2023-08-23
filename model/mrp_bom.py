# Copyright 2015-22 ForgeFlow S.L. (https://www.forgeflow.com)
# License LGPL-3.0 or later (https://www.gnu.org/licenses/lgpl.html).
import operator as py_operator

from odoo import _, api, fields, models
from odoo.exceptions import UserError, ValidationError


class MrpBom(models.Model):
    _inherit = "mrp.bom"

    def action_open_child_products_tree_view(self):
        self.ensure_one()
        product_ids = []
        for bom_line in self.bom_line_ids:
            product_ids.append(bom_line.product_id.id)
        domain = [('id','in',product_ids)]
        view_id_tree = self.env.ref('product.product_product_tree_view')
        return {
            'name': self.display_name,
            'type': 'ir.actions.act_window',
            'res_model': 'product.product',
            'view_type': 'form',
            'view_mode': 'tree,form',
            'views': [(view_id_tree[0].id, 'tree'),(False,'form')],
            #'view_id ref="module_name.tree_view"': '',
            'target': 'current',
            'domain': domain,
        }
