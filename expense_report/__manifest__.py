{


    'name': 'Custom Expense Report',
    'version': '19.0.1.0.0',
    'author': 'Sohag Hossain',

    'summary': 'Custom Expense Report for practice ',

    'depends': ['base','hr_expense'],
    'data': [

        'report/report_templates.xml',
        'report/report_actions.xml',
    ],

    'installable': True,
    'application': False,
    
}