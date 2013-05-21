# -*- coding: utf-8 -*-
##############################################################################
#
#    OpenERP, Open Source Management Solution
#    Copyright (C) 2013 Mariano Ruiz (Enterprise Objects Consulting)
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

from osv import osv

class res_partner_address(osv.osv):
    _name = "res.partner.address"
    _inherit = "res.partner.address"

    def name_search(self, cr, uid, name='', args=None, operator='ilike', context={}, limit=100, offset=0):
        from_clause = "SELECT a.id FROM res_partner_address a JOIN res_partner p on a.partner_id = p.id "
        if operator in 'ilike':
            param = "'%" + name + "%'"
        else:
            param = "'" + name + "'"
        where_clause = name and " a.name %(op)s %(name)s OR p.name %(op)s %(name)s " \
                                " OR a.city %(op)s %(name)s " % {'op': operator, 'name': param} or ''
        limit_str = limit and ' LIMIT %s' % limit or ''
        offset_str = offset and ' OFFSET %s' % offset or ''
        where_str = where_clause and (" WHERE %s" % where_clause) or ''
        cr.execute(from_clause + where_str + limit_str + offset_str)
        ids = map(lambda x: x[0], cr.fetchall())
        return self.name_get(cr, uid, ids, context=context)

res_partner_address()
