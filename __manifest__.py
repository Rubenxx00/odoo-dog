{
    'name': 'Dog',
    'version': '1.1',
    'description': 'Module to manage Dogs',
    'summary': 'Create and view Dog records',
    'category': 'Tools',
    'author': 'Ruben',
    'website': 'www.yourwebsite.com',
    'depends': ['base', 'calendar', 'mail'],
    'data': [
        'views/calendar_event_view.xml',
        'views/dog_views.xml',
        'views/dog_breed_views.xml',
        'views/menu.xml',
        'security/ir.model.access.csv'
    ],
    'license': 'AGPL-3',
    'installable': True,
    'application': True,
    'auto_install': False,
}
