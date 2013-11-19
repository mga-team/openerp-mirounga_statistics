# -*- coding: utf-8 -*-
##############################################################################
#
#    mirounga_statistics module for OpenERP, Statistics on partner and product
#    Copyright (C) 2013 MIROUNGA (<http://www.mirounga.fr/>)
#              Christophe CHAUVET <christophe.chauvet@mirounga.fr>
#
#    This file is a part of mirounga_statistics
#
#    mirounga_statistics is free software: you can redistribute it and/or modify
#    it under the terms of the GNU Affero General Public License as published by
#    the Free Software Foundation, either version 3 of the License, or
#    (at your option) any later version.
#
#    mirounga_statistics is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU Affero General Public License for more details.
#
#    You should have received a copy of the GNU Affero General Public License
#    along with this program.  If not, see <http://www.gnu.org/licenses/>.
#
##############################################################################

{
    'name': 'Products and Partners Statistics',
    'version': '1.0',
    'category': 'Sales Management',
    'description': """Statistics on partners and products

    Display on line per year, with 12 columns.
    """,
    'author': 'MIROUNGA',
    'website': 'http://www.mirounga.fr/',
    'depends': [
        'product',
    ],
    'images': [],
    'data': [
        #'security/groups.xml',
        #'security/ir.model.access.csv',
        #'wizard/wizard.xml',
        #'report/report.xml',
    ],
    'demo': [],
    'test': [],
    #'external_dependancies': {'python': ['kombu'], 'bin': ['which']},
    'installable': True,
    'active': False,
    'license': 'AGPL-3',
}

# vim:expandtab:smartindent:tabstop=4:softtabstop=4:shiftwidth=4:
