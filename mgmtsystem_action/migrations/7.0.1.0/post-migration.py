# -*- encoding: utf-8 -*-
#
#    OpenERP, Open Source Management Solution
#    This module copyright (C) 2013 Savoir-faire Linux
#    (<http://www.savoirfairelinux.com>).
#
#    This program is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as
#    published by the Free Software Foundation, either version 3 of the
#    License, or (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#

from openerp.openupgrade import openupgrade


def migrate_stage_id(cr):
    openupgrade.logged_query(cr, """UPDATE mgmtsystem_action SET stage_id = NULL""")
    for i in [('draft', 'New', 'lead'), ('open', 'Accepted as Claim', 'claim'), ]:
        openupgrade.logged_query(cr, """
            UPDATE mgmtsystem_action AS a
            SET stage_id = (SELECT id
                            FROM crm_claim_stage
                            WHERE state = %s
                            LIMIT 1)
            WHERE a.openupgrade_legacy_7_0_stage_id = (SELECT id
                                                       FROM crm_case_stage
                                                       WHERE name = %s
                                                         AND type = %s
                                                       LIMIT 1)""", i)


@openupgrade.migrate()
def migrate(cr, version):
    migrate_stage_id(cr)

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
