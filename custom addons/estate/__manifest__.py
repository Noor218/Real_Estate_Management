# -*- coding: utf-8 -*-
# Part of Odoo. See LICENSE file for full copyright and licensing details.


{
    'name': 'Real-Estate Management',
    'version': '1.0',
    'category': 'Category',
    'sequence': -90,
    'description': """
    This is a test module of Real-Estate Management!
    Written for the Odoo Quickstart Tutorial.
   """,
    'depends': ['base'],
    'author': 'Osama Imran',
    'license': 'LGPL-3',
    'data': [
        'security/ir.model.access.csv',
        'views/estate_property_views.xml',
        'views/estate_menus.xml',
        'views/estate_property_tree.xml',
        'views/estate_property_form.xml',
        'views/estate_property_search.xml',
        'views/estate_property_tag_tree.xml',
        'views/estate_property_type_tree.xml',
        'views/estate_property_type_form.xml',
        'views/estate_property_offer_tree.xml',
        'views/estate_property_offer_form.xml',
        'views/res_users_views.xml',
   ],
    'installable': True,
    'auto_install': False,
    'application': True,
}
