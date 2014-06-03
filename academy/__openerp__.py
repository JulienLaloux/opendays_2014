# -*- coding: utf-8 -*-
{
    'name': "Academy",
    # short description, used as subtitles on modules listings
    'summary': "",
    # long description of module purpose
    'description': """
""",
    # Who you are
    'author': "",
    'website': "",

    # categories can be used to filter modules in modules listing
    'category': 'Uncategorized',
    'version': '0.1',

    # any module necessary for this one to work correctly
    'depends': [
        'website',
        'website_event'
    ],
    'data': [
        'security/ir.model.access.csv',
        'templates/academy.xml',
        'data/teacher_assistant.xml',
        'data/lecture.xml',
        'view/teacher_assistant.xml',
    ],
    'tests': [
    ],
}
