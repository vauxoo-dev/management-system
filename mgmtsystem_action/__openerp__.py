# -*- encoding: utf-8 -*-
##############################################################################
#    
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2010 Savoir-faire Linux (<http://www.savoirfairelinux.com>).
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
##############################################################################
{
    "name" : "Management System - Action",
    "version" : "1.0",
    "author" : "Savoir-faire Linux",
    "website" : "http://www.savoirfairelinux.com",
<<<<<<< ccdb4bd26de7eaa4305a9d2bdfa2170ba166363e
    "license" : "AGPL-3",
=======
    "license" : "AGPL",
>>>>>>> [CHG] AGPL license; set verion to 1.0
    "category" : "Management System",
    "description": """\
This module enables you to manage the different actions of your management system :
  * immediate actions
  * corrective actions
  * preventive actions
  * improvement opportunities.

WARNING: when upgrading from v0.1, data conversion is required, since there are subtancial changes to the data structure.
    """,
    "depends" : ['mgmtsystem','audittrail','crm_claim'],
    "init_xml" : [],
    "update_xml" : [
        'security/ir.model.access.csv',
        'mgmtsystem_action.xml',
        'action_sequence.xml',
        'board_mgmtsystem_action.xml',
        'workflow_mgmtsystem_action.xml',
    ],
    "demo_xml" : ['demo_action.xml',],
    "installable" : True,
}
# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:

