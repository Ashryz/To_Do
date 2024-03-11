{
    'name': "HMS App",
    'summary': """ """,
    'description': """ """,
    'author': "Tarek Ashry",
    'category': '',
    'version': '17.0.0.1.0',
    'depends': ['base',
                'crm',
                ],
    'application': True,
    'data': [
        'views/base_menu.xml',
        'views/patient.xml',
        'views/department.xml',
        'views/doctor.xml',
        'wizard/patient_history_wizard.xml',
        'views/customers_inherit_view.xml',
        'security/security.xml',
        'security/ir.model.access.csv',
        'reports/patient_print.xml',
    ]
}
