# -*- coding: utf-8 -*-
{
    'name': "Open Academy",

    'summary': """Manage trainings""",

    'description': """
       Open Academy module for managing trainings:
           - training courses
           - training sessions
           - attendees registration
   """,


    'author': "Mohammed Ashraf@OdooDeveloper",
    'website': "http://www.yourcompany.com",

    'category': 'Test',
    'version': '14.0',
    'depends': ['base'],
    'data': [
        'security/security.xml',
        'security/ir.model.access.csv',
        'views/course_view.xml',
        'views/session_view.xml',
        'views/partner_view.xml',
    ],

    'demo': [
        'demo/demo.xml',
    ],

}
