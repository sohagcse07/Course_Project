
{
    'name': 'CRM Extension',
    'author': 'Sohag Hossain',
    'version': '19.0.1.0.0',
    'summary': 'This Module Extends CRM Functionality.',
    'depends': ['base' , 'crm'],
    'data': [
        'views/crm_lead_views.xml',
    ],
    'installable': True,
    'auto_install': False,
    'application': False,
}
