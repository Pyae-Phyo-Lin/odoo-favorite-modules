{
    'name': 'Favorite Modules',
    'version': '1.0.0',
    'summary': 'Easily add any Odoo module as a favorite and filter favorite apps',
    'description': """
Favorite Modules Manager
========================
Easily mark any Odoo app or module as a favorite for quick access.

Tags:
favorite, bookmark, usability, productivity, apps, modules, tools

Features:
- Easily add any Odoo module
- Access favorites from the kanban menu
- Save time searching for frequently used apps
- Works with installed & custom modules
    """,
    'author': 'PYAE_PHYO',
    'license': 'LGPL-3',
    'category': 'Extra Tools',
    'depends': ['base'],
    'data': [
        'views/ir_module_inherit_view.xml',
    ],
    'images':[
        'static/description/banner.gif',
    ],
    'installable': True,
    'auto_install':True,

}