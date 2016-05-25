# coding: utf-8
############################################################################
#    Module Writen For Odoo, Open Source Management Solution
#
#    Copyright (c) 2016 Vauxoo - http://www.vauxoo.com
#    All Rights Reserved.
#    info Vauxoo (info@vauxoo.com)
#    coded by: Luis Torres <luis_t@vauxoo.com>
#    planned by: Sabrina Romero <sabrina@vauxoo.com>
############################################################################
from openerp import api, models


class MgmtsystemNonconformityReport(models.AbstractModel):
    _name = "report.mgmtsystem_nonconformity_report.nonconformity_report"

    @api.multi
    def render_html(self, data=None):
        report_obj = self.env["report"]
        report = report_obj._get_report_from_name(
            "mgmtsystem_nonconformity_report.nonconformity_report")
        docargs = {
            "doc_ids": self._ids,
            "doc_model": report.model,
            "docs": self,
            "members_team": self._members_team,
            "get_part_name": self._get_part_name,
        }
        return report_obj.render(
            "mgmtsystem_nonconformity_report.nonconformity_report", docargs)

    @api.multi
    def _members_team(self, nonconformity):
        """
        Return a list with the responsible, manager, author and users founds
        in the actions of this nonconformity, but not duplicates.
        """
        self.ensure_one()
        users = [nonconformity.responsible_user_id]
        if nonconformity.manager_user_id not in users:
            users.append(nonconformity.manager_user_id)
        if nonconformity.author_user_id not in users:
            users.append(nonconformity.author_user_id)
        for action in nonconformity.action_ids:
            if action.user_id not in users:
                users.append(action.user_id)
        return users

    @api.multi
    def _get_part_name(self, product, partner):
        """
        If the product related to this nonconformity have seller_ids, and the
        partner related to the same nonconformity is found in this seller_ids
        will return the Supplier Product Name of this, else only will return
        the product description.
        """
        for seller in product.seller_ids:
            if seller.name.id == partner.id:
                return seller.product_name
        return product.description
